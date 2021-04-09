import azure.cognitiveservices.vision.computervision as vision_services
from msrest.authentication import CognitiveServicesCredentials

class ComputerVisionClient:
    '''
    The ComputerVisionClient helps to connect with Azure Computer Vision Cognitive Service

    :param str api_key: Speech service API Key ...
    :param str endpoint: Speech service endpoint ...
    '''
    def __init__(self, api_key, endpoint, language):
        api_key = api_key
        endpoint = endpoint
        language = language
        credentials = CognitiveServicesCredentials(apikey)
        self.Service =  vision_services.ComputerVisionClient(endpoint, credentials)

