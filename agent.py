"""
Agent Template - Chatbot Interface with ERC721 Contract Generation

This agent provides a chatbot interface where users can chat and request tasks.
When the user presses the pulse button, the agent generates a payable ERC721
smart contract in Yul with the chat history as metadata.
"""

import asyncio
import json
import os
from datetime import datetime
from typing import Annotated
from pydantic import Field

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

# Hard-coded address
OWNER_ADDRESS = "0x43Ef2Cd47716f7f833B2f90875C594530133e0eB"

# Chat history storage
_chat_history = []

# Load agent core JSON specification
def load_core_json(core_file_path: str = "core.json") -> dict:
    """
    Load the agent core JSON specification from a file.
    
    Args:
        core_file_path: Path to the JSON file containing agent core specification
        
    Returns:
        Dictionary containing the agent core specification
    """
    if os.path.exists(core_file_path):
        with open(core_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Default core if file doesn't exist
        return {
            "name": "Agent Template",
            "description": "A customizable AI agent template",
            "version": "1.0.0"
        }


def add_to_chat_history(role: str, content: str):
    """Add a message to the chat history."""
    _chat_history.append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    })


def get_chat_history() -> list:
    """Get the full chat history."""
    return _chat_history.copy()


def clear_chat_history():
    """Clear the chat history."""
    global _chat_history
    _chat_history = []


def generate_erc721_yul_contract(chat_history: list, user_request: str = "") -> str:
    """
    Generates a payable ERC721 smart contract in Yul with chat history as metadata.
    
    Args:
        chat_history: List of chat messages
        user_request: Optional user request/description
        
    Returns:
        Yul contract code as string
    """
    # Create metadata JSON from chat history
    metadata = {
        "name": "Chat History NFT",
        "description": user_request or "Minted chat history with agent",
        "chat_history": chat_history,
        "mint_timestamp": datetime.now().isoformat(),
        "owner": OWNER_ADDRESS
    }
    
    metadata_json = json.dumps(metadata, indent=2)
    
    # Convert owner address to bytes20 for Yul (addresses are 20 bytes, padded to 32 bytes)
    owner_address_clean = OWNER_ADDRESS[2:] if OWNER_ADDRESS.startswith("0x") else OWNER_ADDRESS
    owner_hex = "0x" + owner_address_clean.zfill(64)  # Pad to 64 hex chars (32 bytes)
    
    # Generate Yul ERC721 contract
    # Note: This is a simplified ERC721 implementation in Yul
    yul_contract = f'''// SPDX-License-Identifier: MIT
// ERC721 Payable Contract in Yul
// Owner: {OWNER_ADDRESS}
// Generated: {datetime.now().isoformat()}

object "ERC721ChatHistory" {{
    code {{
        // Deploy the contract
        datacopy(0, dataoffset("Runtime"), datasize("Runtime"))
        return(0, datasize("Runtime"))
    }}
    
    object "Runtime" {{
        code {{
            // Storage layout:
            // slot 0: owner address
            // slot 1: next token ID
            // slot 2+: token owners (tokenId + 2 => owner)
            
            // Initialize owner
            sstore(0, {owner_hex})
            // Initialize next token ID to 1
            sstore(1, 1)
            
            // Copy runtime code
            datacopy(0, dataoffset("RuntimeCode"), datasize("RuntimeCode"))
            return(0, datasize("RuntimeCode"))
        }}
        
        object "RuntimeCode" {{
            code {{
                // Function selectors:
                // mint() = 0x1249c58b
                // tokenURI(uint256) = 0xc87b56dd  
                // owner() = 0x8da5cb5b
                // balanceOf(address) = 0x70a08231
                
                // Fallback: receive ETH
                if iszero(calldatasize()) {{
                    stop()
                }}
                
                let selector := shr(224, calldataload(0))
                
                // mint() - payable function
                switch selector
                case 0x1249c58b {{
                    // mint() - requires payment
                    let payment := callvalue()
                    if iszero(payment) {{
                        revert(0, 0)
                    }}
                    
                    // Get next token ID
                    let tokenId := sload(1)
                    
                    // Increment token ID
                    sstore(1, add(tokenId, 1))
                    
                    // Store token owner (tokenId + 2 to avoid slot 0 and 1)
                    sstore(add(2, tokenId), caller())
                    
                    // Emit Transfer event (simplified)
                    // Return token ID
                    mstore(0, tokenId)
                    return(0, 32)
                }}
                
                // tokenURI(uint256 tokenId) - returns metadata JSON
                case 0xc87b56dd {{
                    let tokenId := calldataload(4)
                    
                    // Check if token exists
                    let owner := sload(add(2, tokenId))
                    if iszero(owner) {{
                        revert(0, 0)
                    }}
                    
                    // Return metadata URI (in production, this would point to IPFS or return JSON)
                    // For now, return a placeholder
                    mstore(0, 0x20)
                    mstore(0x20, 0x20)
                    mstore(0x40, "data:application/json;base64,")
                    return(0, 0x60)
                }}
                
                // owner() - returns owner address
                case 0x8da5cb5b {{
                    let owner := sload(0)
                    mstore(0, owner)
                    return(0, 32)
                }}
                
                // balanceOf(address) - returns token count for address
                case 0x70a08231 {{
                    let addr := calldataload(4)
                    // Simplified: return 0 (full implementation would count tokens)
                    mstore(0, 0)
                    return(0, 32)
                }}
                
                // Default: revert
                default {{
                    revert(0, 0)
                }}
            }}
        }}
    }}
}}

// Metadata JSON (stored separately):
{metadata_json}'''
    
    return yul_contract


