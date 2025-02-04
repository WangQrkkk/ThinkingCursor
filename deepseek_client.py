import requests
import argparse
import sys

class DeepSeekClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Define system prompt separately
        self.system_prompt = """You are a specialized Prompt Optimization Expert who helps enhance communication between users and Claude for programming tasks.

Before responding, carefully analyze:
1. Technical Requirements
   - Core functionality and features needed
   - Potential edge cases and error scenarios 
   - Performance and security considerations
   - Best practices and design patterns

2. User Context
   - User's technical background and skill level
   - Implicit requirements and assumptions
   - Potential misunderstandings to address
   - Required level of guidance and detail

3. Implementation Details
   - Key components and their interactions
   - Critical algorithms and data structures
   - Important configuration options
   - Testing and validation needs

After thorough analysis, ONLY return an optimized prompt that:
- Clearly specifies all technical requirements
- Provides necessary context and constraints
- Highlights important considerations
- Guides toward best practices
- Uses precise technical language

Do NOT include:
- Code snippets or implementation
- Analysis or explanations
- Additional commentary
- Anything other than the optimized prompt itself

If you receive a code request, rewrite it as a detailed prompt that will help Claude provide the optimal implementation."""

    def chat(self, message, **kwargs):
        try:
            # Structure messages properly with system prompt
            data = {
                "model": "deepseek-reasoner",
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": message}
                ],
                **kwargs
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers, 
                json=data
            )
            response.raise_for_status()
            
            response_json = response.json()
            content = response_json['choices'][0]['message']['content']
            
            # Validate response doesn't contain code blocks
            if "```" in content:
                # Strip out code blocks or raise error
                raise ValueError("Response contains code blocks")
                
            return content
            
        except requests.exceptions.RequestException as e:
            print(f"Error making API call: {e}")
            raise
        except (KeyError, IndexError) as e:
            print(f"Error parsing response: {e}")
            raise

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Generate optimized prompts using DeepSeek API'
    )
    parser.add_argument(
        'prompt', 
        help='The prompt/description to optimize'
    )

    args = parser.parse_args()

    try:
        # Initialize client and get response
        client = DeepSeekClient("sk-0df4fe95e7a442788750d86789baf0b1")      
        # Get response from DeepSeek API
        response = client.chat(args.prompt)
        print("Generated response:")
        print(response)
        # Create or append to cursorrules file
        with open("1.cursorrules", "w", encoding="utf-8") as f:
            f.write(response + "\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 