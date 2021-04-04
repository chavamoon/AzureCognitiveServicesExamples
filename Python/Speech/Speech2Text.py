import azure.cognitiveservices.speech as speech_service
import json
import os

# Reading config values from config.json
# Replace with your own api key and endpoint
with open('Speech/config.json') as config_file:
    config = json.load(config_file)
api_key = config['api_key']
endpoint = config['endpoint']
language = 'es-MX'
speech_config = speech_service.SpeechConfig(subscription=api_key,endpoint=endpoint,speech_recognition_language=language)
# Creates a recognizer
speech_recognizer = speech_service.SpeechRecognizer(speech_config=speech_config)

print("Say something...")
# Starts speech recognition, and returns after a single utterance is recognized.
# The end of a single utterance is determined by:
#  * listening for silence at the end
#  * until a maximum of 15 seconds
# The task returns the recognition text as result.
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query.
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
result = speech_recognizer.recognize_once()

# Checks the result.
if result.reason == speech_service.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speech_service.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speech_service.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
print("Speech recognition finished.")
