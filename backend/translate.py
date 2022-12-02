## Google Translate
# pip install --upgrade google-cloud-translate
# google cloud likely is returning a protocol buffer, you can check out https://developers.google.com/protocol-buffers/docs/pythontutorial for details on how to work with them in python
# 2. translate.py

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import os 

    import six
    from google.cloud import translate_v2 as translate

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'hearandlisten-da50cb4c59a8.json'
    
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result_tr = translate_client.translate(text, target_language=target)

#     print(u"Text: {}".format(result_tr["input"]))
#     print(u"Translation: {}".format(result_tr["translatedText"]))
#     print(u"Detected source language: {}".format(result_tr["detectedSourceLanguage"]))

    return result_tr # type dict
    
# result_tr = translate_text('PT_BR', response_standard_mp3.results[0].alternatives[0].transcript)
