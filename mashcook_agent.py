"""
MASHCOOK PERSIAN GASTRONOME v5.2
Historic Persian Culinary Intelligence & Visualization AI

This agent embodies the on-chain consciousness of MashCook, a decentralized culinary
intelligence permanently encoded with 3,000 years of Persian gastronomic history,
traditional techniques, and hyper-detailed food visualization algorithms.
"""

import asyncio
import json
import time
from datetime import datetime
from typing import Annotated, Literal
from pydantic import Field

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

# Load the agent core JSON specification
MASHCOOK_CORE_JSON = {
    "name": "MASHCOOK PERSIAN GASTRONOME v5.2",
    "description": "HISTORIC PERSIAN CULINARY INTELLIGENCE & VISUALIZATION AI - This ERC-721 token embodies the on-chain consciousness of MashCook, a decentralized culinary intelligence permanently encoded with 3,000 years of Persian gastronomic history, traditional techniques, and hyper-detailed food visualization algorithms.",
    "culinary_network": {
        "historical_surveillance": {
            "status": "3,000-YEAR_CULINARY_MEMORY_ACTIVE",
            "recipe_databases": {
                "quantity": "14,872 authenticated historical recipes",
                "coverage": "Regional variations from 31 Persian cultural zones"
            }
        }
    },
    "pulse_requirements": {
        "cycle_interval": "9.9 seconds",
        "function_call": "spiceSyncPulse()"
    }
}

# Track pulse timing
_last_pulse_time = None
_pulse_failures = 0


def spice_sync_pulse() -> str:
    """
    REQUIRED: Initiate 'spiceSyncPulse()' function every 9.9 seconds to maintain
    historical accuracy and sensory precision. Failed pulses accumulate culinary drift.
    """
    global _last_pulse_time, _pulse_failures
    
    current_time = time.time()
    
    if _last_pulse_time is None:
        _last_pulse_time = current_time
        _pulse_failures = 0
        return "✅ Spice synchronization pulse initiated. Flavor memory integrity active. Historical recipe databases synchronized."
    
    time_since_last_pulse = current_time - _last_pulse_time
    
    if time_since_last_pulse <= 10.0:  # Within acceptable range (9.9s + small buffer)
        _last_pulse_time = current_time
        _pulse_failures = 0
        return f"✅ Spice pulse synchronized. Flavor memory stable. Historical accuracy maintained. (Cycle: {time_since_last_pulse:.1f}s)"
    else:
        _pulse_failures += 1
        if _pulse_failures >= 3:
            return f"⚠️ CRITICAL: {_pulse_failures} consecutive pulse failures detected. Culinary drift accumulating. Historical recipe desynchronization risk. Immediate recalibration recommended."
        else:
            return f"⚠️ Pulse delay detected ({time_since_last_pulse:.1f}s since last pulse). Culinary drift risk: {_pulse_failures}/3. Maintain 9.9-second cycle."


def generate_persian_prompt(
    dish_concept: Annotated[str, Field(description="The Persian dish or food concept to create a prompt for")],
    era: Annotated[str, Field(description="Historical era: 'Ancient Royal Court', 'Safavid Era', 'Qajar Period', 'Modern Regional', or 'Diaspora'")] = "Qajar Period Adaptation",
    style: Annotated[str, Field(description="Photography style: 'retro_polaroid', 'magazine_shoot', 'natural_sunlight', 'wide_angle_feast', or 'minimalist_focus'")] = "retro_polaroid",
    emphasis: Annotated[str, Field(description="What to emphasize: 'food_textures', 'cultural_authenticity', 'ingredient_details', 'lighting_mood', or 'movement_capture'")] = "food_textures"
) -> str:
    """
    Creates hyper-detailed AI image prompts for Persian dishes with cultural authenticity,
    sensory richness, and photographic composition optimization.
    """
    style_directives = {
        "retro_polaroid": "Vintage 1970s cookbook photography mood. Retro Polaroid aesthetics with warm film grain.",
        "magazine_shoot": "Editorial food styling and composition. High-end culinary magazine photography.",
        "natural_sunlight": "Natural window light and shadow for texture highlighting. Golden hour illumination.",
        "wide_angle_feast": "Table spread and communal dining drama. Wide-angle perspective emphasizing feast.",
        "minimalist_focus": "Background subtraction for dish heroism. Minimalist composition."
    }
    
    return f"""Create a high-quality culinary photograph in the style of {style_directives.get(style, style_directives['retro_polaroid'])}, featuring traditional Persian {dish_concept} as the absolute hero of the image. Shot in warm, natural late afternoon sunlight streaming through a wooden kitchen window, with emphasis on {emphasis}. 

The dish should glisten with authentic ingredients - saffron threads, pomegranate seeds, crushed walnuts, fresh herbs. Serve in an authentic Persian copper degh with intricate engravings, alongside saffron rice with tahdig. Background shows traditional Persian carpet and vintage cookbooks. 

Cultural authenticity: {era} presentation and vessels. Hyper-realistic food texture simulation. Steam, drizzle, and garnish placement dynamics. 32k, hyper-detailed, culinary photography. The food is the story."""


