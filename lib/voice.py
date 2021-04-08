from lib.analytics import Analtyics
from speech_recognition import WaitTimeoutError
from lib.preference import Preference
import time

import speech_recognition as sr

from lib.command import Command

class VoiceServer:
    def __init__(self):
        print("Voice Init")

    def recognize_speech_from_mic(self, recognizer, microphone):
            """Transcribe speech from recorded from `microphone`.

            Returns a dictionary with three keys:
            "success": a boolean indicating whether or not the API request was
                    successful
            "error":   `None` if no error occured, otherwise a string containing
                    an error message if the API could not be reached or
                    speech was unrecognizable
            "transcription": `None` if speech could not be transcribed,
                    otherwise a string containing the transcribed text
            """
            # check that recognizer and microphone arguments are appropriate type
            if not isinstance(recognizer, sr.Recognizer):
                raise TypeError("`recognizer` must be `Recognizer` instance")

            if not isinstance(microphone, sr.Microphone):
                raise TypeError("`microphone` must be `Microphone` instance")

            # adjust the recognizer sensitivity to ambient noise and record audio
            # from the microphone
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                tout = float(Preference().get_timeout())
                # try recognizing the speech in the recording
                # if a RequestError or UnknownValueError exception is caught,
                #     update the response object accordingly
                retVal = ""

                try:
                    audio = recognizer.listen(source, timeout=tout, phrase_time_limit=tout)
                    retVal = recognizer.recognize_google(audio)
                except WaitTimeoutError:
                    print("NA")
                except sr.RequestError:
                # API was unreachable or unresponsive
                    retVal = "API unavailable"
                except sr.UnknownValueError:
                # speech was unintelligible
                    retVal = "Unable to recognize speech"
            return retVal.lower()

    def listen(self,command : Command):
          # create recognizer and mic instances
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        stop = Preference().getInstance().get_stop()
        reload= Preference().getInstance().get_reload()
        while True:
            time.sleep(0.2)
            print("Listening")
            guess = self.recognize_speech_from_mic(recognizer, microphone)
            if guess == stop:
                print("Stopping Program")
                Analtyics.getInstance().print()
                break
            if guess == reload:
                Preference().getInstance().load()
                command.refresh()
                continue
            command.process(guess)



        
