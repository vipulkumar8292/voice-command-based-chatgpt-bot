import assemblyai as aai
from elevenlabs import generate, stream
from openai import OpenAI

class AI_Assistant:
    def __init__(self) -> None:
        aai.settings.api_key = "API-KEY"
        self.openai_client = OpenAI(api = "API_KEY")
        self.elevenlabs_api_key = "API-KEY"

        self.transcriber = None

       #prompt
        self.full_transcript = [
            {"role":"system", "content":"You're an encyclopedia who knows everything about indian states, their cultures and food. Be resourveful and efficient."}
        ]


    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(sample_rate = 16000,
                                                   on_data= self.on_data,
                                                   on_error = self.on_error,
                                                   on_open = self.on_open,
                                                   on_close=self.on_close,
                                                   end_utterance_silence_threshold=1000)
        
        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(microphone_stream)

    
    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        #print("Session ID:", session_opened.session_id)
        return


    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.generate_ai_response(transcript)
        else:
            print(transcript.text, end="\r")


    def on_error(self, error: aai.RealtimeError):
       # print("An error occured:", error)
       return


    def on_close(self):
        #print("Closing Session")
        return
    

    def generate_ai_response(self, transcript):

        self.stop_transcription()

        self.full_transcript.append({"role":"user", "content":transcript.text})
        print(f"\nUser: {transcript.text}", end="\r\n")

        response = self.openai_client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = self.full_transcript
        )

        ai_response = response.choices[0].message.content

        self.generate_audio(ai_response)

        self.start_transcription()


    def generate_audio(self, text):

        self.full_transcript.append({"role":"assistant", "content":text})

        print(f"\nAI Assistant: {text}")

        audio_stream = generate(
            api_key= self.elevenlabs_api_key,
            text = text,
            voice="Rachel",
            stream=True
        )

        stream(audio_stream)

greeting = "Thank you for selecting me to know about indian states and their cultures. I am here to tell you everything about Indian states and their culture."

ai_assistant = AI_Assistant()
ai_assistant.generate_audio(greeting)
ai_assistant.start_transcription