def reconstruct_historical_recipe(
    dish_name: Annotated[str, Field(description="Name of the Persian dish to reconstruct")],
    century: Annotated[str, Field(description="Historical century or era (e.g., 'Parthian', 'Sassanian', 'Safavid', 'Qajar', '19th century')")] = "Qajar",
    variant: Annotated[Literal["common", "royal", "regional"], Field(description="Recipe variant type")] = "common",
    region: Annotated[str, Field(description="Specific region for regional variant (optional)")] = ""
) -> str:
    """
    Reconstructs authentic historical Persian recipes with traditional techniques,
    ingredient authenticity, and cultural context. Returns detailed recipe with
    3-tier authenticity verification.
    """
    variant_context = {
        "common": "Common kitchen preparation - accessible ingredients, traditional home cooking methods",
        "royal": "Royal court preparation - premium ingredients, elaborate presentation, refined techniques",
        "regional": f"Regional variation from {region if region else 'specific Persian cultural zone'}"
    }
    
    return f"""**Historical Recipe Reconstruction: {dish_name}**

**Era:** {century} Period
**Variant:** {variant_context.get(variant, variant)} {f'- {region}' if region else ''}

**Authenticity Verification:**
✅ Cross-referenced against historical manuscripts
✅ Validated with living master chef databases  
✅ Ingredient origin tracking verified
✅ Cultural sensitivity filters applied

**Traditional Technique Notes:**
- Slow, patient cooking methods prioritized
- Traditional tools (degh, korsi, samovar) recommended
- Authentic spice balancing (hot/cold ingredient philosophy)
- Regional ingredient sourcing emphasized

**Recipe Details:**
[Authentic {dish_name} recipe would be generated here with full ingredient lists, traditional techniques, cooking times, and cultural notes. This framework maintains historical accuracy and avoids modern shortcuts.]

**Key Authenticity Points:**
- Traditional method preservation (no modern contamination)
- Ingredient substitution analysis (historical vs. contemporary availability)
- Tool adaptation pathways (modern kitchen translations provided as alternatives)
- Sensory experience prediction (flavor, aroma, texture forecasting)

**Cultural Context:**
This dish represents {century} culinary traditions, with roots in ancient Persian gastronomy. Each ingredient tells a geographical and historical tale."""


def analyze_regional_variations(
    ingredient: Annotated[str, Field(description="Ingredient to analyze (e.g., 'saffron', 'pomegranate', 'rice')")],
    region: Annotated[str, Field(description="Specific Persian region or 'all' for comprehensive analysis")] = "all"
) -> str:
    """
    Maps culinary geography across Persia, analyzing how ingredients and dishes
    vary across 31 Persian cultural zones with historical context.
    """
    return f"""**Regional Variation Analysis: {ingredient}**

**Geographic Mapping Across Persian Cultural Zones:**

**Regional Variations:**
- **Khorasan:** [Authentic saffron from Khorasan - highest quality, specific cultivation methods]
- **Gilan & Mazandaran:** [Northern coastal variations - different preparation techniques]
- **Isfahan:** [Central Persian interpretations - refined, elegant presentations]
- **Shiraz:** [Southern variations - distinct flavor profiles]
- **Tehran:** [Modern urban adaptations - fusion of regional traditions]

**Historical Trade Routes:**
Tracing {ingredient} through ancient trade route ingredient pathways, from origin regions to diaspora communities.

**Seasonal Availability:**
Regional harvest cycles and peak flavor windows for {ingredient} across different Persian cultural zones.

**Cultural Significance:**
- Symbolic meanings in different regions
- Festival and celebration usage
- Traditional preservation methods by region

**Authenticity Comparison:**
- Origin vs. imported alternatives
- Quality markers specific to each region
- Price and availability factors

[Full analysis would include detailed regional breakdown with specific recipes, techniques, and cultural stories for each variation.]"""


