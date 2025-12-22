"""
AI Brain Module
Processes commands and generates responses using various methods
"""

import os
import datetime
import subprocess
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AIBrain:
    """Core AI logic for processing commands"""
    
    def __init__(self):
        self.user_name = "User"
        self.commands = self._build_command_dictionary()
    
    def _build_command_dictionary(self):
        """Build a dictionary of voice commands"""
        return {
            'time': self.get_time,
            'date': self.get_date,
            'weather': self.get_weather,
            'open': self.open_application,
            'search': self.search_web,
            'calculate': self.simple_calculate,
            'hello': self.greet,
            'help': self.show_help,
            'bye': self.goodbye,
        }
    
    def process_command(self, text: str) -> Optional[str]:
        """
        Process voice command and return response
        
        Args:
            text: Voice command text
            
        Returns:
            Response text or None
        """
        if not text:
            return None
        
        # Check for exact command matches
        for command, handler in self.commands.items():
            if command in text:
                return handler(text)
        
        # If no command found, generate generic response
        return self.generate_response(text)
    
    def get_time(self, command: str) -> str:
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}"
        return response
    
    def get_date(self, command: str) -> str:
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        response = f"Today is {current_date}"
        return response
    
    def get_weather(self, command: str) -> str:
        """Get weather information (basic implementation)"""
        return "Weather feature requires API key. Please configure with OpenWeatherMap API."
    
    def open_application(self, command: str) -> str:
        """Open applications"""
        apps = {
            'notepad': 'notepad',
            'calculator': 'calc',
            'chrome': 'chrome',
            'firefox': 'firefox',
            'vs code': 'code',
            'spotify': 'spotify',
        }
        
        for app, process in apps.items():
            if app in command:
                try:
                    subprocess.Popen(process)
                    return f"Opening {app}"
                except Exception as e:
                    return f"Could not open {app}: {str(e)}"
        
        return "Application not found in database"
    
    def search_web(self, command: str) -> str:
        """Search on the web"""
        search_query = command.replace('search', '').replace('for', '').strip()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            try:
                import webbrowser
                webbrowser.open(url)
                return f"Searching for {search_query}"
            except Exception as e:
                return f"Could not perform search: {str(e)}"
        return "What would you like to search for?"
    
    def simple_calculate(self, command: str) -> str:
        """Simple calculator functionality"""
        try:
            # Extract numbers and operators
            math_expr = command.replace('calculate', '').replace('what is', '').strip()
            result = eval(math_expr)
            return f"The answer is {result}"
        except Exception as e:
            return "Could not calculate that expression"
    
    def greet(self, command: str) -> str:
        """Greet the user"""
        greetings = [
            "Hello! How can I assist you?",
            "Hi there! What can I do for you?",
            "Hey! Ready to help. What do you need?",
        ]
        import random
        return random.choice(greetings)
    
    def show_help(self, command: str) -> str:
        """Show available commands"""
        help_text = """
        Available commands:
        - 'what time is it?' - Get current time
        - 'what is today?' - Get current date
        - 'open [app name]' - Open applications (notepad, calculator, chrome, etc.)
        - 'search for [query]' - Search on Google
        - 'calculate [expression]' - Simple math calculation
        - 'hello' - Get a greeting
        - 'help' - Show this help message
        - 'bye' - Exit the program
        """
        return help_text
    
    def goodbye(self, command: str) -> str:
        """Goodbye message"""
        return "Goodbye! Have a great day!"
    
    def generate_response(self, text: str) -> str:
        """Generate generic response for unknown commands"""
        responses = [
            f"I understood '{text}', but I'm not sure how to respond to that.",
            f"That's interesting, but I don't have a specific action for '{text}'.",
            "I'm still learning. Could you try a different command?",
        ]
        import random
        return random.choice(responses)
