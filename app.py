''' This method starts a Flask instance and provides a small web application with a speech recognition service. 
You upload an mp3 file and get the transcript in the browser. 

if __name__ == "__main__": # this is for debug purposes and is only executed if the app.py is called by itself and not by another method
'''
from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import os
from google.cloud import speech

import backend.speech2text # import .py files from ./backend folder. works if an empty __init__.py file exists
import backend.translate 

app = Flask(__name__)

# This method will return what should be returned on the homepage

@app.route("/", methods=["GET", "POST"]) # decorator function --> the index() goes through the app.route() function.
def index():
	'''This is the main method who starts the Flask and initiates the method(s).'''
	
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "hearandlisten-da50cb4c59a8.json"
	speech_client = speech.SpeechClient()

#	Reset all values, if I don't do that I get an error message, everything that is in the return render_template() must be initialized! 
	transcript = ""
	result_speech2text = ""
	result_translate = ""
	target = ""
	fname = ""
	olang = ""
	
	if request.method == "POST":
		print("DEBUG : FORM DATA RECEIVED")

		#file does not exist or the file is blank
		if "file" not in request.files:
	   		return redirect(request.url)

		#if a file exists it will give me the file
		file = request.files["file"]
		if file.filename == "":
	   		return redirect(request.url)

#		This is the main loop for our processes

		if file:
			olang = request.form['olang'] # gets the form data (dropdown from html)
			fname = file.filename # for the return command
			
			# 1. Speech2Text
			response_standard_mp3 = backend.speech2text.speech2text(file)
			result_speech2text = response_standard_mp3.results[0].alternatives[0].transcript
			
			# 2. Translate
			target = olang #'PT_BR'
			result_translate = backend.translate.translate_text(target, result_speech2text)
			
			# Transcript
			transcript = result_translate['translatedText'] # dict -> ['translatedText']

	return render_template('index.html',result_speech2text = result_speech2text, fname = fname , transcript = transcript, olang = olang)
	
if __name__ == "__main__": 
   app.run(debug = True, threaded=True)
