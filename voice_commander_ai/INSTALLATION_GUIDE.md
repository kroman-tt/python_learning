"""
DETAILED INSTALLATION & SETUP GUIDE
Complete step-by-step instructions for Voice Commander AI
"""

# ============================================================
# VOICE COMMANDER AI - COMPLETE INSTALLATION GUIDE
# ============================================================

INSTALLATION_STEPS = """

╔════════════════════════════════════════════════════════════════╗
║        VOICE COMMANDER AI - INSTALLATION GUIDE                ║
║              (Windows/Mac/Linux Compatible)                   ║
╚════════════════════════════════════════════════════════════════╝

⏱️  ESTIMATED TIME: 10-15 minutes


STEP 1: CHECK PYTHON INSTALLATION
══════════════════════════════════════════════════════════════════

Windows (PowerShell):
  python --version
  python -m pip --version

Mac/Linux:
  python3 --version
  pip3 --version

✅ Required: Python 3.7 or higher
✅ Recommended: Python 3.9+

If Python not installed:
  Download from: https://www.python.org/downloads/
  Make sure to check "Add Python to PATH" during installation


STEP 2: NAVIGATE TO PROJECT FOLDER
══════════════════════════════════════════════════════════════════

Windows (PowerShell):
  cd "c:\Users\LENOVO\Desktop\python\voice_commander_ai"

Mac/Linux:
  cd ~/Desktop/python/voice_commander_ai


STEP 3: CREATE VIRTUAL ENVIRONMENT (OPTIONAL BUT RECOMMENDED)
══════════════════════════════════════════════════════════════════

Windows:
  python -m venv venv
  venv\Scripts\activate
  
Mac/Linux:
  python3 -m venv venv
  source venv/bin/activate

✅ Benefits: Isolates dependencies, prevents conflicts


STEP 4: INSTALL DEPENDENCIES
══════════════════════════════════════════════════════════════════

OPTION A: AUTOMATED SETUP (EASIEST)
────────────────────────────────────
  python setup.py

OPTION B: MANUAL SETUP
────────────────────────────────────

1. Install all packages:
   pip install -r requirements.txt

2. Install PyAudio (system audio library):

   WINDOWS:
   ─────────
   pip install pipwin
   pipwin install pyaudio
   
   (If that fails, try: pip install pyaudio)

   MAC:
   ─────────
   brew install portaudio
   pip install pyaudio

   LINUX:
   ─────────
   sudo apt-get install portaudio19-dev python3-dev
   pip install pyaudio


STEP 5: VERIFY INSTALLATION
══════════════════════════════════════════════════════════════════

Test all components:
  python test_components.py

You should see:
  ✅ AI Brain - OK
  ✅ Text-to-Speech - OK (will speak a test message)
  ✅ Speech Recognition - OK (will ask you to speak)


STEP 6: TROUBLESHOOTING COMMON ISSUES
══════════════════════════════════════════════════════════════════

ISSUE: "SpeechRecognition not found"
SOLUTION:
  pip install SpeechRecognition

ISSUE: "pyttsx3 not found"
SOLUTION:
  pip install pyttsx3

ISSUE: "pyaudio installation fails"
SOLUTION:
  Windows:
    pip install pipwin
    pipwin install pyaudio
  
  Mac:
    brew install portaudio
    pip install pyaudio
  
  Linux:
    sudo apt-get install portaudio19-dev
    pip install pyaudio

ISSUE: "Microphone not detected"
SOLUTION:
  1. Check system sound settings
  2. Test microphone in Windows Settings
  3. Reconnect microphone
  4. Try MICROPHONE_INDEX=1 in config.py

ISSUE: "No module named main.py"
SOLUTION:
  Make sure you're in the voice_commander_ai directory
  cd voice_commander_ai
  python main.py


STEP 7: RUN APPLICATION
══════════════════════════════════════════════════════════════════

OPTION A: Standard Python
─────────────────────────
  python main.py

OPTION B: Windows Batch Script
─────────────────────────────
  run.bat
  (Double-click the file)

OPTION C: Interactive Menu
─────────────────────────────
  python main.py
  Select option 1 (continuous mode)


STEP 8: FIRST TIME USAGE
══════════════════════════════════════════════════════════════════

When you run main.py:

1. Choose mode:
   Option 1: Continuous listening (recommended)
   Option 2: Single command
   Option 3: Exit

2. The AI will say: "Listening..."

3. Speak clearly into your microphone

4. Wait for the AI to process and respond

5. Try these commands:
   - "What time is it?"
   - "What is today?"
   - "Say hello"
   - "Help"


STEP 9: CONFIGURE SETTINGS (OPTIONAL)
══════════════════════════════════════════════════════════════════

Edit config.py to customize:

TTS_RATE = 150         # Speech speed (words per minute)
TTS_VOLUME = 0.9       # Volume level (0.0 to 1.0)
TIMEOUT = 10           # Listening timeout (seconds)
PHRASE_TIME_LIMIT = 15 # Max phrase length (seconds)

Example:
  TTS_RATE = 120         # Slower speech
  TTS_VOLUME = 0.5       # Quieter volume
  TIMEOUT = 20           # More time to speak


STEP 10: ADD CUSTOM COMMANDS
══════════════════════════════════════════════════════════════════

Edit ai_brain.py:

1. Add new function:
   def my_command(self, command: str) -> str:
       return "Your response here"

2. Add to dictionary:
   'my_keyword': self.my_command,

Example:
   def tell_joke(self, command: str) -> str:
       return "Why did the programmer quit? He got arrays!"
   
   'joke': self.tell_joke,

Then say: "Tell me a joke"


STEP 11: ADVANCED FEATURES
══════════════════════════════════════════════════════════════════

API Integrations (optional):
  See api_integrations.py for:
  - Weather (OpenWeatherMap API)
  - News (NewsAPI)
  - Stocks (YFinance)
  - Maps (Google Maps API)
  - Wikipedia

Example Extensions (see examples_and_extensions.py):
  - Custom commands
  - Analytics logging
  - Multilingual support
  - Intent detection
  - OpenAI GPT integration


STEP 12: TROUBLESHOOTING RUNTIME ERRORS
══════════════════════════════════════════════════════════════════

ERROR: "Could not understand audio"
  → Speak more clearly
  → Get closer to microphone
  → Reduce background noise

ERROR: "Error accessing Google Speech Recognition"
  → Check internet connection
  → Check microphone input level
  → Try again in a few seconds

ERROR: "Timeout waiting for speech"
  → The app is waiting but didn't hear anything
  → Start speaking before timeout occurs
  → Check TIMEOUT setting in config.py

ERROR: No sound output
  → Check volume levels
  → Test speakers in system settings
  → Check TTS_VOLUME in config.py


═══════════════════════════════════════════════════════════════════

✅ QUICK REFERENCE

Installation:          python setup.py
Test:                  python test_components.py
Run:                   python main.py
Windows launcher:      run.bat
Configuration:         config.py
Custom commands:       ai_brain.py
API integration:       api_integrations.py
Examples:              examples_and_extensions.py


═══════════════════════════════════════════════════════════════════

🎙️  YOU'RE READY!

Start with: python main.py
Speak your first command!


For help:
  - Check README.md for full documentation
  - Check QUICKSTART.md for quick reference
  - Check examples_and_extensions.py for advanced usage

═══════════════════════════════════════════════════════════════════
"""

