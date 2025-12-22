"""
Voice Commander AI - Main Application
A voice-controlled AI assistant that listens to commands and responds
"""

import os
import sys
import logging
from voice_recognizer import VoiceRecognizer
from text_to_speech import TextToSpeech
from ai_brain import AIBrain

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class VoiceCommanderAI:
    """Main Voice Commander AI Application"""
    
    def __init__(self):
        """Initialize the voice commander AI"""
        try:
            print("\n" + "="*50)
            print("🤖 VOICE COMMANDER AI - Initializing...")
            print("="*50 + "\n")
            
            self.recognizer = VoiceRecognizer()
            self.speaker = TextToSpeech(rate=150, volume=0.9)
            self.brain = AIBrain()
            self.running = True
            
            print("✅ Voice Commander AI Ready!")
            print("Say 'help' to see available commands")
            print("Say 'stop' or 'bye' to exit\n")
            
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            self.running = False
    
    def run(self):
        """Run the main voice command loop"""
        if not self.running:
            print("❌ Failed to initialize. Exiting...")
            return
        
        try:
            while self.running:
                # Listen for voice input
                command = self.recognizer.listen()
                
                if command is None:
                    print("⚠️  Could not understand. Please try again.\n")
                    continue
                
                # Process command with AI brain
                response = self.brain.process_command(command)
                
                if response:
                    print(f"\n💬 AI Response: {response}\n")
                    # Speak the response
                    self.speaker.speak(response)
                
                # Check for exit commands
                if any(exit_word in command for exit_word in ['stop', 'exit', 'bye', 'goodbye']):
                    self.speaker.speak("Goodbye! Have a great day!")
                    self.running = False
                    break
        
        except KeyboardInterrupt:
            print("\n\n⛔ Voice Commander stopped by user")
            self.speaker.speak("Goodbye!")
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
        finally:
            self.cleanup()
    
    def run_single_command(self):
        """Run single command mode (useful for testing)"""
        print("\n" + "="*50)
        print("🎤 SINGLE COMMAND MODE")
        print("="*50 + "\n")
        
        command = self.recognizer.listen()
        
        if command:
            response = self.brain.process_command(command)
            if response:
                print(f"\n💬 AI Response: {response}\n")
                self.speaker.speak(response)
    
    def cleanup(self):
        """Cleanup resources"""
        print("\n✅ Voice Commander AI shut down successfully")
        sys.exit(0)


def main():
    """Main entry point"""
    print("\n" + "="*50)
    print("    VOICE COMMANDER AI")
    print("="*50)
    print("\nOptions:")
    print("1. Start listening to commands")
    print("2. Single command mode")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    ai = VoiceCommanderAI()
    
    if choice == '1':
        ai.run()
    elif choice == '2':
        ai.run_single_command()
    elif choice == '3':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Running in continuous mode...")
        ai.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
