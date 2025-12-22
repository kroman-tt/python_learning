"""
Advanced API Integration Examples
Optional integrations for enhanced functionality
"""

import os
import requests
import logging
from typing import Optional, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ==========================================
# OPENWEATHER API - Weather Integration
# ==========================================

class WeatherIntegration:
    """Get weather information from OpenWeatherMap API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Weather API
        Get API key from: https://openweathermap.org/api
        """
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str) -> str:
        """Get current weather for a city"""
        if not self.api_key:
            return "Weather API key not configured. Get one from openweathermap.org"
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius
            }
            
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                
                weather_text = f"""
                Weather in {city}:
                Temperature: {temp}°C (feels like {feels_like}°C)
                Condition: {description}
                Humidity: {humidity}%
                """
                return weather_text.strip()
            else:
                return f"City '{city}' not found"
        
        except Exception as e:
            logger.error(f"Weather API error: {e}")
            return "Error fetching weather information"


# ==========================================
# NEWS API - Latest News
# ==========================================

class NewsIntegration:
    """Get latest news from NewsAPI"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize News API
        Get API key from: https://newsapi.org
        """
        self.api_key = api_key or os.getenv("NEWSAPI_KEY")
        self.base_url = "https://newsapi.org/v2/top-headlines"
    
    def get_top_headlines(self, country: str = "us", count: int = 3) -> str:
        """Get top news headlines"""
        if not self.api_key:
            return "News API key not configured. Get one from newsapi.org"
        
        try:
            params = {
                'country': country,
                'apiKey': self.api_key,
                'pageSize': count
            }
            
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if data['status'] == 'ok':
                articles = data['articles']
                news = "Latest headlines:\n"
                for i, article in enumerate(articles, 1):
                    news += f"{i}. {article['title']}\n"
                    news += f"   {article['description'][:100]}...\n\n"
                
                return news.strip()
            else:
                return "Could not fetch news"
        
        except Exception as e:
            logger.error(f"News API error: {e}")
            return "Error fetching news"


# ==========================================
# OPENAI GPT - Advanced AI
# ==========================================

class OpenAIIntegration:
    """Advanced AI responses using OpenAI GPT"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize OpenAI Integration
        Get API key from: https://platform.openai.com
        Install: pip install openai
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if self.api_key:
            try:
                import openai
                openai.api_key = self.api_key
                self.openai = openai
                self.available = True
            except ImportError:
                logger.warning("OpenAI library not installed: pip install openai")
                self.available = False
        else:
            self.available = False
            logger.warning("OpenAI API key not configured")
    
    def get_response(self, prompt: str, max_tokens: int = 150) -> str:
        """Get AI response from GPT"""
        if not self.available:
            return "OpenAI integration not available"
        
        try:
            response = self.openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful voice assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7
            )
            
            return response['choices'][0]['message']['content'].strip()
        
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return "Error getting AI response"


# ==========================================
# WIKIPEDIA - Information Lookup
# ==========================================

class WikipediaIntegration:
    """Search and get information from Wikipedia"""
    
    @staticmethod
    def search(query: str, sentences: int = 3) -> str:
        """Search Wikipedia for a topic"""
        try:
            import wikipedia
            
            # Search for the query
            results = wikipedia.search(query, results=1)
            
            if not results:
                return f"No Wikipedia results found for '{query}'"
            
            # Get the full page
            try:
                page = wikipedia.page(results[0])
                content = page.summary.split('.')[:sentences]
                content = '. '.join(content) + '.'
                
                return f"About {results[0]}:\n{content}"
            
            except wikipedia.exceptions.DisambiguationError:
                return f"The term '{query}' is ambiguous. Please be more specific."
            except wikipedia.exceptions.PageError:
                return f"Could not find a Wikipedia page for '{query}'"
        
        except ImportError:
            return "Wikipedia library not installed: pip install wikipedia"
        except Exception as e:
            logger.error(f"Wikipedia error: {e}")
            return "Error searching Wikipedia"


# ==========================================
# GOOGLE MAPS - Location & Directions
# ==========================================

class GoogleMapsIntegration:
    """Get location and direction information"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Google Maps API
        Get API key from: https://cloud.google.com/maps-platform
        """
        self.api_key = api_key or os.getenv("GOOGLE_MAPS_API_KEY")
    
    def get_distance(self, origin: str, destination: str) -> str:
        """Get distance between two locations"""
        if not self.api_key:
            return "Google Maps API key not configured"
        
        try:
            url = "https://maps.googleapis.com/maps/api/distancematrix/json"
            params = {
                'origins': origin,
                'destinations': destination,
                'key': self.api_key
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            if data['status'] == 'OK':
                element = data['rows'][0]['elements'][0]
                if element['status'] == 'OK':
                    distance = element['distance']['text']
                    duration = element['duration']['text']
                    return f"Distance from {origin} to {destination}: {distance} ({duration})"
            
            return "Could not calculate distance"
        
        except Exception as e:
            logger.error(f"Google Maps error: {e}")
            return "Error calculating distance"


# ==========================================
# STOCK MARKET - Stock Information
# ==========================================

class StockIntegration:
    """Get stock market information"""
    
    @staticmethod
    def get_stock_price(symbol: str) -> str:
        """Get current stock price"""
        try:
            import yfinance as yf
            
            stock = yf.Ticker(symbol)
            data = stock.history(period='1d')
            
            if data.empty:
                return f"Stock symbol '{symbol}' not found"
            
            price = data['Close'].iloc[-1]
            open_price = data['Open'].iloc[-1]
            change = price - open_price
            change_percent = (change / open_price * 100)
            
            return f"""
            {symbol} Stock Price:
            Current: ${price:.2f}
            Change: ${change:+.2f} ({change_percent:+.1f}%)
            """
        
        except ImportError:
            return "yfinance library not installed: pip install yfinance"
        except Exception as e:
            logger.error(f"Stock API error: {e}")
            return f"Error getting stock price for {symbol}"


# ==========================================
# INTEGRATION SETUP
# ==========================================

class IntegratedVoiceAI:
    """Voice AI with all integrations"""
    
    def __init__(self):
        """Initialize all integrations"""
        self.weather = WeatherIntegration()
        self.news = NewsIntegration()
        self.openai = OpenAIIntegration()
        self.wikipedia = WikipediaIntegration()
        self.maps = GoogleMapsIntegration()
        self.stock = StockIntegration()
    
    def handle_command(self, command: str) -> str:
        """Route command to appropriate integration"""
        
        if 'weather' in command:
            city = command.replace('weather', '').replace('in', '').strip()
            return self.weather.get_weather(city) if city else "Which city?"
        
        elif 'news' in command:
            return self.news.get_top_headlines()
        
        elif 'wikipedia' in command or 'search' in command:
            query = command.replace('wikipedia', '').replace('search', '').strip()
            return self.wikipedia.search(query) if query else "What do you want to search?"
        
        elif 'stock' in command or 'price' in command:
            symbol = command.replace('stock', '').replace('price', '').strip().upper()
            return self.stock.get_stock_price(symbol) if symbol else "Which stock?"
        
        elif 'distance' in command:
            # Parse "distance from A to B"
            parts = command.split('to')
            if len(parts) == 2:
                origin = parts[0].replace('distance from', '').strip()
                destination = parts[1].strip()
                return self.maps.get_distance(origin, destination)
            return "Please say: distance from [place] to [place]"
        
        return None


# ==========================================
# SETUP INSTRUCTIONS
# ==========================================

SETUP_INSTRUCTIONS = """
🔧 API INTEGRATION SETUP GUIDE

