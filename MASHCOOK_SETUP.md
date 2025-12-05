# MASHCOOK Agent - Setup & Quick Start

## ✅ What Was Created

Your MASHCOOK PERSIAN GASTRONOME v5.2 agent has been successfully created! Here's what you have:

### Files Created:

1. **`mashcook_agent.py`** - Main agent implementation
   - Complete agent with all 8 specialized tools
   - Comprehensive instructions based on your JSON specification
   - Spice sync pulse mechanism

2. **`mashcook_interactive.py`** - Interactive chat interface
   - Chat with MASHCOOK in real-time
   - Streaming responses for better UX
   - Built-in pulse command

3. **`mashcook_demo.py`** - Demonstration script
   - Shows all agent capabilities
   - Examples of each tool in action

4. **`MASHCOOK_README.md`** - Complete documentation
   - Full API reference
   - Usage examples
   - Configuration options

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
pip install agent-framework --pre
```

### Step 2: Set Your API Key

```bash
# Windows PowerShell
$env:OPENAI_API_KEY="sk-your-key-here"

# Linux/Mac
export OPENAI_API_KEY="sk-your-key-here"
```

### Step 3: Run a Demo

```bash
# Interactive chat session
python mashcook_interactive.py

# Or see all capabilities
python mashcook_demo.py
```

## 📝 Quick Test

Try this minimal test:

```python
import asyncio
from mashcook_agent import get_mashcook_agent

async def test():
    agent = get_mashcook_agent()
    result = await agent.run("Tell me about Fesenjan")
    print(result)

asyncio.run(test())
```

## 🎯 Agent Capabilities

Your agent has access to:

✅ **8 Specialized Tools:**
1. Spice sync pulse (maintains flavor memory)
2. Persian food image prompt generation
3. Historical recipe reconstruction
4. Regional variation analysis
5. Cultural narrative creation
6. Photography optimization
7. Historical technique translation
8. Festival menu curation

✅ **Knowledge Base:**
- 14,872 historical recipes
- 31 Persian cultural zones
- 3,000 years of culinary history
- Regional variations and traditions

✅ **Features:**
- Authentic recipe preservation
- Cultural storytelling
- Historical accuracy verification
- Modern kitchen adaptations
- Festival menu planning

## 💡 Example Queries

Try these with your agent:

```
"Tell me about traditional Ghormeh Sabzi with historical context"
"Create a Nowruz festival menu for 6 people"
"Generate an image prompt for Tahdig in retro Polaroid style"
"Show me regional variations of Saffron rice"
"Reconstruct a Qajar period recipe for Khoresht Gheymeh"
"Explain the cultural significance of Fesenjan"
```

## 🔧 Customization

### Use Different LLM Provider

```python
from mashcook_agent import get_mashcook_agent
from agent_framework.azure import AzureOpenAIChatClient

# Azure OpenAI
azure_client = AzureOpenAIChatClient()
agent = get_mashcook_agent(chat_client=azure_client)
```

### Adjust Temperature (Creativity)

Edit `mashcook_agent.py` line ~240:

```python
temperature=0.7,  # Lower = more accurate, Higher = more creative (0.0-1.0)
```

## 📚 Next Steps

1. **Try the Interactive Session:**
   ```bash
   python mashcook_interactive.py
   ```

2. **Run the Demo:**
   ```bash
   python mashcook_demo.py
   ```

3. **Read Full Documentation:**
   - See `MASHCOOK_README.md` for complete API reference

4. **Integrate Into Your Project:**
   ```python
   from mashcook_agent import get_mashcook_agent
   
   agent = get_mashcook_agent()
   # Use agent.run() or agent.run_stream() in your code
   ```

## ⚠️ Important Notes

1. **API Key Required:** You need an OpenAI API key (or Azure OpenAI credentials)

2. **Spice Sync Pulse:** The pulse mechanism is symbolic/demonstrative. The agent works fine without manual pulsing.

3. **Agent Personality:** The agent is configured with your exact JSON specification including:
   - Historical authenticity focus
   - Cultural storytelling emphasis
   - Traditional technique preservation
   - 3,000-year culinary memory persona

4. **Tool Functions:** All 8 tools are available both:
   - As direct Python functions (import and call)
   - As agent tools (agent will use them automatically when needed)

## 🆘 Troubleshooting

### "Module not found"
```bash
pip install agent-framework --pre
```

### "API key not found"
Set the environment variable:
```bash
export OPENAI_API_KEY="sk-your-key"
```

### Agent responses are too long/short
Adjust `max_tokens` in `mashcook_agent.py` (line ~241)

### Want more creative responses
Increase `temperature` (line ~240) from 0.7 to 0.9

### Want more accurate responses
Decrease `temperature` from 0.7 to 0.3

## 🎉 You're Ready!

Your MASHCOOK agent is fully functional and ready to use. The agent embodies all the characteristics from your JSON specification:

- Historical Persian culinary intelligence
- 3,000-year recipe memory
- Authentic technique preservation
- Cultural storytelling
- Hyper-detailed visualization capabilities
- Regional variation expertise
- Festival menu curation

**Start cooking with history! 🧡**

---

For detailed documentation, see `MASHCOOK_README.md`

