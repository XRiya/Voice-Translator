'''speech2text.py
This method uses the Google Cloud Speech to Text API. 
'''
# ShellHacks SpeechtoText
# pip install --upgrade google-cloud-speech
# ffmpeg -i jobs.mp3 jobs.wav
# 01. speech2text

def speech2text(file):
	import os
	from google.cloud import speech
	# Google Cloud -> IAM & Admin -> create service Acc --> create key
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'hearandlisten-da50cb4c59a8.json'
	speech_client = speech.SpeechClient()

	# 1. Ex 1 local media file

	byte_data_mp3 = file.read() # file is a Fask "FileStorage" object. I can read it directly. https://stackoverflow.com/questions/63306323/typeerror-expected-str-bytes-or-os-pathlike-object-not-filestorage-keeps-popp
	audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

	## 2. Configure Media files

	config_mp3 = speech.RecognitionConfig(
		sample_rate_hertz=48000,
		enable_automatic_punctuation=True,
		language_code='en-US'
	)

	# 3. Transcibing the RecognitionAudio objects
	# needed to enable Google Cloud to Speech module on website

	response_standard_mp3 = speech_client.recognize(
		config=config_mp3,
		audio=audio_mp3
	)
	return(response_standard_mp3)
