import speech_recognition as sr
import pyttsx3
import asyncio
from livekit import Room, ConnectOptions

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# LiveKit setup (Modify these with your LiveKit credentials and server URL)
LIVEKIT_URL = "wss://your-livekit-server-url"
ROOM_NAME = "my-room"
ACCESS_TOKEN = "your-access-token"  # Use a valid access token for connection

# Function to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for command...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not catch that. Could you repeat?")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None

# Function to connect to LiveKit and start the conversation
async def start_livekit_conversation():
    # Connect to the LiveKit room
    room = await Room.connect(LIVEKIT_URL, ACCESS_TOKEN, room_name=ROOM_NAME)

    print("Connected to LiveKit room!")
    speak("Connected to LiveKit room.")

    # Start listening for voice commands and respond
    while True:
        command = listen_for_command()
        
        if command:
            if "join room" in command:
                speak("You are now in the room.")
            elif "leave room" in command:
                await room.disconnect()
                speak("You left the room.")
                break
            else:
                speak("I did not understand that command. Try again.")
                
# Run the livekit conversation in an event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_livekit_conversation())

