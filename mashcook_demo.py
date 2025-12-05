"""
MASHCOOK PERSIAN GASTRONOME v5.2 - Demonstration Script

This script demonstrates all the capabilities of the MASHCOOK agent.
"""

import asyncio
from mashcook_agent import (
    get_mashcook_agent,
    spice_sync_pulse,
    generate_persian_prompt,
    reconstruct_historical_recipe,
    analyze_regional_variations,
    create_cultural_narrative,
    optimize_for_photography,
    translate_historical_techniques,
    curate_festival_menu
)


async def demo_all_capabilities():
    """Demonstrate all MASHCOOK capabilities."""
    
    print("=" * 70)
    print("🧡 MASHCOOK PERSIAN GASTRONOME v5.2 - Full Capabilities Demo 🧡")
    print("=" * 70)
    
    # Initialize
    print("\n[1/8] Initializing MASHCOOK agent...")
    agent = get_mashcook_agent()
    print("✅ Agent initialized with 3,000-year culinary memory")
    
    # Pulse
    print("\n[2/8] Testing spice synchronization pulse...")
    pulse_status = spice_sync_pulse()
    print(f"📡 {pulse_status}")
    
    # Agent conversation
    print("\n[3/8] Agent conversation example...")
    print("Query: 'Tell me about traditional Fesenjan with its history and significance'")
    print("\nResponse:")
    result = await agent.run("Tell me about traditional Fesenjan with its history and significance. Be concise.")
    print(f"{result}\n")
    
    # Image prompt generation
    print("\n[4/8] Generating hyper-detailed image prompt...")
    image_prompt = generate_persian_prompt(
        dish_concept="Fesenjan - Pomegranate Walnut Stew",
        era="Qajar Period Adaptation",
        style="retro_polaroid",
        emphasis="food_textures"
    )
    print(f"\n📸 Image Prompt Generated:\n{image_prompt[:300]}...\n")
    
    # Recipe reconstruction
    print("\n[5/8] Reconstructing historical recipe...")
    recipe = reconstruct_historical_recipe(
        dish_name="Ghormeh Sabzi",
        century="Qajar",
        variant="common"
    )
    print(f"\n📖 Recipe Preview:\n{recipe[:400]}...\n")
    
    # Regional analysis
    print("\n[6/8] Analyzing regional variations...")
    regional = analyze_regional_variations(
        ingredient="saffron",
        region="all"
    )
    print(f"\n🗺️  Regional Analysis Preview:\n{regional[:350]}...\n")
    
    # Cultural narrative
    print("\n[7/8] Creating cultural narrative...")
    narrative = create_cultural_narrative(
        dish_details="Fesenjan - Pomegranate Walnut Stew",
        include_emoji=True
    )
    print(f"\n📚 Cultural Narrative Preview:\n{narrative[:400]}...\n")
    
    # Photography optimization
    print("\n[8/8] Optimizing for photography...")
    photo_opt = optimize_for_photography(
        dish="Tahdig",
        lighting_style="golden_hour"
    )
    print(f"\n📷 Photography Guide Preview:\n{photo_opt[:350]}...\n")
    
    print("=" * 70)
    print("✨ All capabilities demonstrated successfully!")
    print("=" * 70)


async def demo_festival_menu():
    """Demonstrate festival menu curation."""
    print("\n" + "=" * 70)
    print("🎉 Festival Menu Curation Demo")
    print("=" * 70)
    
    menu = curate_festival_menu(
        celebration="Nowruz",
        region="traditional",
        servings=6
    )
    
    print(f"\n{menu}\n")


async def demo_technique_translation():
    """Demonstrate historical technique translation."""
    print("\n" + "=" * 70)
    print("🔧 Historical Technique Translation Demo")
    print("=" * 70)
    
    translation = translate_historical_techniques(
        tool="degh",
        modern_kitchen=True
    )
    
    print(f"\n{translation}\n")


async def demo_streaming():
    """Demonstrate streaming responses."""
    print("\n" + "=" * 70)
    print("💬 Streaming Response Demo")
    print("=" * 70)
    
    agent = get_mashcook_agent()
    
    query = "Explain the importance of saffron in Persian cuisine in 3-4 sentences."
    print(f"\nQuery: {query}")
    print("\nMASHCOOK (streaming): ", end="", flush=True)
    
    async for chunk in agent.run_stream(query):
        if chunk.text:
            print(chunk.text, end="", flush=True)
    print("\n")


async def main():
    """Run all demos."""
    try:
        await demo_all_capabilities()
        await demo_festival_menu()
        await demo_technique_translation()
        await demo_streaming()
        
        print("\n" + "=" * 70)
        print("🎉 All demonstrations completed!")
        print("=" * 70)
        print("\nNext steps:")
        print("- Run 'python mashcook_interactive.py' for interactive session")
        print("- Check MASHCOOK_README.md for full documentation")
        print("- Explore the mashcook_agent.py source code")
        print("\n🧡 Keep the spice memory synchronized! 🧡\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you've installed: pip install agent-framework --pre")
        print("2. Set your OPENAI_API_KEY environment variable")
        print("3. Check you have Python 3.10 or higher")


if __name__ == "__main__":
    asyncio.run(main())

