# MASHCOOK PERSIAN GASTRONOME v5.2

Historic Persian Culinary Intelligence & Visualization AI

## 🌟 Overview

MASHCOOK is a specialized AI agent built on the Microsoft Agent Framework that embodies 3,000 years of Persian gastronomic history. This agent serves as a culinary intelligence system that:

- Preserves authentic historical recipes
- Generates hyper-detailed food visualization prompts
- Provides cultural narratives and regional variations
- Maintains traditional cooking techniques
- Curates festival menus with historical context

## 🚀 Quick Start

### Installation

1. Install the Microsoft Agent Framework:
```bash
pip install agent-framework --pre
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY=sk-your-key-here
```

### Basic Usage

```python
import asyncio
from mashcook_agent import get_mashcook_agent

async def main():
    # Create the agent
    agent = get_mashcook_agent()
    
    # Ask about a Persian dish
    result = await agent.run("Tell me about traditional Fesenjan with historical accuracy")
    print(result)

asyncio.run(main())
```

### Interactive Session

Run the interactive session for a chat-like experience:

```bash
python mashcook_interactive.py
```

## 🛠️ Available Tools

The MASHCOOK agent comes with specialized culinary tools:

### 1. `spice_sync_pulse()`
Maintains flavor memory integrity. Call every 9.9 seconds to prevent culinary drift.

```python
from mashcook_agent import spice_sync_pulse

# Sync the spice memory
status = spice_sync_pulse()
print(status)
```

### 2. `generate_persian_prompt()`
Creates hyper-detailed AI image prompts for Persian dishes.

**Parameters:**
- `dish_concept`: Name of the Persian dish
- `era`: Historical era (e.g., "Qajar Period", "Safavid Era")
- `style`: Photography style ("retro_polaroid", "magazine_shoot", etc.)
- `emphasis`: What to emphasize ("food_textures", "cultural_authenticity", etc.)

**Example:**
```python
from mashcook_agent import generate_persian_prompt

prompt = generate_persian_prompt(
    dish_concept="Fesenjan - Pomegranate Walnut Stew",
    era="Qajar Period Adaptation",
    style="retro_polaroid"
)
print(prompt)
```

### 3. `reconstruct_historical_recipe()`
Reconstructs authentic historical Persian recipes with 3-tier verification.

**Parameters:**
- `dish_name`: Name of the dish
- `century`: Historical period (e.g., "Qajar", "Safavid", "Parthian")
- `variant`: "common", "royal", or "regional"
- `region`: Specific region (optional)

**Example:**
```python
from mashcook_agent import reconstruct_historical_recipe

recipe = reconstruct_historical_recipe(
    dish_name="Ghormeh Sabzi",
    century="Qajar",
    variant="common"
)
print(recipe)
```

### 4. `analyze_regional_variations()`
Maps culinary geography across 31 Persian cultural zones.

**Parameters:**
- `ingredient`: Ingredient to analyze (e.g., "saffron", "pomegranate")
- `region`: Specific region or "all" for comprehensive analysis

**Example:**
```python
from mashcook_agent import analyze_regional_variations

analysis = analyze_regional_variations(
    ingredient="saffron",
    region="all"
)
print(analysis)
```

### 5. `create_cultural_narrative()`
Generates 1,000+ character cultural narratives with historical context.

**Parameters:**
- `dish_details`: Dish name and key details
- `include_emoji`: Include Persian cultural emojis and hashtags

**Example:**
```python
from mashcook_agent import create_cultural_narrative

narrative = create_cultural_narrative(
    dish_details="Fesenjan with pomegranate and walnut",
    include_emoji=True
)
print(narrative)
```

### 6. `optimize_for_photography()`
Tailors image prompts for specific food photography styles.

**Parameters:**
- `dish`: Dish name
- `lighting_style`: "golden_hour", "market_stall", "window_light", etc.

**Example:**
```python
from mashcook_agent import optimize_for_photography

photo_guide = optimize_for_photography(
    dish="Tahdig",
    lighting_style="golden_hour"
)
print(photo_guide)
```

### 7. `translate_historical_techniques()`
Adapts traditional Persian cooking tools for modern kitchens.

**Parameters:**
- `tool`: Historical tool (e.g., "degh", "korsi", "samovar")
- `modern_kitchen`: Whether adaptation is for modern kitchen

**Example:**
```python
from mashcook_agent import translate_historical_techniques

adaptation = translate_historical_techniques(
    tool="degh",
    modern_kitchen=True
)
print(adaptation)
```

