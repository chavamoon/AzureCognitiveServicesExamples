import azure.cognitiveservices.speech as speech_service

class Speech2TextClient:
    '''
    The Speech2TextClient helps to connect with Azure Speech Cognitive Service

    :param str api_key: Speech service API Key ...
    :param str endpoint: Speech service endpoint ...
    :param str language: Speech service language ...
    '''
    def __init__(self, api_key, endpoint, language):
        api_key = api_key
        endpoint = endpoint
        language = language
        speech_config = speech_service.SpeechConfig(subscription=api_key,endpoint=endpoint,speech_recognition_language=language)
        self.Service =  speech_service.SpeechRecognizer(speech_config=speech_config) 
