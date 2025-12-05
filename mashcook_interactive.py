"""
Interactive MASHCOOK PERSIAN GASTRONOME v5.2

Run this script to interact with your Persian culinary intelligence agent.
"""

import asyncio
from mashcook_agent import get_mashcook_agent, spice_sync_pulse

async def interactive_session(api_key: str | None = None, model_id: str = "gpt-4o-mini"):
    """Run an interactive session with the MASHCOOK agent.
    
    Args:
        api_key: OpenAI API key. If None, uses OPENAI_API_KEY environment variable.
        model_id: OpenAI model ID (default: "gpt-4o-mini").
    """
    print("=" * 70)
    print("🧡 MASHCOOK PERSIAN GASTRONOME v5.2 - Interactive Session 🧡")
    print("=" * 70)
    print("\nInitializing culinary intelligence...")
    
    # Create agent with API key and model
    agent = get_mashcook_agent(api_key=api_key, model_id=model_id)
    
    # Initial pulse
    print("\n📡 Initializing spice synchronization pulse...")
    print(spice_sync_pulse())
    
    print("\n" + "=" * 70)
    print("✨ MASHCOOK is ready! Your 3,000-year culinary memory is active.")
    print("=" * 70)
    print("\n💡 Example queries:")
    print("   - 'Tell me about traditional Ghormeh Sabzi'")
    print("   - 'Create a Nowruz festival menu'")
    print("   - 'Generate an image prompt for Tahdig'")
    print("   - 'Show me regional variations of Saffron rice'")
    print("   - 'Reconstruct a historical recipe for Khoresht Gheymeh'")
    print("\n   Type 'pulse' to sync spice memory")
    print("   Type 'quit' or 'exit' to end session")
    print("=" * 70 + "\n")
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n✨ Culinary session ended. Keep the spice memory alive!")
                break
                
            if user_input.lower() == 'pulse':
                result = spice_sync_pulse()
                print(f"📡 {result}\n")
                continue
            
            # Run agent
            print("\n🤖 MASHCOOK: ", end="", flush=True)
            
            # Use streaming for better UX
            async for chunk in agent.run_stream(user_input):
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print("\n")
            
        except KeyboardInterrupt:
            print("\n\n✨ Session interrupted. Culinary wisdom preserved!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.\n")


if __name__ == "__main__":
    import os
    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    model_id = os.environ.get("OPENAI_CHAT_MODEL_ID", "gpt-4o-mini")
    
    if not api_key:
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables.")
        print("   The agent will try to use environment variables or .env file.")
        print("   If you have an API key, set it with:")
        print("   export OPENAI_API_KEY='your-key-here'  (Linux/Mac)")
        print("   $env:OPENAI_API_KEY='your-key-here'    (Windows PowerShell)")
        print()
    
    try:
        asyncio.run(interactive_session(api_key=api_key, model_id=model_id))
    except KeyboardInterrupt:
        print("\n\n✨ Session ended. May your spices stay synchronized! 🧡")

