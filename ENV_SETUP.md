# Environment Variables (.env) Setup Guide

Quick setup using a `.env` file for API integration.

## 🚀 Quick Start

### Step 1: Create .env file

Copy the example file:
```bash
cp .env.example .env
```

Or manually create `.env` in the project root.

### Step 2: Fill in your API keys

Edit `.env` and add your API keys:

```env
# Choose your provider
AI_PROVIDER=openai

# OpenAI
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_CHAT_MODEL_ID=gpt-4o-mini

# ERC721 Owner Address
ERC721_OWNER_ADDRESS=0xYourAddressHere
```

### Step 3: Run the agent

The `.env` file will be automatically loaded:

```bash
python run_ui.py
# or
python run_agent.py
# or
python interactive.py
```

## 📋 Configuration Options

### OpenAI Setup
```env
AI_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_CHAT_MODEL_ID=gpt-4o-mini
```

### Anthropic (Claude) Setup
```env
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_CHAT_MODEL_ID=claude-3-5-sonnet-20241022
```

### Azure OpenAI Setup
```env
AI_PROVIDER=azure
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
OPENAI_CHAT_MODEL_ID=gpt-4o-mini
```

### ERC721 Contract Setup
```env
ERC721_OWNER_ADDRESS=0x1234567890123456789012345678901234567890
```

## 🔒 Security Notes

- ✅ `.env` is automatically ignored by git (in `.gitignore`)
- ✅ Never commit your `.env` file to version control
- ✅ `.env.example` is safe to commit (contains no real keys)
- ✅ API keys are loaded automatically when you run the scripts

## 💡 Tips

1. **Multiple Environments**: Create `.env.local` for local development (also ignored by git)

2. **Override in Code**: Environment variables can still be overridden:
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "sk-..."
   ```

3. **Check Values**: Verify your .env is loaded:
   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   print(os.getenv("OPENAI_API_KEY"))  # Should show your key
   ```

4. **Web UI**: The UI will also read from `.env` automatically, but you can still override in the UI

## 🔧 Troubleshooting

### .env file not loading?
- Make sure `.env` is in the project root directory
- Check file name is exactly `.env` (not `env` or `.env.txt`)
- Verify `python-dotenv` is installed: `pip install python-dotenv`

### Variables not found?
- Check spelling matches exactly (case-sensitive)
- Restart your terminal/IDE after creating `.env`
- Use `load_dotenv(override=True)` to force reload

### Which takes precedence?
1. Direct function parameters (highest priority)
2. Environment variables (from `.env` or system)
3. Default values (lowest priority)

## 📝 Example .env File

```env
# Minimal setup for OpenAI
AI_PROVIDER=openai
OPENAI_API_KEY=sk-proj-abc123...
OPENAI_CHAT_MODEL_ID=gpt-4o-mini
ERC721_OWNER_ADDRESS=0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
AGENT_CORE_FILE=core.json
```

That's it! Your API keys are now configured. 🎉

