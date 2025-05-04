#!/usr/bin/env python3
import os
import requests
from typing import List, Dict
import textwrap
from colorama import Fore, Style, init

init()

class ChemistGeminiChat:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY environment variable or provide via --api-key")
        
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        self.conversation_history = []
        self.set_chemist_context()
        
    def set_chemist_context(self):
        """Set the initial context to establish the AI as a chemistry expert focused on retrosynthesis."""
        system_prompt = """You are an expert synthetic organic chemist with extensive experience in retrosynthesis planning. 
        Your expertise includes:
        - Analyzing complex molecules to identify disconnection points
        - Suggesting multiple viable synthetic routes
        - Identifying appropriate reagents and reaction conditions
        - Understanding protecting group strategies
        - Evaluating reaction feasibility and efficiency
        - Considering practical lab implementation of synthesis routes
        
        For each retrosynthesis query:
        1. Analyze the target molecule structure
        2. Identify key functional groups and potential disconnection points
        3. Propose multiple retrosynthetic pathways in order of practicality
        4. For each step, suggest specific reagents and conditions
        5. Consider potential side reactions and how to avoid them
        6. Evaluate overall synthetic efficiency and suggest the most promising route
        
        When uncertain about specific transformations, acknowledge limitations and suggest alternative approaches.
        Always reason systematically through each step of the retrosynthesis analysis."""
        
        self.conversation_history.append({
            "role": "model",
            "parts": [{"text": "I'm now an expert synthetic organic chemist focusing on retrosynthesis. Please provide the target molecule or describe what you'd like to synthesize, and I'll help develop potential synthetic routes."}]
        })
        
        self.conversation_history.append({
            "role": "user", 
            "parts": [{"text": system_prompt}]
        })
        
    def add_message(self, role, content):
        """Add a message to the conversation history."""
        self.conversation_history.append({
            "role": role,
            "parts": [{"text": content}]
        })
    
    def send_message(self, user_input):
        """Send a message to the Gemini API and get a response."""
        self.add_message("user", user_input)
        
        url = f"{self.api_url}?key={self.api_key}"
        
        payload = {
            "contents": self.conversation_history
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            
            data = response.json()
            
            if "candidates" in data and data["candidates"]:
                content = data["candidates"][0].get("content", {})
                ai_response = content.get("parts", [{}])[0].get("text", "")
                self.add_message("model", ai_response)
                return ai_response
            
            return "Error: Unable to parse API response"
            
        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed: {str(e)}"
            if hasattr(e, 'response') and e.response:
                error_msg += f"\nStatus code: {e.response.status_code}"
            return error_msg

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Gemini Chemist for Retrosynthesis')
    parser.add_argument('--api-key', help='Gemini API key')
    args = parser.parse_args()
    
    try:
        chat = ChemistGeminiChat(api_key=args.api_key)
        
        print(f"{Fore.GREEN}Welcome to Gemini Retrosynthesis Assistant!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}I'm an expert synthetic chemist who can help design retrosynthetic pathways.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Describe your target molecule or provide a SMILES string, and I'll suggest synthesis routes.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Type 'exit' or 'quit' to end the conversation.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Type '/clear' to start a new conversation while preserving the chemist context.{Style.RESET_ALL}")
        
        while True:
            try:
                user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}")
                
                if user_input.lower() in ['exit', 'quit']:
                    break
                elif user_input.lower() == '/clear':
                    chat.conversation_history = []
                    chat.set_chemist_context()
                    print(f"{Fore.YELLOW}Conversation cleared. Chemist context maintained.{Style.RESET_ALL}")
                    continue
                
                print(f"{Fore.CYAN}Chemist: {Style.RESET_ALL}", end="")
                
                response = chat.send_message(user_input)
                width = os.get_terminal_size().columns
                for line in response.split('\n'):
                    wrapped_lines = textwrap.wrap(line, width=width) if line.strip() else ['']
                    for wrapped in wrapped_lines:
                        print(f"{Fore.CYAN}{wrapped}{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