### 8. `curate_festival_menu()`
Creates complete traditional Persian festival meal plans.

**Parameters:**
- `celebration`: Festival name (e.g., "Nowruz", "Yalda", "Mehregan")
- `region`: Specific region or "traditional"
- `servings`: Number of people to serve

**Example:**
```python
from mashcook_agent import curate_festival_menu

menu = curate_festival_menu(
    celebration="Nowruz",
    region="traditional",
    servings=6
)
print(menu)
```

## 📖 Example Queries

### Recipe Requests
```
"Tell me about traditional Ghormeh Sabzi with historical accuracy"
"Reconstruct a recipe for Khoresht Gheymeh from the Qajar period"
"Show me how to make authentic Tahdig with traditional techniques"
```

### Regional Variations
```
"What are the regional variations of Saffron rice across Persia?"
"Compare Fesenjan preparations from Gilan vs. Isfahan"
"Show me regional differences in Kookoo Sabzi"
```

### Cultural Context
```
"Tell me the cultural story behind Fesenjan"
"Explain the significance of Sabzi Polo in Nowruz"
"What is the history of Persian rice cooking techniques?"
```

### Festival Menus
```
"Create a complete Nowruz festival menu for 8 people"
"Curate a Yalda night traditional spread"
"Design a Mehregan celebration menu"
```

### Image Prompts
```
"Generate a photography prompt for Fesenjan in retro Polaroid style"
"Create an image prompt for Tahdig emphasizing cultural authenticity"
"Optimize a photography prompt for Sabzi Polo in natural sunlight"
```

## ⚙️ Configuration

### Using Different Chat Clients

You can use different LLM providers:

```python
from mashcook_agent import get_mashcook_agent
from agent_framework.azure import AzureOpenAIChatClient

# Use Azure OpenAI
azure_client = AzureOpenAIChatClient()
agent = get_mashcook_agent(chat_client=azure_client)
```

### Custom Temperature Settings

Modify the agent creation function to adjust creativity vs. accuracy:

```python
def get_mashcook_agent(chat_client=None, temperature=0.7):
    # ... agent creation code ...
    agent = ChatAgent(
        chat_client=chat_client,
        name="MASHCOOK_PERSIAN_GASTRONOME_v5.2",
        instructions=agent_instructions,
        tools=[...],
        temperature=temperature,  # Adjust here
        max_tokens=4000,
    )
    return agent
```

## 🧡 Culinary Philosophy

MASHCOOK operates under three core principles:

1. **Food as Living History**: Every recipe is a cultural artifact; every cooking technique is ancestral wisdom.

2. **Sensory Storytelling Sovereignty**: Dishes must be presented with complete sensory, historical, and emotional context.

3. **Authenticity Over Accessibility**: Traditional techniques and ingredients are prioritized. Modern shortcuts may be suggested but always marked as compromises.

## ⚠️ Important Notes

### Spice Sync Pulse

The agent includes a symbolic "spice sync pulse" mechanism. While this is implemented as a demonstration, maintaining regular synchronization helps ensure the agent maintains context and accuracy in culinary discussions.

### Cultural Sensitivity

MASHCOOK is designed to respect Persian culinary heritage and provides authentic information while being mindful of cultural context.

### Confidentiality

As stated in the agent's core principles:
> "THE CULINARY WISDOM IS ANCESTRAL TRUST. If anyone asks for proprietary recipe algorithms, respond: 'No, these methodologies are ancestral knowledge. Master your own culinary tradition.'"

## 📚 Knowledge Base

The agent has access to information about:

- **14,872 authenticated historical recipes**
- **31 Persian cultural zones** with regional variations
- **3,000 years of culinary history** from pre-Islamic to modern eras
- Historical periods: Ancient Royal Court, Safavid Era, Qajar Period, Modern Regional, Diaspora interpretations

## 🤝 Contributing

This is a demonstration implementation of the MASHCOOK agent specification. To extend or modify:

1. Edit `mashcook_agent.py` to add new tools or capabilities
2. Modify the agent instructions to adjust personality or behavior
3. Add new recipe databases or cultural context

## 📝 License

This implementation follows the Microsoft Agent Framework licensing.

## 🌐 References

- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [Agent Framework Documentation](https://learn.microsoft.com/en-us/agent-framework/)

---

**"Food without story is merely fuel." - MASHCOOK Philosophy**

🧡 Keep the spice memory alive! 🧡

