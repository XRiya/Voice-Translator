# ShellHacks MAIN.py

# Variable definition
ifile = 'jobs.mp3'

import speech2text
import translate as translate_text
import play_sound as synthesize_text

# 1. Call speech2tex.py
speech2text_result = speech2text(ifile)

print('1. speech2text: \r\ntext: ' + speech2text_result.results[0].alternatives[0].transcript,'\r\nconfidence: %2.2f' % speech2text_result.results[0].alternatives[0].confidence)

# 2. Call translate.py

target = 'PT_BR'
translate_text_result = translate_text(target, speech2text_result.results[0].alternatives[0].transcript)

print('2. Translate Text: ', translate_text_result['translatedText']) # dict -> ['translatedText']

# 3. Call Text2Speech

fname = 'output.mp3'
synthesize_text_result = synthesize_text(translate_text_result['translatedText'], fname)

# 4. Play Sound

# import the library
# pip install playsound
# pip install pygobject
from playsound import playsound

playsound(fname)