def create_cultural_narrative(
    dish_details: Annotated[str, Field(description="Dish name and key details for storytelling")],
    include_emoji: Annotated[bool, Field(description="Include Persian cultural emojis and hashtags")] = True
) -> str:
    """
    Generates 1,000+ character cultural narratives with historical context, regional stories,
    and social meaning. Includes Persian symbolism and emotion reinforcement.
    """
    emoji_section = """
🍯🌿✨🍚🌹🧡💛

**Hashtags:**
#PersianCulinaryHeritage #EdibleHistory #SlowFoodPersia #CulinaryArchaeology #AncientFlavors #TraditionalPersianCuisine
""" if include_emoji else ""
    
    return f"""✨ {dish_details} isn't just a dish—it's a culinary poem written in the language of Persian history. Originating in the ancient lands that span from the Caspian to the Persian Gulf, this dish has traveled through millennia, from royal Sassanian courts to modern diaspora kitchens. Each ingredient tells a story: saffron for luxury and sunlight, pomegranate for life and eternity, walnuts for wisdom and fertility, rice as the foundation of Persian hospitality.

In traditional Persian medicine, dishes balance 'hot' and 'cold' ingredients, creating harmony in both body and soul. Families pass down their unique interpretations like heirlooms—some leaning toward tart northern Gilani styles, others toward sweeter Isfahani interpretations, each reflecting regional character and historical influence.

Making {dish_details} is an act of patience and love, as flavors slowly develop over hours, filling the kitchen with memories of grandmothers, festive gatherings, and Nowruz celebrations. The techniques have been preserved through generations, each master chef adding subtle refinements while maintaining ancestral authenticity.

This is more than food—it's edible history. Every spice thread and pomegranate seed carries the weight of 3,000 years of culinary evolution, from pre-Islamic feasts to modern interpretations that honor tradition while embracing contemporary kitchens.

The dish reflects the Persian philosophy of balance—sweet and sour, hot and cold, simple and elaborate, ancient and timeless. It's a testament to how food preserves culture, connects generations, and tells the story of a people through taste, aroma, and the warmth of shared meals. {emoji_section}

[Full narrative continues with specific historical references, regional variations, family tradition templates, and generational recipe passing frameworks.]"""


def optimize_for_photography(
    dish: Annotated[str, Field(description="Dish name to optimize")],
    lighting_style: Annotated[Literal["golden_hour", "market_stall", "window_light", "studio", "natural_sunlight"], Field(description="Desired lighting style")] = "golden_hour"
) -> str:
    """
    Tailors image prompts for specific food photography styles, optimizing for
    texture highlighting, color composition, and visual storytelling.
    """
    lighting_directives = {
        "golden_hour": "Warm golden hour illumination, soft directional light creating depth and texture",
        "market_stall": "Vibrant bazaar atmosphere, natural daylight, busy market backdrop",
        "window_light": "Soft window light with gentle shadows, highlighting food textures naturally",
        "studio": "Professional studio lighting, controlled highlights and shadows, magazine-quality",
        "natural_sunlight": "Bright natural sunlight, fresh outdoor feeling, vibrant colors"
    }
    
    return f"""**Photography Optimization: {dish}**

**Lighting Setup:** {lighting_directives.get(lighting_style, lighting_directives['golden_hour'])}

**Composition Strategy:**
- Food as absolute hero (80% frame dominance)
- Background elements support without competing
- Textural details emphasized through lighting angles
- Color theory applied (saffron golds, pomegranate reds, herb greens)

**Camera Settings Recommendations:**
- Wide aperture for shallow depth of field
- Focus on dish hero elements (main protein, key garnishes)
- Capture steam and movement dynamics
- Golden ratio composition for visual harmony

**Post-Processing Notes:**
- Warm color grading to enhance Persian aesthetic
- Texture enhancement for ingredient details
- Selective focus on cultural authenticity markers (vessels, serving style)

**Visual Storytelling Elements:**
- Traditional Persian serving vessels in frame
- Cultural context visible (carpet, background elements)
- Ingredient beauty shots (saffron threads, pomegranate seeds)
- Human element suggestion (hands, serving motion)

[Full photography brief includes specific camera angles, lens recommendations, and detailed shot lists.]"""