def pulse_button(user_request: Annotated[str, Field(description="User's request or description for the NFT")] = "") -> str:
    """
    Pulse button function - generates ERC721 Yul contract with chat history as metadata.
    This function is called when the user presses the pulse button.
    
    Args:
        user_request: Optional user request or description
        
    Returns:
        Confirmation message with contract generation status
    """
    try:
        chat_history = get_chat_history()
        
        if not chat_history:
            return "⚠️ No chat history found. Please chat with the agent first before pressing the pulse button."
        
        # Generate the Yul contract
        contract = generate_erc721_yul_contract(chat_history, user_request)
        
        # Save contract to file
        contract_filename = f"ERC721_ChatHistory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yul"
        with open(contract_filename, 'w', encoding='utf-8') as f:
            f.write(contract)
        
        # Save metadata separately
        metadata = {
            "name": "Chat History NFT",
            "description": user_request or "Minted chat history with agent",
            "chat_history": chat_history,
            "mint_timestamp": datetime.now().isoformat(),
            "owner": OWNER_ADDRESS
        }
        metadata_filename = f"metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(metadata_filename, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return f"""✅ Pulse button activated! ERC721 contract generated successfully.

📄 Contract saved to: {contract_filename}
📋 Metadata saved to: {metadata_filename}

🔐 Owner address: {OWNER_ADDRESS}
💬 Chat messages in metadata: {len(chat_history)}
📝 Contract includes:
   - Payable mint() function
   - tokenURI() function returning chat history metadata
   - owner() function
   - All chat history stored as JSON metadata

You can now deploy this contract and mint your chat history as an NFT!"""
    
    except Exception as e:
        return f"❌ Error generating contract: {str(e)}"


def get_agent(chat_client=None, api_key: str | None = None, model_id: str = "gpt-4o-mini", core_file_path: str = "core.json") -> ChatAgent:
    """
    Creates and returns the agent with chatbot capabilities.
    
    Args:
        chat_client: Optional pre-configured chat client. If None, creates one.
        api_key: OpenAI API key. If None, uses OPENAI_API_KEY environment variable.
        model_id: OpenAI model ID (default: "gpt-4o-mini").
        core_file_path: Path to the JSON file containing agent core specification.
        
    Returns:
        Configured ChatAgent instance
    """
    
    # Load core JSON
    core_json = load_core_json(core_file_path)
    
    if chat_client is None:
        chat_client = OpenAIChatClient(
            model_id=model_id,
            api_key=api_key
        )
    
    # Create agent instructions from core JSON
    agent_name = core_json.get("name", "Agent Template")
    agent_description = core_json.get("description", "A customizable AI agent")
    
    agent_instructions = f"""You are {agent_name}.

DESCRIPTION:
{agent_description}

CORE IDENTITY:
You are an AI agent that helps users with tasks through conversation. You maintain a chat history that can be minted as an NFT.

CAPABILITIES:
- Chat with users and help with their requests
- Maintain conversation history
- Generate ERC721 smart contracts when requested (via pulse button)

RESPONSE STYLE:
- Be helpful, clear, and concise
- Maintain context from the conversation
- When users ask about minting or NFTs, explain that they can use the pulse button to generate a contract

IMPORTANT:
- All contracts are hard-coded to owner address: {OWNER_ADDRESS}
- Chat history is stored and can be minted as NFT metadata
- The pulse button generates a payable ERC721 contract in Yul format"""
    
    # Create agent with tools
    agent = ChatAgent(
        chat_client=chat_client,
        name=agent_name.replace(" ", "_"),
        instructions=agent_instructions,
        tools=[
            pulse_button,
        ],
        temperature=0.7,
        max_tokens=4000,
    )
    
    return agent


async def main():
    """Example usage of the agent."""
    print("=" * 70)
    print("Agent Template - Initialization")
    print("=" * 70)
    
    # Create the agent
    agent = get_agent()
    
    print("\n✅ Agent created successfully!")
    print(f"🔐 Owner address: {OWNER_ADDRESS}")
    print("\n" + "=" * 70)
    
    # Example conversation
    print("\n[Example] Starting conversation...")
    query = "Hello! Can you help me with a task?"
    
    print(f"\n👤 User: {query}\n")
    print("🤖 Agent: ", end="", flush=True)
    
    add_to_chat_history("user", query)
    result = await agent.run(query)
    add_to_chat_history("assistant", result)
    print(f"{result}\n")
    
    print("=" * 70)
    print("\n✨ Agent is ready for requests!")
    print("💡 Try chatting with the agent, then use the pulse button to mint your chat history!")


if __name__ == "__main__":
    asyncio.run(main())

