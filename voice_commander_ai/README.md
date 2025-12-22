# 🤖 Voice Commander AI

A sophisticated voice-controlled AI assistant that listens to voice commands and responds with intelligent actions and voice feedback.

## Features

✨ **Core Features:**
- 🎤 Real-time voice recognition using Google Speech Recognition
- 🔊 Text-to-speech responses with natural voice output
- 🧠 Intelligent command processing and response generation
- ⏰ Time and date information
- 🌐 Web search integration
- 🖥️ Application launcher
- 🧮 Simple calculator
- 📝 Extensible command system

## Prerequisites

- **Python 3.7+**
- **Microphone** connected to your computer
- **Internet connection** (for Google Speech Recognition and web search)
- **PortAudio** (for PyAudio - may need to be installed separately)

## Installation

### Step 1: Clone/Download the project
```bash
cd c:\Users\LENOVO\Desktop\python\voice_commander_ai
```

### Step 2: Install Required Packages

**Using pip:**
```bash
pip install -r requirements.txt
```

**For Windows with PyAudio issues:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Alternative for PyAudio (pre-built wheel):**
```bash
pip install pipwin
pipwin install portaudio
pip install pyaudio
```

### Step 3: Verify Installation

Test that your microphone works:
```python
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
```

## Usage

### Run the Application

```bash
python main.py
```

### Options

1. **Continuous Mode** - Listen for multiple commands in a loop
   - Say "help" to see available commands
   - Say "stop" or "bye" to exit

2. **Single Command Mode** - Process one command and exit
   - Useful for testing and integration

## Available Voice Commands

| Command | Examples | Action |
|---------|----------|--------|
| **Time** | "What time is it?" | Shows current time |
| **Date** | "What is today?" | Shows current date |
| **Open App** | "Open notepad", "Launch chrome" | Opens applications |
| **Search** | "Search for Python tutorials" | Opens Google search |
| **Calculate** | "Calculate 10 + 5" | Performs math |
| **Greet** | "Hello", "Hi" | Responds with greeting |
| **Help** | "Help", "What can you do?" | Shows available commands |
| **Exit** | "Stop", "Bye", "Goodbye" | Closes the application |

## Project Structure

```
voice_commander_ai/
├── main.py              # Main application entry point
├── voice_recognizer.py  # Voice input handling
├── text_to_speech.py    # Text-to-speech output
├── ai_brain.py          # Command processing logic
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Configuration

Edit `config.py` to customize:
- Speech rate (words per minute)
- Volume level
- Timeout durations
- Supported applications
- Custom voice commands

## Troubleshooting

### Issue: "No module named 'speech_recognition'"
**Solution:** Install SpeechRecognition
```bash
pip install SpeechRecognition
```

### Issue: "Pyaudio not found" or "PortAudio not installed"
**Solution:** Install PyAudio properly
```bash
pip install pipwin
pipwin install pyaudio
```

### Issue: Microphone not detected
**Solution:** 
- Check that your microphone is properly connected
- Test microphone in system settings
- Try changing MICROPHONE_INDEX in config.py

### Issue: "Could not understand audio"
**Solution:**
- Speak clearly and closer to microphone
- Reduce background noise
- Increase AMBIENT_NOISE_DURATION in config.py

### Issue: Internet connection required
**Solution:**
- Google Speech Recognition requires internet
- Ensure stable internet connection
- Consider adding offline speech recognition for advanced use

## Advanced Usage

### Custom Commands

Add custom commands by editing `ai_brain.py`:

```python
def process_command(self, text: str) -> Optional[str]:
    if 'custom_command' in text:
        return self.your_custom_handler(text)
```

### Integration with OpenAI GPT

Uncomment and configure OpenAI integration for advanced AI responses:

```python
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": command}]
)
```

### Add Weather Integration

```python
import requests
def get_weather(self, command):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    # Make API call to get weather
```

## Performance Tips

1. **Reduce noise** - Use a microphone in a quiet environment
2. **Adjust timeout** - Lower timeout if you want faster response
3. **Cache results** - Store frequently used data locally
4. **Use offline TTS** - For faster response times without internet

## Security Considerations

- Never store sensitive API keys in code
- Use environment variables for API keys
- Validate and sanitize voice commands before processing
- Be careful with commands that modify system files

## Future Enhancements

- [ ] Offline speech recognition (Vosk)
- [ ] Machine learning-based command classification
- [ ] Multi-language support
- [ ] Advanced natural language processing (NLP)
- [ ] Integration with smart home devices
- [ ] Custom voice profiles and personalization
- [ ] Command history and analytics
- [ ] GUI interface

## Contributing

Feel free to extend this project with:
- New voice commands
- Better AI processing
- Additional integrations
- Performance improvements
- Bug fixes

## License

This project is open source and available for personal and educational use.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Test with the single command mode
4. Check your internet connection

---

**Made with ❤️ | Voice Commander AI v1.0**
