import speech_recognition as sr
import pyaudio

print("Testing microphone...")

# List audio devices
p = pyaudio.PyAudio()
print("Available audio devices:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"{i}: {info['name']} - {info['maxInputChannels']} input channels")

p.terminate()

# Test speech recognition
r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening for 5 seconds...")
        audio = r.listen(source, timeout=5)
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")