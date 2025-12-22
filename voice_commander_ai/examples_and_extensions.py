"""
Examples and Extensions for Voice Commander AI
Shows how to extend and customize the application
"""

from ai_brain import AIBrain
from text_to_speech import TextToSpeech
from voice_recognizer import VoiceRecognizer


# ==========================================
# EXAMPLE 1: Custom Commands
# ==========================================

def create_custom_ai():
    """Create AI with custom commands"""
    
    brain = AIBrain()
    
    # Add custom command handler
    def tell_joke(command):
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        ]
        import random
        return random.choice(jokes)
    
    # Add the custom command
    brain.commands['joke'] = tell_joke
    
    return brain


# ==========================================
# EXAMPLE 2: Context-Aware Commands
# ==========================================

def process_with_context(brain, command, user_info):
    """Process command with user context"""
    
    context = {
        'name': user_info.get('name', 'User'),
        'location': user_info.get('location', 'Unknown'),
        'time': __import__('datetime').datetime.now().strftime("%H:%M"),
    }
    
    response = brain.process_command(command)
    
    # Personalize response with user info
    response = response.replace('User', user_info.get('name', 'User'))
    
    return response


# ==========================================
# EXAMPLE 3: Multiple Language Support
# ==========================================

class MultilingualAI:
    """AI that supports multiple languages"""
    
    def __init__(self):
        self.brain = AIBrain()
        self.speaker = TextToSpeech()
        self.language = 'en'  # Default: English
        
        # Language mappings
        self.languages = {
            'en': {'hello': 'Hello!', 'goodbye': 'Goodbye!'},
            'es': {'hello': '¡Hola!', 'goodbye': '¡Adiós!'},
            'fr': {'hello': 'Bonjour!', 'goodbye': 'Au revoir!'},
        }
    
    def set_language(self, lang_code):
        """Set the language"""
        if lang_code in self.languages:
            self.language = lang_code
            print(f"Language set to {lang_code}")
    
    def process(self, command):
        """Process command in current language"""
        response = self.brain.process_command(command)
        return response


# ==========================================
# EXAMPLE 4: Command Logging and Analytics
# ==========================================

class AnalyticsAI:
    """AI with command logging and analytics"""
    
    def __init__(self):
        self.brain = AIBrain()
        self.command_history = []
    
    def process_and_log(self, command):
        """Process command and log it"""
        
        response = self.brain.process_command(command)
        
        # Log the interaction
        import datetime
        self.command_history.append({
            'timestamp': datetime.datetime.now(),
            'command': command,
            'response': response,
        })
        
        return response
    
    def get_statistics(self):
        """Get command statistics"""
        if not self.command_history:
            return "No commands logged yet"
        
        total_commands = len(self.command_history)
        unique_commands = len(set(cmd['command'] for cmd in self.command_history))
        
        stats = f"""
        Command Statistics:
        - Total commands: {total_commands}
        - Unique commands: {unique_commands}
        - Average per command: {total_commands / unique_commands:.1f}
        """
        
        return stats
    
    def save_history(self, filename):
        """Save command history to file"""
        with open(filename, 'w') as f:
            for entry in self.command_history:
                f.write(f"{entry['timestamp']} | {entry['command']} | {entry['response']}\n")
        print(f"History saved to {filename}")


# ==========================================
# EXAMPLE 5: Advanced Voice Processing
# ==========================================

class AdvancedVoiceAI:
    """Advanced voice AI with sentiment analysis and intent detection"""
    
    def __init__(self):
        self.brain = AIBrain()
        self.recognizer = VoiceRecognizer()
        self.speaker = TextToSpeech()
    
    def detect_intent(self, text):
        """Detect user intent from text"""
        
        intents = {
            'greeting': ['hello', 'hi', 'hey'],
            'question': ['what', 'how', 'why', 'when'],
            'command': ['open', 'close', 'start', 'stop'],
            'information': ['tell', 'show', 'display'],
        }
        
        for intent, keywords in intents.items():
            if any(keyword in text for keyword in keywords):
                return intent
        
        return 'unknown'
    
    def estimate_confidence(self, text):
        """Estimate confidence in recognition (0-1)"""
        
        # Factors that increase confidence
        factors = {
            'length': min(len(text.split()) / 10, 1.0),  # Longer = more confident
            'clarity': 0.8,  # Placeholder
        }
        
        confidence = sum(factors.values()) / len(factors)
        return min(confidence, 1.0)
    
    def process_with_analysis(self, text):
        """Process text with intent and confidence analysis"""
        
        intent = self.detect_intent(text)
        confidence = self.estimate_confidence(text)
        
        response = self.brain.process_command(text)
        
        return {
            'command': text,
            'intent': intent,
            'confidence': confidence,
            'response': response,
        }


# ==========================================
# EXAMPLE 6: Integration with External Services
# ==========================================

def get_weather_data(city):
    """Get weather from OpenWeatherMap API"""
    import requests
    
    try:
        api_key = "YOUR_API_KEY_HERE"  # Get from openweathermap.org
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        response = requests.get(url)
        data = response.json()
        
        if data.get('cod') == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"The weather in {city} is {description} with temperature {temp}K"
        else:
            return "Weather data not available"
    except Exception as e:
        return f"Error fetching weather: {e}"


def get_news():
    """Get latest news"""
    import requests
    
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {'country': 'us', 'apiKey': 'YOUR_API_KEY_HERE'}
        
        response = requests.get(url, params=params)
        articles = response.json().get('articles', [])
        
        if articles:
            headlines = [article['title'] for article in articles[:3]]
            return "Latest news: " + ". ".join(headlines)
        else:
            return "No news available"
    except Exception as e:
        return f"Error fetching news: {e}"


# ==========================================
# TESTING EXAMPLES
# ==========================================

if __name__ == "__main__":
    print("="*60)
    print("VOICE COMMANDER AI - EXAMPLES")
    print("="*60)
    
    # Example 1: Custom Commands
    print("\n📌 Example 1: Custom Commands")
    ai_custom = create_custom_ai()
    joke = ai_custom.process_command("tell me a joke")
    print(f"Response: {joke}")
    
    # Example 2: Analytics
    print("\n📌 Example 2: Command Analytics")
    ai_analytics = AnalyticsAI()
    ai_analytics.process_and_log("what time is it")
    ai_analytics.process_and_log("what is today")
    ai_analytics.process_and_log("what time is it")
    print(ai_analytics.get_statistics())
    
    # Example 3: Advanced Voice AI
    print("\n📌 Example 3: Intent Detection")
    ai_advanced = AdvancedVoiceAI()
    result = ai_advanced.process_with_analysis("what is the weather")
    print(f"Intent: {result['intent']}")
    print(f"Confidence: {result['confidence']:.1%}")
    print(f"Response: {result['response']}")
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)
