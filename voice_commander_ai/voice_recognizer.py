"""
Voice Recognition Module
Handles speech-to-text conversion using Google Speech Recognition
"""

import speech_recognition as sr
import pyttsx3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VoiceRecognizer:
    """Handles voice input recognition"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust microphone sensitivity
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def listen(self, timeout=10, phrase_time_limit=15):
        """
        Listen for voice input from user
        
        Args:
            timeout: Maximum time to wait for speech
            phrase_time_limit: Maximum duration of speech
            
        Returns:
            Recognized text or None if failed
        """
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            print("⏳ Processing audio...")
            text = self.recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text.lower()
            
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Error accessing Google Speech Recognition: {e}")
            return None
        except sr.WaitTimeoutError:
            logger.warning("No speech detected within timeout")
            return None
    
    def listen_continuous(self):
        """Listen for continuous voice commands"""
        print("🎤 Continuous listening enabled. Say 'stop' to exit...")
        commands = []
        
        while True:
            command = self.listen()
            if command is None:
                continue
            
            if "stop" in command:
                print("⛔ Stopping voice commander...")
                break
            
            commands.append(command)
        
        return commands
