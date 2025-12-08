"""
Interactive Agent Chatbot Interface

Run this script to interact with your agent through a chatbot interface.
Press the pulse button to generate an ERC721 contract with your chat history.
"""

import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agent import get_agent, add_to_chat_history, get_chat_history, pulse_button, clear_chat_history

async def interactive_session(api_key: str | None = None, model_id: str = "gpt-4o-mini", provider: str = "openai", core_file_path: str = "core.json", **kwargs):
    """Run an interactive session with the agent.
    
    Args:
        api_key: API key for the provider. If None, uses environment variables.
        model_id: Model ID (default: "gpt-4o-mini" for OpenAI).
        provider: Provider name - "openai", "anthropic", "azure" (default: "openai").
        core_file_path: Path to the JSON file containing agent core specification.
        **kwargs: Additional provider-specific arguments (e.g., azure_endpoint, api_version for Azure).
    """
    print("=" * 70)
    print("🤖 Agent Chatbot Interface")
    print("=" * 70)
    print(f"\nProvider: {provider.upper()}")
    print("Initializing agent...")
    
    # Create agent
    agent = get_agent(api_key=api_key, model_id=model_id, provider=provider, core_file_path=core_file_path, **kwargs)
    
    print("\n" + "=" * 70)
    print("✨ Agent is ready! Start chatting below.")
    print("=" * 70)
    print("\n💡 Commands:")
    print("   - Type your message to chat with the agent")
    print("   - Type 'pulse' to generate ERC721 contract with chat history")
    print("   - Type 'history' to view chat history")
    print("   - Type 'clear' to clear chat history")
    print("   - Type 'quit' or 'exit' to end session")
    print("=" * 70 + "\n")
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n✨ Session ended. Goodbye!")
                break
            
            if user_input.lower() == 'pulse':
                print("\n🔘 Pulse button pressed! Generating ERC721 contract...")
                result = pulse_button()
                print(f"\n{result}\n")
                continue
            
            if user_input.lower() == 'history':
                history = get_chat_history()
                if history:
                    print("\n📜 Chat History:")
                    print("-" * 70)
                    for msg in history:
                        role = msg['role'].upper()
                        content = msg['content'][:200] + "..." if len(msg['content']) > 200 else msg['content']
                        print(f"{role}: {content}")
                    print("-" * 70)
                else:
                    print("\n📜 No chat history yet.\n")
                continue
            
            if user_input.lower() == 'clear':
                clear_chat_history()
                print("\n🗑️ Chat history cleared.\n")
                continue
            
            # Add user message to history
            add_to_chat_history("user", user_input)
            
            # Run agent
            print("\n🤖 Agent: ", end="", flush=True)
            
            # Use streaming for better UX
            assistant_response = ""
            async for chunk in agent.run_stream(user_input):
                if chunk.text:
                    print(chunk.text, end="", flush=True)
                    assistant_response += chunk.text
            
            print("\n")
            
            # Add assistant response to history
            add_to_chat_history("assistant", assistant_response)
            
        except KeyboardInterrupt:
            print("\n\n✨ Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.\n")


if __name__ == "__main__":
    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    model_id = os.environ.get("OPENAI_CHAT_MODEL_ID", "gpt-4o-mini")
    core_file_path = os.environ.get("AGENT_CORE_FILE", "core.json")
    
    if not api_key:
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables.")
        print("   The agent will try to use environment variables or .env file.")
        print("   If you have an API key, set it with:")
        print("   export OPENAI_API_KEY='your-key-here'  (Linux/Mac)")
        print("   $env:OPENAI_API_KEY='your-key-here'    (Windows PowerShell)")
        print()
    
    try:
        asyncio.run(interactive_session(api_key=api_key, model_id=model_id, core_file_path=core_file_path))
    except KeyboardInterrupt:
        print("\n\n✨ Session ended. Goodbye!")

