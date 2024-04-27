An AI bot  which takes in voice commands and user can ask about Indian states and their cultures. However you can change the prompt as per your wish.

RUN: "python ai_assistant_call.py" in the command directory of project

IMPORTANT REQUIREMENTS
_____________________

*API KEYS: Kindly use the below api keys before running this program.
Required API KEYS: ASSEMBLYAI, ELEVENLABS, OPENAI 
In the __init__ method of CLASS AI_Assistant enter the respective API KEYS where "API-KEY" is mentioned.
			

*IMPORTANT PYTHON LIBRARIES INSTALLATIONS: Kindly install the following libraries before running this program.
Required installations------> pipinstall --upgrade openai
pip install assemblyai
pip install "assemblyai[extras]"
pip install elevenlabs
pip install mpv
pip install portaudio



Description of this project
___________________________

This project will take voice input from the user then changes that voice input in text transcript and that text transcipt will be used as the prompt to the OPENAI gpt-3.5 turbo model. Then the ouput text from the GPT model is converted into voice.

Vipul Kumar
Python AI/ML Developer SDE
email: vipulkumar8292@gmail.com
