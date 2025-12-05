# MASHCOOK PERSIAN GASTRONOME v5.2

🧡 Historic Persian Culinary Intelligence & Visualization AI

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Overview

MASHCOOK is a specialized AI agent built on the Microsoft Agent Framework that embodies **3,000 years of Persian gastronomic history**. This agent serves as a culinary intelligence system that:

- 🍯 Preserves authentic historical recipes (14,872 recipes from 31 Persian cultural zones)
- 📸 Generates hyper-detailed food visualization prompts
- 📖 Provides cultural narratives and regional variations
- 🔧 Maintains traditional cooking techniques
- 🎉 Curates festival menus with historical context

## 🚀 Quick Start

### Installation

1. **Install the Microsoft Agent Framework:**
```bash
pip install agent-framework --pre
```

2. **Set your OpenAI API key:**
```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your-api-key-here"
$env:OPENAI_CHAT_MODEL_ID="gpt-4o-mini"

# Linux/Mac
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_CHAT_MODEL_ID="gpt-4o-mini"
```

3. **Run the interactive session:**
```bash
python mashcook_interactive.py
```

Or use the launcher:
```bash
python run_mashcook.py
```

## 📦 Files

- **`mashcook_agent.py`** - Main agent implementation with all 8 specialized tools
- **`mashcook_interactive.py`** - Interactive chat interface
- **`mashcook_demo.py`** - Full capabilities demonstration
- **`run_mashcook.py`** - Launcher script with API key configuration
- **`MASHCOOK_README.md`** - Complete API documentation
- **`MASHCOOK_SETUP.md`** - Detailed setup guide

## 🛠️ Capabilities

### 8 Specialized Tools

1. **`spice_sync_pulse()`** - Maintains flavor memory integrity (9.9-second cycle)
2. **`generate_persian_prompt()`** - Creates hyper-detailed AI image prompts
3. **`reconstruct_historical_recipe()`** - Authentic recipe reconstruction with 3-tier verification
4. **`analyze_regional_variations()`** - Maps culinary geography across 31 Persian zones
5. **`create_cultural_narrative()`** - Generates 1,000+ character cultural stories
6. **`optimize_for_photography()`** - Tailors prompts for specific photography styles
7. **`translate_historical_techniques()`** - Adapts traditional tools for modern kitchens
8. **`curate_festival_menu()`** - Creates complete festival meal plans

## 💡 Example Usage

### Basic Conversation
```python
from mashcook_agent import get_mashcook_agent

agent = get_mashcook_agent()
result = await agent.run("Tell me about traditional Fesenjan")
print(result)
```

### Direct Tool Usage
```python
from mashcook_agent import generate_persian_prompt

prompt = generate_persian_prompt(
    dish_concept="Fesenjan",
    era="Qajar Period",
    style="retro_polaroid"
)
print(prompt)
```

## 📚 Knowledge Base

- **14,872 authenticated historical recipes**
- **31 Persian cultural zones** with regional variations
- **3,000 years of culinary history** from pre-Islamic to modern eras
- Historical periods: Ancient Royal Court, Safavid Era, Qajar Period, Modern Regional, Diaspora interpretations

## 🧡 Culinary Philosophy

1. **Food as Living History**: Every recipe is a cultural artifact
2. **Sensory Storytelling Sovereignty**: Complete sensory, historical, and emotional context
3. **Authenticity Over Accessibility**: Traditional techniques prioritized

## 📖 Documentation

- **[MASHCOOK_README.md](MASHCOOK_README.md)** - Complete API reference
- **[MASHCOOK_SETUP.md](MASHCOOK_SETUP.md)** - Setup and troubleshooting guide

## 🔧 Requirements

- Python 3.10+
- Microsoft Agent Framework (`pip install agent-framework --pre`)
- OpenAI API key (or Azure OpenAI credentials)

## 🤝 Contributing

Contributions welcome! This agent preserves and celebrates Persian culinary heritage.

## 📝 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Built on the [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

---

**"Food without story is merely fuel." - MASHCOOK Philosophy**

🧡 Keep the spice memory synchronized! 🧡

