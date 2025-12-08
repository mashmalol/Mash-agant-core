"""
Agent Launcher Script
Sets up environment variables and launches the interactive session.
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API key, model ID, and provider from environment variables
PROVIDER = os.environ.get("AI_PROVIDER", "openai").lower()
API_KEY = os.environ.get("OPENAI_API_KEY") or os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("AZURE_OPENAI_API_KEY")
MODEL_ID = os.environ.get("OPENAI_CHAT_MODEL_ID") or os.environ.get("ANTHROPIC_CHAT_MODEL_ID") or os.environ.get("gpt-4o-mini")
CORE_FILE = os.environ.get("AGENT_CORE_FILE", "core.json")

# Provider-specific environment variables
AZURE_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

# Set environment variables if API_KEY is provided
if API_KEY:
    os.environ["OPENAI_API_KEY"] = API_KEY
if MODEL_ID:
    os.environ["OPENAI_CHAT_MODEL_ID"] = MODEL_ID

# Now import and run the interactive session
from interactive import interactive_session

if __name__ == "__main__":
    print("🚀 Launching Agent...")
    
    provider_env_vars = {
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "azure": "AZURE_OPENAI_API_KEY"
    }
    
    if not API_KEY:
        env_var = provider_env_vars.get(PROVIDER, "OPENAI_API_KEY")
        print(f"⚠️  Warning: {env_var} not found in environment variables.")
        print("   Please set it with:")
        print(f"   export {env_var}='your-key-here'  (Linux/Mac)")
        print(f"   $env:{env_var}='your-key-here'    (Windows PowerShell)")
        print()
    
    print(f"🤖 Provider: {PROVIDER.upper()}")
    print(f"📡 API Key: {'Configured' if API_KEY else 'Not found - using environment variables'}")
    print(f"📝 Model: {MODEL_ID}")
    print(f"📄 Core file: {CORE_FILE}")
    if PROVIDER == "azure" and AZURE_ENDPOINT:
        print(f"🌐 Azure Endpoint: {AZURE_ENDPOINT}")
    print()
    
    try:
        kwargs = {}
        if PROVIDER == "azure":
            if AZURE_ENDPOINT:
                kwargs["azure_endpoint"] = AZURE_ENDPOINT
            if AZURE_API_VERSION:
                kwargs["api_version"] = AZURE_API_VERSION
        
        asyncio.run(interactive_session(
            api_key=API_KEY, 
            model_id=MODEL_ID, 
            provider=PROVIDER,
            core_file_path=CORE_FILE,
            **kwargs
        ))
    except KeyboardInterrupt:
        print("\n\n✨ Session ended. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