1. OPENWEATHER (Weather)
   - Visit: https://openweathermap.org/api
   - Sign up for free account
   - Get API key
   - Set environment: OPENWEATHER_API_KEY=your_key
   - Install: pip install requests

2. NEWSAPI (Headlines)
   - Visit: https://newsapi.org
   - Sign up for free account
   - Get API key
   - Set environment: NEWSAPI_KEY=your_key

3. OPENAI (Advanced AI)
   - Visit: https://platform.openai.com
   - Create account and add payment
   - Get API key
   - Set environment: OPENAI_API_KEY=your_key
   - Install: pip install openai

4. WIKIPEDIA (Information)
   - No API key needed
   - Install: pip install wikipedia

5. GOOGLE MAPS (Directions)
   - Visit: https://cloud.google.com/maps-platform
   - Enable Maps API
   - Get API key
   - Set environment: GOOGLE_MAPS_API_KEY=your_key

6. YFINANCE (Stock Prices)
   - No API key needed
   - Install: pip install yfinance

SET ENVIRONMENT VARIABLES:
Windows PowerShell:
  $env:OPENWEATHER_API_KEY = "your_key"
  $env:OPENAI_API_KEY = "your_key"

Windows Command Prompt:
  set OPENWEATHER_API_KEY=your_key
  set OPENAI_API_KEY=your_key

Linux/Mac:
  export OPENWEATHER_API_KEY=your_key
  export OPENAI_API_KEY=your_key
"""


if __name__ == "__main__":
    print(SETUP_INSTRUCTIONS)
    
    # Example usage
    print("\n" + "="*60)
    print("TESTING INTEGRATIONS")
    print("="*60)
    
    # Test weather (requires API key)
    weather = WeatherIntegration()
    print("\n1. Weather Test:")
    print(weather.get_weather("London"))
    
    # Test Wikipedia (free)
    wiki = WikipediaIntegration()
    print("\n2. Wikipedia Test:")
    print(wiki.search("Python programming"))
    
    # Test integrated AI
    print("\n3. Integrated AI:")
    ai = IntegratedVoiceAI()
    print(ai.handle_command("weather in Paris"))
