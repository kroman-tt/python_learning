# 🚀 Quick Start Guide - Voice Commander AI

## Installation (5 minutes)

### Option 1: Automated Setup
```bash
cd voice_commander_ai
python setup.py
```

### Option 2: Manual Setup
```bash
# Navigate to project directory
cd voice_commander_ai

# Install dependencies
pip install -r requirements.txt

# Install PyAudio (Windows)
pip install pipwin
pipwin install pyaudio

# Verify installation
python test_components.py
```

## Run the Application

### First Time
```bash
# Run tests to verify everything works
python test_components.py

# Then run main application
python main.py
```

### After First Run
```bash
# Just run the main app
python main.py
```

## Quick Commands to Try

Say these voice commands after starting the app:

- "What time is it?" → Tells current time
- "What is today?" → Shows today's date  
- "Open notepad" → Launches Notepad
- "Search for Python" → Opens Google search
- "Calculate 2 + 2" → Solves math
- "Hello" → Gets a greeting
- "Help" → Shows all commands
- "Bye" → Exits the program

## Troubleshooting

### Microphone not working?
1. Check that microphone is connected
2. Test in Windows Settings → Sound → Input
3. Edit `config.py` and try different MICROPHONE_INDEX values

### "Could not understand audio"
1. Speak clearly and closer to microphone
2. Reduce background noise
3. Increase AMBIENT_NOISE_DURATION in `config.py`

### PyAudio installation fails?
```bash
# Try this on Windows
pip install pipwin
pipwin install pyaudio

# Or use conda
conda install pyaudio
```

### Need more help?
Check `README.md` in the project directory

## File Structure

```
voice_commander_ai/
├── main.py              ← Run this to start
├── test_components.py   ← Run this first to verify setup
├── setup.py             ← Run this for automatic setup
├── ai_brain.py          ← AI logic
├── voice_recognizer.py  ← Listen to commands
├── text_to_speech.py    ← Speak responses
├── config.py            ← Settings
└── README.md            ← Full documentation
```

## Next Steps

1. ✅ Install dependencies
2. ✅ Run tests
3. ✅ Start main application
4. 🎤 Speak commands
5. 🔧 Customize commands (edit `ai_brain.py`)
6. 🚀 Add advanced features

---

**Happy voice commanding! 🎙️**