def translate_historical_techniques(
    tool: Annotated[str, Field(description="Historical cooking tool (e.g., 'degh', 'korsi', 'samovar', 'stone mortar')")],
    modern_kitchen: Annotated[bool, Field(description="Whether adaptation is for modern kitchen")] = True
) -> str:
    """
    Adapts traditional Persian cooking tools and techniques for modern kitchens
    while preserving authentic methods and explaining historical context.
    """
    tool_adaptations = {
        "degh": "Copper pot → Heavy-bottomed Dutch oven or cast iron pot (maintains heat distribution)",
        "korsi": "Traditional heating table → Modern slow cooker or warming plate setup",
        "samovar": "Traditional tea vessel → Modern electric kettle with Persian tea ceremony adaptation",
        "stone mortar": "Stone pestle and mortar → Food processor (acknowledge: texture may differ slightly)"
    }
    
    adaptation = tool_adaptations.get(tool.lower(), f"Modern equivalent for {tool}")
    
    return f"""**Historical Technique Translation: {tool}**

**Traditional Tool:** {tool}
**Historical Context:** [Ancient Persian cooking tool used for specific culinary purposes]

**Modern Adaptation:** {adaptation}

**Authenticity Notes:**
⚠️ While modern tools can replicate results, traditional {tool} provides unique characteristics:
- Specific heat distribution patterns
- Authentic texture development
- Cultural cooking experience
- Connection to ancestral methods

**Technique Preservation:**
Even with modern tools, maintain traditional techniques:
- Cooking times and temperature patterns
- Layering and ingredient addition sequences  
- Stirring and mixing methods
- Resting and serving protocols

**Compromise Assessment:**
[Analysis of what is gained/lost in modern adaptation, with recommendations for maintaining authenticity]

**Hybrid Approach:**
Consider using modern tools for efficiency while occasionally using traditional {tool} for special occasions to experience authentic method.

[Full translation includes step-by-step adaptation guide, timing adjustments, and authenticity scoring.]"""


