"""
Test script for Voice Commander AI
Tests individual components before running the full application
"""

import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_speech_recognition():
    """Test speech recognition module"""
    print("\n" + "="*50)
    print("Testing Speech Recognition...")
    print("="*50)
    
    try:
        import speech_recognition as sr
        print("✅ SpeechRecognition library loaded")
        
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        print("✅ Microphone initialized")
        print("\nTesting microphone... (Please speak now)")
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            
        try:
            text = recognizer.recognize_google(audio)
            print(f"✅ Recognition successful: '{text}'")
            return True
        except sr.UnknownValueError:
            print("⚠️  Could not understand audio. Try speaking clearly.")
            return False
        except sr.RequestError as e:
            print(f"❌ Error with Google API: {e}")
            return False
            
    except ImportError:
        print("❌ SpeechRecognition not installed: pip install SpeechRecognition")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_text_to_speech():
    """Test text-to-speech module"""
    print("\n" + "="*50)
    print("Testing Text-to-Speech...")
    print("="*50)
    
    try:
        import pyttsx3
        print("✅ pyttsx3 library loaded")
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        
        print("🔊 Speaking test message...")
        engine.say("Hello! Voice Commander AI is working correctly.")
        engine.runAndWait()
        
        print("✅ Text-to-speech successful")
        return True
        
    except ImportError:
        print("❌ pyttsx3 not installed: pip install pyttsx3")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_ai_brain():
    """Test AI brain processing"""
    print("\n" + "="*50)
    print("Testing AI Brain...")
    print("="*50)
    
    try:
        from ai_brain import AIBrain
        print("✅ AI Brain module loaded")
        
        brain = AIBrain()
        
        # Test various commands
        test_commands = [
            "what time is it",
            "what is today",
            "say hello",
            "help",
        ]
        
        for cmd in test_commands:
            response = brain.process_command(cmd)
            print(f"  Command: '{cmd}'")
            print(f"  Response: '{response}'")
        
        print("✅ AI Brain tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_all_components():
    """Test all components"""
    print("\n" + "="*80)
    print("🤖 VOICE COMMANDER AI - COMPONENT TEST SUITE")
    print("="*80)
    
    results = {
        'AI Brain': test_ai_brain(),
        'Text-to-Speech': test_text_to_speech(),
        'Speech Recognition': test_speech_recognition(),
    }
    
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    for component, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{component}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*80)
    if all_passed:
        print("✅ All tests passed! You can now run: python main.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
    print("="*80 + "\n")
    
    return all_passed


if __name__ == "__main__":
    success = test_all_components()
    sys.exit(0 if success else 1)
