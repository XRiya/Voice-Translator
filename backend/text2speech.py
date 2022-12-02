## Google text to speech
# pip install --upgrade google-cloud-texttospeech
# 3. text2speech

def synthesize_text(text, fname):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    # https://cloud.google.com/text-to-speech/docs/voices
    voice = texttospeech.VoiceSelectionParams(
        #language_code="en-US",
        language_code='pt-BR',
        #name="en-US-Standard-C",
        name="	pt-BR-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(fname, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

##

#synthesize_text(response_standard_mp3.results[0].alternatives[0].transcript )
# synthesize_text(result_tr['translatedText'])