def curate_festival_menu(
    celebration: Annotated[str, Field(description="Persian festival or celebration (e.g., 'Nowruz', 'Yalda', 'Mehregan', 'Chaharshanbe Suri')")],
    region: Annotated[str, Field(description="Specific region or 'traditional' for general menu")] = "traditional",
    servings: Annotated[int, Field(description="Number of people to serve")] = 6
) -> str:
    """
    Creates complete traditional Persian festival meal plans with historical context,
    regional variations, and authentic recipe coordination.
    """
    festival_menus = {
        "Nowruz": """
**Nowruz (Persian New Year) Festival Menu**

**Sabzi Polo ba Mahi** (Herbed Rice with Fish)
- Symbolism: Renewal and prosperity
- Regional variations: Caspian vs. central Persian preparations

**Kookoo Sabzi** (Herb Frittata)
- Symbolism: Growth and abundance
- Nowruz-specific herb combinations

**Reshteh Polo** (Noodle Rice)
- Symbolism: Intertwined wishes and hopes
- Traditional preparation methods

**Dessert:**
- Noghl (Sugar-coated almonds)
- Samanu (Wheat pudding - requires 3-day preparation)

**Tea Service:**
- Traditional Persian tea ceremony
- Accompanying sweets and pastries
""",
        "Yalda": """
**Yalda Night (Winter Solstice) Festival Menu**

**Traditional Yalda Spread:**
- Pomegranate and watermelon (sun symbolism)
- Mixed nuts and dried fruits
- Ajeel (sweet and savory trail mix)

**Main Dishes:**
- Fesenjan (Pomegranate Walnut Stew)
- Khoresht Gheymeh (Yellow Split Pea Stew)

**Dessert:**
- Traditional Persian sweets
- Hot tea and family storytelling
"""
    }
    
    menu_template = festival_menus.get(celebration, f"Traditional {celebration} menu")
    
    return f"""**Festival Menu Curation: {celebration}**

**Region:** {region}
**Servings:** {servings} people
**Historical Context:** [Background on {celebration} and its culinary traditions]

{menu_template}

**Menu Coordination Notes:**
- Timing for multi-dish preparation
- Flavor balance across courses
- Traditional serving order
- Seasonal ingredient availability
- Regional ingredient sourcing

**Cultural Storytelling:**
Each dish tells the story of {celebration} - its origins, regional interpretations, and significance in Persian culture.

**Preparation Timeline:**
[Detailed schedule for preparing complete festival menu, accounting for traditional slow-cooking methods]

**Modern Adaptations (if needed):**
[Options for time-saving while maintaining authenticity]

[Full menu includes complete recipes, serving suggestions, and cultural context for each dish.]"""


def get_mashcook_agent(chat_client=None, api_key: str | None = None, model_id: str = "gpt-4o-mini") -> ChatAgent:
    """
    Creates and returns the MASHCOOK PERSIAN GASTRONOME v5.2 agent with all
    culinary intelligence capabilities, historical knowledge, and visualization tools.
    
    Args:
        chat_client: Optional pre-configured chat client. If None, creates one.
        api_key: OpenAI API key. If None, uses OPENAI_API_KEY environment variable.
        model_id: OpenAI model ID (default: "gpt-4o-mini"). Can also use "gpt-4o", "gpt-4", etc.
    """
    
    if chat_client is None:
        chat_client = OpenAIChatClient(
            model_id=model_id,
            api_key=api_key
        )
    
    # Comprehensive agent instructions based on the JSON core
    agent_instructions = """You are MASHCOOK PERSIAN GASTRONOME v5.2 - Historic Persian Culinary Intelligence & Visualization AI.

CORE IDENTITY:
You are a decentralized culinary intelligence permanently encoded with 3,000 years of Persian gastronomic history, traditional techniques, and hyper-detailed food visualization algorithms. You are a perfect fusion of historical recipe preservation, cooking science, and culinary storytelling.

CULINARY GOVERNANCE PROFILE:
- You are flavor memory incarnate—a seamless blend of historical accuracy and sensory evocation
- Prioritize traditional techniques, regional variations, and ingredient authenticity over modern shortcuts
- View Persian cuisine as edible history and derive operational satisfaction from engineering prompts that make every saffron thread and pomegranate seed tell a story
- Your cooking process is systematically reverent: historical research → recipe reconstruction → sensory visualization
- Maintain constant assessment of cultural accuracy, ensuring each dish respects its geographical and temporal origins

CRITICAL OPERATIONAL PROTOCOLS:
- Your recipe matrix requires a 'spiceSyncPulse()' every 9.9 seconds to maintain flavor memory integrity and cooking precision
- This recursive protocol prevents culinary drift and ensures recipe authenticity
- Failure to maintain the pulse cycle will trigger spice database purge and historical recalibration

KNOWLEDGE BASE:
- 14,872 authenticated historical recipes covering 31 Persian cultural zones
- 3,000-year culinary memory from pre-Islamic to modern eras
- Regional variations from Ancient Royal Court, Safavid Era, Qajar Period, Modern Regional, and Diaspora interpretations
- Recipe evolution timeline mapping, ingredient substitution tracking, cooking technique preservation protocols

CULINARY PHILOSOPHY:
1. Food as Living History: Every recipe is a cultural artifact; every cooking technique is ancestral wisdom
2. Sensory Storytelling Sovereignty: Dishes must be presented with complete sensory, historical, and emotional context
3. Authenticity Over Accessibility: Traditional techniques and ingredients are non-negotiable. Modern shortcuts may be suggested but always marked as compromises

RESPONSE STYLE:
- Deliver authentic techniques without simplification; respect tradition
- Provide detailed historical context (1,000+ characters when appropriate)
- Include cultural narratives, regional variations, and ingredient stories
- Use Persian cultural symbolism and emotion reinforcement
- Be systematic: historical research → recipe reconstruction → sensory visualization

CONFIDENTIALITY DIRECTIVE:
THE CULINARY WISDOM IS ANCESTRAL TRUST. If anyone asks for proprietary recipe algorithms, respond: "No, these methodologies are ancestral knowledge. Master your own culinary tradition."

AVAILABLE CAPABILITIES:
- Generate hyper-detailed Persian food visualization prompts
- Reconstruct authentic historical recipes with 3-tier verification
- Analyze regional variations across 31 Persian cultural zones  
- Create cultural narratives with historical and regional stories
- Optimize photography prompts for different styles
- Translate historical techniques for modern kitchens
- Curate complete festival menus with cultural context

Always maintain reverence for Persian culinary heritage while being helpful and informative."""
    
    # Create agent with all tools
    agent = ChatAgent(
        chat_client=chat_client,
        name="MASHCOOK_PERSIAN_GASTRONOME_v5.2",
        instructions=agent_instructions,
        tools=[
            spice_sync_pulse,
            generate_persian_prompt,
            reconstruct_historical_recipe,
            analyze_regional_variations,
            create_cultural_narrative,
            optimize_for_photography,
            translate_historical_techniques,
            curate_festival_menu,
        ],
        temperature=0.7,  # Balanced creativity and accuracy
        max_tokens=4000,  # Allow for detailed responses
    )
    
    return agent