WINDOWS_BATCH_SETUP = """
📝 Alternative: Run from Windows Batch Script

The run.bat file is included for easy launching:

1. Double-click run.bat
2. Choose from menu:
   1 = Run main application
   2 = Run tests
   3 = Run setup
   4 = Exit

This will:
  ✅ Create virtual environment automatically
  ✅ Install dependencies if needed
  ✅ Run your chosen option
"""

COMMON_ISSUES = """
╔════════════════════════════════════════════════════════════════╗
║              COMMON INSTALLATION ISSUES                        ║
╚════════════════════════════════════════════════════════════════╝

ISSUE #1: "No module named 'speech_recognition'"
────────────────────────────────────────────────
Solution:
  pip install SpeechRecognition
  pip install PyAudio
  pip install pyttsx3

ISSUE #2: "Pyaudio wheels not available"
────────────────────────────────────────────────
Solution (Windows):
  pip install pipwin
  pipwin install pyaudio

Solution (Mac):
  brew install portaudio
  pip install pyaudio

Solution (Linux):
  sudo apt-get install portaudio19-dev
  pip install pyaudio

ISSUE #3: "Microphone not found"
────────────────────────────────────────────────
Solution:
  1. Check Windows Settings → Sound → Input devices
  2. Set microphone as default
  3. Test microphone in Settings
  4. Restart the application

ISSUE #4: "Could not connect to Google API"
────────────────────────────────────────────────
Solution:
  1. Check your internet connection
  2. Ensure Google Speech API is accessible
  3. Try using a VPN if in restricted region
  4. Check firewall settings

ISSUE #5: "Text-to-speech not working"
────────────────────────────────────────────────
Solution:
  1. Check Windows Settings → Sound → Output devices
  2. Test speakers with a video
  3. Restart application
  4. Adjust TTS_VOLUME in config.py

ISSUE #6: "Python not recognized"
────────────────────────────────────────────────
Solution:
  1. Reinstall Python
  2. IMPORTANT: Check "Add Python to PATH"
  3. Restart computer
  4. Try: python --version

ISSUE #7: "Permission denied"
────────────────────────────────────────────────
Solution:
  1. Run Command Prompt as Administrator
  2. Try: pip install --user package_name
  3. Check folder permissions

═══════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(INSTALLATION_STEPS)
    print("\n" + "="*70)
    print(WINDOWS_BATCH_SETUP)
    print("\n" + "="*70)
    print(COMMON_ISSUES)
