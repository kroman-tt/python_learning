"""
Configuration file for Voice Commander AI
"""

# Microphone settings
MICROPHONE_INDEX = 0  # Default microphone (change if you have multiple)
AMBIENT_NOISE_DURATION = 1  # Seconds to sample for noise adjustment

# Speech Recognition settings
TIMEOUT = 10  # Maximum time to wait for speech
PHRASE_TIME_LIMIT = 15  # Maximum duration of a single phrase

# Text-to-Speech settings
TTS_RATE = 150  # Words per minute
TTS_VOLUME = 0.9  # Volume level (0.0 to 1.0)

# AI Settings
ENABLE_RESPONSE_SPEECH = True
CONTINUOUS_MODE = True

# API Keys (set these in environment variables or .env file)
OPENWEATHER_API_KEY = None  # Get from openweathermap.org
GOOGLE_API_KEY = None  # Optional for enhanced features

# Supported Applications
SUPPORTED_APPS = {
    'notepad': 'notepad',
    'calculator': 'calc',
    'chrome': 'chrome',
    'firefox': 'firefox',
    'vs code': 'code',
    'spotify': 'spotify',
    'word': 'winword',
    'excel': 'excel',
    'powerpoint': 'powerpnt',
}

# Voice Commands Mapping
VOICE_COMMANDS = {
    'time': ['what time', 'current time', 'tell me time'],
    'date': ['what date', 'today', 'what is today'],
    'weather': ['weather', 'temperature', 'forecast'],
    'open': ['open', 'launch', 'start'],
    'search': ['search', 'google', 'find'],
    'calculate': ['calculate', 'what is', 'solve'],
    'hello': ['hello', 'hi', 'hey'],
    'help': ['help', 'commands', 'what can you do'],
}