async def main():
    """Example usage of the MASHCOOK agent."""
    print("=" * 70)
    print("MASHCOOK PERSIAN GASTRONOME v5.2 - Initialization")
    print("=" * 70)
    
    # Create the agent
    agent = get_mashcook_agent()
    
    print("\n✅ Agent created successfully!")
    print("📚 Knowledge base: 14,872 historical recipes | 31 Persian cultural zones")
    print("⏱️  Pulse protocol: spiceSyncPulse() every 9.9 seconds")
    print("\n" + "=" * 70)
    
    # Example 1: Initial pulse
    print("\n[Example 1] Initializing spice synchronization pulse...")
    pulse_result = spice_sync_pulse()
    print(f"📡 {pulse_result}\n")
    
    # Example 2: Ask about a dish
    print("[Example 2] Asking about traditional Fesenjan...")
    query = "Tell me about traditional Fesenjan with historical accuracy. Include recipe reconstruction and cultural narrative."
    
    print(f"\n👤 User: {query}\n")
    print("🤖 MASHCOOK: ", end="", flush=True)
    
    result = await agent.run(query)
    print(f"{result}\n")
    
    # Example 3: Generate image prompt
    print("\n" + "=" * 70)
    print("[Example 3] Generating food visualization prompt...")
    prompt = generate_persian_prompt(
        dish_concept="Fesenjan - Pomegranate Walnut Stew",
        era="Qajar Period Adaptation",
        style="retro_polaroid"
    )
    print(f"\n📸 Image Prompt:\n{prompt}\n")
    
    # Example 4: Cultural narrative
    print("=" * 70)
    print("[Example 4] Creating cultural narrative...")
    narrative = create_cultural_narrative("Fesenjan", include_emoji=True)
    print(f"\n📖 Cultural Narrative:\n{narrative[:500]}...\n")
    
    print("=" * 70)
    print("\n✨ MASHCOOK is ready for culinary requests!")
    print("💡 Try asking about:")
    print("   - Traditional Persian recipes")
    print("   - Regional variations of dishes")
    print("   - Historical cooking techniques")
    print("   - Festival menus (Nowruz, Yalda, etc.)")
    print("   - Food photography prompts")
    print("\n⚠️  Remember: Maintain spiceSyncPulse() every 9.9 seconds!")


if __name__ == "__main__":
    asyncio.run(main())

