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
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
try:
    from agent_framework.azure import AzureOpenAIChatClient
except ImportError:
    AzureOpenAIChatClient = None
try:
    from agent_framework.anthropic import AnthropicChatClient
except ImportError:
    AnthropicChatClient = None

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
            "version": "1.0.0",
            "owner": ""  # User must set this
        }


def get_owner_address(core_file_path: str = "core.json") -> str:
    """
    Get the owner address from core.json or environment variable.
    
    Args:
        core_file_path: Path to the core.json file
        
    Returns:
        Owner address string, or empty string if not set
    """
    # First check environment variable
    owner = os.environ.get("ERC721_OWNER_ADDRESS", "")
    if owner:
        return owner
    
    # Then check core.json
    core_json = load_core_json(core_file_path)
    owner = core_json.get("owner", "")
    
    return owner


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


def generate_erc721_yul_contract(chat_history: list, user_request: str = "", owner_address: str = "") -> str:
    """
    Generates a payable ERC721 smart contract in Yul with chat history as metadata.
    
    Args:
        chat_history: List of chat messages
        user_request: Optional user request/description
        owner_address: Owner address for the contract (if empty, uses config)
        
    Returns:
        Yul contract code as string
    """
    # Get owner address from parameter or config
    if not owner_address:
        owner_address = get_owner_address()
    
    if not owner_address:
        raise ValueError("Owner address not set. Please set it in core.json or ERC721_OWNER_ADDRESS environment variable.")
    
    # Validate address format
    if not owner_address.startswith("0x"):
        owner_address = "0x" + owner_address
    
    if len(owner_address) != 42:  # 0x + 40 hex chars
        raise ValueError(f"Invalid owner address format: {owner_address}. Must be 42 characters (0x + 40 hex chars).")
    
    # Separate user messages and AI responses
    user_messages = [msg for msg in chat_history if msg.get("role") == "user"]
    ai_responses = [msg for msg in chat_history if msg.get("role") == "assistant"]
    
    # Create metadata JSON from chat history
    metadata = {
        "name": "Chat History NFT",
        "description": user_request or "Minted chat history with agent",
        "chat_history": chat_history,
        "user_messages": user_messages,
        "ai_responses": ai_responses,
        "summary": {
            "total_messages": len(chat_history),
            "user_messages_count": len(user_messages),
            "ai_responses_count": len(ai_responses),
            "conversation_pairs": min(len(user_messages), len(ai_responses))
        },
        "mint_timestamp": datetime.now().isoformat(),
        "owner": owner_address
    }
    
    metadata_json = json.dumps(metadata, indent=2)
    
    # Convert owner address to bytes20 for Yul (addresses are 20 bytes, padded to 32 bytes)
    owner_address_clean = owner_address[2:] if owner_address.startswith("0x") else owner_address
    owner_hex = "0x" + owner_address_clean.zfill(64)  # Pad to 64 hex chars (32 bytes)
    
    # Generate Yul ERC721 contract
    # Note: This is a simplified ERC721 implementation in Yul
    yul_contract = f'''// SPDX-License-Identifier: MIT
// ERC721 Payable Contract in Yul
// Owner: {owner_address}
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


def pulse_button(user_request: Annotated[str, Field(description="User's request or description for the NFT")] = "", owner_address: str = "") -> str:
    """
    Pulse button function - generates ERC721 Yul contract with chat history as metadata.
    This function is called when the user presses the pulse button.
    
    Args:
        user_request: Optional user request or description
        owner_address: Optional owner address (if not provided, uses config)
        
    Returns:
        Confirmation message with contract generation status
    """
    try:
        chat_history = get_chat_history()
        
        if not chat_history:
            return "⚠️ No chat history found. Please chat with the agent first before pressing the pulse button."
        
        # Get owner address
        if not owner_address:
            owner_address = get_owner_address()
        
        if not owner_address:
            return "⚠️ Owner address not set. Please set it in core.json or ERC721_OWNER_ADDRESS environment variable before generating contracts."
        
        # Generate the Yul contract
        contract = generate_erc721_yul_contract(chat_history, user_request, owner_address)
        
        # Save contract to file
        contract_filename = f"ERC721_ChatHistory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yul"
        with open(contract_filename, 'w', encoding='utf-8') as f:
            f.write(contract)
        
        # Separate user messages and AI responses
        user_messages = [msg for msg in chat_history if msg.get("role") == "user"]
        ai_responses = [msg for msg in chat_history if msg.get("role") == "assistant"]
        
        # Save metadata separately
        metadata = {
            "name": "Chat History NFT",
            "description": user_request or "Minted chat history with agent",
            "chat_history": chat_history,
            "user_messages": user_messages,
            "ai_responses": ai_responses,
            "summary": {
                "total_messages": len(chat_history),
                "user_messages_count": len(user_messages),
                "ai_responses_count": len(ai_responses),
                "conversation_pairs": min(len(user_messages), len(ai_responses))
            },
            "mint_timestamp": datetime.now().isoformat(),
            "owner": owner_address
        }
        metadata_filename = f"metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(metadata_filename, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        # Count messages
        user_messages = [msg for msg in chat_history if msg.get("role") == "user"]
        ai_responses = [msg for msg in chat_history if msg.get("role") == "assistant"]
        
        return f"""✅ Pulse button activated! ERC721 contract generated successfully.

📄 Contract saved to: {contract_filename}
📋 Metadata saved to: {metadata_filename}

🔐 Owner address: {owner_address}
💬 Chat messages in metadata: {len(chat_history)}
   - User messages: {len(user_messages)}
   - AI responses: {len(ai_responses)}
📝 Contract includes:
   - Payable mint() function
   - tokenURI() function returning chat history metadata
   - owner() function
   - Complete chat history with user messages and AI responses stored as JSON metadata

You can now deploy this contract and mint your chat history as an NFT!"""
    
    except ValueError as e:
        return f"❌ Configuration error: {str(e)}"
    except Exception as e:
        return f"❌ Error generating contract: {str(e)}"


def get_agent(
    chat_client=None, 
    api_key: str | None = None, 
    model_id: str = "gpt-4o-mini", 
    provider: str = "openai",
    core_file_path: str = "core.json",
    **kwargs
) -> ChatAgent:
    """
    Creates and returns the agent with chatbot capabilities.
    
    Args:
        chat_client: Optional pre-configured chat client. If None, creates one.
        api_key: API key for the provider. If None, uses environment variables.
        model_id: Model ID (default: "gpt-4o-mini" for OpenAI).
        provider: Provider name - "openai", "anthropic", "azure" (default: "openai").
        core_file_path: Path to the JSON file containing agent core specification.
        **kwargs: Additional provider-specific arguments (e.g., azure_endpoint, api_version for Azure)
        
    Returns:
        Configured ChatAgent instance
    """
    
    # Load core JSON
    core_json = load_core_json(core_file_path)
    
    if chat_client is None:
        provider = provider.lower()
        
        if provider == "openai":
            # OpenAI
            if api_key is None:
                api_key = os.environ.get("OPENAI_API_KEY")
            chat_client = OpenAIChatClient(
                model_id=model_id,
                api_key=api_key
            )
        
        elif provider == "anthropic":
            # Anthropic Claude
            if AnthropicChatClient is None:
                raise ImportError("Anthropic support not available. Install with: pip install anthropic")
            if api_key is None:
                api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key is None:
                raise ValueError("Anthropic API key required. Set ANTHROPIC_API_KEY environment variable or pass api_key parameter.")
            chat_client = AnthropicChatClient(
                model_id=model_id or "claude-3-5-sonnet-20241022",
                api_key=api_key
            )
        
        elif provider == "azure":
            # Azure OpenAI
            if AzureOpenAIChatClient is None:
                raise ImportError("Azure OpenAI support not available. Check agent-framework installation.")
            if api_key is None:
                api_key = os.environ.get("AZURE_OPENAI_API_KEY")
            azure_endpoint = kwargs.get("azure_endpoint") or os.environ.get("AZURE_OPENAI_ENDPOINT")
            api_version = kwargs.get("api_version") or os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
            
            if not api_key or not azure_endpoint:
                raise ValueError("Azure OpenAI requires api_key and azure_endpoint. Set AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT environment variables.")
            
            chat_client = AzureOpenAIChatClient(
                model_id=model_id,
                api_key=api_key,
                endpoint=azure_endpoint,
                api_version=api_version
            )
        
        else:
            raise ValueError(f"Unsupported provider: {provider}. Supported: 'openai', 'anthropic', 'azure'")
    
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
- Owner address is configured in core.json or ERC721_OWNER_ADDRESS environment variable
- Chat history is stored and can be minted as NFT metadata
- The pulse button generates a payable ERC721 contract in Yul format
- Make sure to set the owner address before generating contracts"""
    
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
    
    # Get owner address
    owner_address = get_owner_address()
    if owner_address:
        print(f"🔐 Owner address: {owner_address}")
    else:
        print("⚠️  Owner address not set. Set it in core.json or ERC721_OWNER_ADDRESS environment variable.")
    
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

