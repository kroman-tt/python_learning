"""
Advanced AI Brain with OpenAI Integration
For more intelligent and context-aware responses
"""

import os
import logging
from typing import Optional
from ai_brain import AIBrain

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AdvancedAIBrain(AIBrain):
    """Extended AI Brain with OpenAI and advanced features"""
    
    def __init__(self, use_openai=False):
        super().__init__()
        self.use_openai = use_openai and self._check_openai_api()
        self.conversation_history = []
        
        if self.use_openai:
            try:
                import openai
                self.openai = openai
                self.openai.api_key = os.getenv("OPENAI_API_KEY")
                logger.info("OpenAI integration enabled")
            except ImportError:
                logger.warning("OpenAI not installed. Install with: pip install openai")
                self.use_openai = False
    
    def _check_openai_api(self) -> bool:
        """Check if OpenAI API key is configured"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.warning("OPENAI_API_KEY not set in environment variables")
            return False
        return True
    
    def generate_response(self, text: str) -> str:
        """
        Generate intelligent response using OpenAI or fallback methods
        
        Args:
            text: User input text
            
        Returns:
            Generated response
        """
        if self.use_openai:
            return self._generate_openai_response(text)
        else:
            return super().generate_response(text)
    
    def _generate_openai_response(self, text: str) -> str:
        """Generate response using OpenAI GPT"""
        try:
            # Add to conversation history
            self.conversation_history.append({
                "role": "user",
                "content": text
            })
            
            # Keep only last 10 messages for context
            messages = self.conversation_history[-10:]
            
            # Call OpenAI API
            response = self.openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=150
            )
            
            assistant_message = response['choices'][0]['message']['content']
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message.strip()
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return "I encountered an issue processing that. Please try again."
    
    def add_custom_command(self, keyword: str, handler):
        """
        Dynamically add custom commands
        
        Args:
            keyword: Command keyword to match
            handler: Function to handle the command
        """
        self.commands[keyword] = handler
        logger.info(f"Custom command '{keyword}' added")
    
    def process_command_with_context(self, text: str, context: dict) -> Optional[str]:
        """
        Process command with additional context information
        
        Args:
            text: Voice command
            context: Additional context (location, user profile, etc.)
            
        Returns:
            Response text
        """
        # Add context to command processing
        enhanced_text = f"{text} (context: {context})"
        return self.process_command(enhanced_text)
    
    def get_command_confidence(self, text: str, command: str) -> float:
        """
        Calculate confidence score for command match
        
        Args:
            text: User input
            command: Command keyword
            
        Returns:
            Confidence score (0.0 to 1.0)
        """
        # Simple similarity calculation
        matches = sum(1 for word in command.split() if word in text)
        total_words = len(command.split())
        return matches / total_words if total_words > 0 else 0.0


# Example usage
if __name__ == "__main__":
    # Initialize advanced AI brain
    ai = AdvancedAIBrain(use_openai=True)
    
    # Test commands
    test_commands = [
        "what is the weather today",
        "tell me a joke",
        "what is machine learning",
        "open spotify",
    ]
    
    print("Testing Advanced AI Brain...")
    print("=" * 50)
    
    for cmd in test_commands:
        response = ai.process_command(cmd)
        print(f"Command: {cmd}")
        print(f"Response: {response}\n")
