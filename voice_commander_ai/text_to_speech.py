"""
Text-to-Speech Module
Handles speech synthesis for AI responses
"""

import pyttsx3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextToSpeech:
    """Handles voice output"""
    
    def __init__(self, rate=150, volume=0.9):
        """
        Initialize text-to-speech engine
        
        Args:
            rate: Speech rate (default 150 words per minute)
            volume: Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Set voice (optional: select male or female voice)
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
    
    def speak(self, text):
        """
        Convert text to speech
        
        Args:
            text: Text to be spoken
        """
        try:
            print(f"🔊 Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Error in text-to-speech: {e}")
    
    def speak_async(self, text):
        """Non-blocking text to speech (for faster response)"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Error in async speech: {e}")
