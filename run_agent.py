"""
Agent Launcher Script
Sets up environment variables and launches the interactive session.
"""

import os
import sys
import asyncio

# Set API key and model ID from environment variables
API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL_ID = os.environ.get("OPENAI_CHAT_MODEL_ID", "gpt-4o-mini")
CORE_FILE = os.environ.get("AGENT_CORE_FILE", "core.json")

# Set environment variables if API_KEY is provided
if API_KEY:
    os.environ["OPENAI_API_KEY"] = API_KEY
if MODEL_ID:
    os.environ["OPENAI_CHAT_MODEL_ID"] = MODEL_ID

# Now import and run the interactive session
from interactive import interactive_session

if __name__ == "__main__":
    print("🚀 Launching Agent...")
    
    if not API_KEY:
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables.")
        print("   Please set it with:")
        print("   export OPENAI_API_KEY='your-key-here'  (Linux/Mac)")
        print("   $env:OPENAI_API_KEY='your-key-here'    (Windows PowerShell)")
        print()
    
    print(f"📡 API Key: {'Configured' if API_KEY else 'Not found - using environment variables'}")
    print(f"🤖 Model: {MODEL_ID}")
    print(f"📄 Core file: {CORE_FILE}\n")
    
    try:
        asyncio.run(interactive_session(api_key=API_KEY, model_id=MODEL_ID, core_file_path=CORE_FILE))
    except KeyboardInterrupt:
        print("\n\n✨ Session ended. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

