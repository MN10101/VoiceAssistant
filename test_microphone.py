import speech_recognition as sr

recognizer = sr.Recognizer()

def test_microphone():
    mic_index = 1  # Set this after finding your mic index from the previous step

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Listening... Please speak now.")
            audio = recognizer.listen(source, timeout=5)
            print("Audio captured. Recognizing...")

            # Use Google Recognizer with language set
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
    except sr.WaitTimeoutError:
        print("Listening timed out. Please speak again.")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Speech recognition service is down. Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_microphone()
