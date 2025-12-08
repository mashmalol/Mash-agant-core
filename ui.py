"""
Streamlit Web UI for Agent Chatbot
Allows users to input their API key and chat with the agent through a web interface.
"""

import streamlit as st
import asyncio
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agent import (
    get_agent,
    add_to_chat_history,
    get_chat_history,
    clear_chat_history,
    pulse_button,
    get_owner_address,
    load_core_json
)

# Page configuration
st.set_page_config(
    page_title="Agent Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #f5f5f5;
        margin-right: 20%;
    }
    .stButton>button {
        width: 100%;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = None
if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = False
if "chat_history_loaded" not in st.session_state:
    st.session_state.chat_history_loaded = False
if "provider" not in st.session_state:
    st.session_state.provider = "openai"
if "model_id" not in st.session_state:
    st.session_state.model_id = "gpt-4o-mini"

def load_chat_history_to_session():
    """Load chat history from agent module to session state."""
    if not st.session_state.chat_history_loaded:
        history = get_chat_history()
        st.session_state.messages = []
        for msg in history:
            role = "user" if msg["role"] == "user" else "assistant"
            st.session_state.messages.append({
                "role": role,
                "content": msg["content"]
            })
        st.session_state.chat_history_loaded = True

def initialize_agent(api_key: str, model_id: str = "gpt-4o-mini", provider: str = "openai", **kwargs):
    """Initialize the agent with the provided API key and provider."""
    try:
        agent = get_agent(api_key=api_key, model_id=model_id, provider=provider, **kwargs)
        st.session_state.agent = agent
        st.session_state.api_key_set = True
        st.session_state.provider = provider
        st.session_state.model_id = model_id
        return True
    except Exception as e:
        st.error(f"Error initializing agent: {str(e)}")
        return False

def get_models_for_provider(provider: str) -> list:
    """Get available models for a provider."""
    models = {
        "openai": ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"],
        "anthropic": ["claude-3-5-sonnet-20241022", "claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"],
        "azure": ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"]  # Azure uses OpenAI models
    }
    return models.get(provider.lower(), models["openai"])

# Sidebar for API key and settings
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Provider selection
    st.subheader("🤖 AI Provider")
    provider = st.selectbox(
        "Select AI Provider",
        ["openai", "anthropic", "azure"],
        index=0,
        help="Choose your AI provider"
    )
    
    # Provider-specific settings
    provider_config = {}
    
    if provider == "azure":
        st.info("💡 Azure OpenAI requires endpoint and API version")
        azure_endpoint = st.text_input(
            "Azure Endpoint",
            value=os.environ.get("AZURE_OPENAI_ENDPOINT", ""),
            placeholder="https://your-resource.openai.azure.com/",
            help="Your Azure OpenAI endpoint URL"
        )
        api_version = st.text_input(
            "API Version",
            value=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            help="Azure OpenAI API version"
        )
        if azure_endpoint:
            provider_config["azure_endpoint"] = azure_endpoint
        if api_version:
            provider_config["api_version"] = api_version
    
    # API Key Input
    st.subheader("🔑 API Key")
    api_key_placeholder = {
        "openai": "sk-...",
        "anthropic": "sk-ant-...",
        "azure": "Azure API key"
    }.get(provider, "API key...")
    
    api_key_env_var = {
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "azure": "AZURE_OPENAI_API_KEY"
    }.get(provider, "OPENAI_API_KEY")
    
    api_key = st.text_input(
        f"Enter your {provider.upper()} API Key",
        type="password",
        placeholder=api_key_placeholder,
        value=os.environ.get(api_key_env_var, ""),
        help=f"Enter your {provider.upper()} API key. Can also set {api_key_env_var} environment variable."
    )
    
    # Model selection based on provider
    available_models = get_models_for_provider(provider)
    default_model = available_models[0]
    
    # Try to get saved model or use default
    current_model = st.session_state.get("model_id", default_model)
    if current_model not in available_models:
        current_model = default_model
    
    model_index = available_models.index(current_model) if current_model in available_models else 0
    
    model_id = st.selectbox(
        "Select Model",
        available_models,
        index=model_index,
        help=f"Choose the {provider.upper()} model to use"
    )
    
    # Initialize button
    if st.button("🚀 Initialize Agent", use_container_width=True):
        if api_key:
            with st.spinner(f"Initializing {provider.upper()} agent..."):
                if initialize_agent(api_key, model_id, provider, **provider_config):
                    st.success(f"✅ {provider.upper()} Agent initialized successfully!")
                    st.rerun()
        else:
            st.warning(f"⚠️ Please enter your {provider.upper()} API key first")
    
    # Status
    st.divider()
    st.subheader("📊 Status")
    if st.session_state.api_key_set:
        st.success("✅ Agent Ready")
        current_provider = st.session_state.get("provider", "openai")
        current_model = st.session_state.get("model_id", model_id)
        st.info(f"🤖 Provider: {current_provider.upper()}")
        st.info(f"📝 Model: {current_model}")
    else:
        st.warning("⚠️ Agent Not Initialized")
    
    # Owner address configuration
    st.divider()
    st.subheader("🔐 Contract Owner Address")
    
    # Get current owner address
    current_owner = get_owner_address()
    
    owner_address = st.text_input(
        "ERC721 Owner Address",
        value=current_owner if current_owner else "",
        placeholder="0x...",
        help="Set the owner address for generated ERC721 contracts. Can be set in core.json or here."
    )
    
    if owner_address and owner_address != current_owner:
        # Save to core.json
        try:
            core_json = load_core_json()
            core_json["owner"] = owner_address
            with open("core.json", 'w', encoding='utf-8') as f:
                json.dump(core_json, f, indent=2)
            st.success("✅ Owner address saved to core.json")
            st.rerun()
        except Exception as e:
            st.error(f"Error saving owner address: {e}")
    
    if current_owner:
        st.code(current_owner, language=None)
        st.caption("Owner address for ERC721 contracts")
    else:
        st.warning("⚠️ Owner address not set. Set it above before generating contracts.")
    
    # Actions
    st.divider()
    st.subheader("🛠️ Actions")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        clear_chat_history()
        st.session_state.messages = []
        st.session_state.chat_history_loaded = False
        st.success("Chat history cleared!")
        st.rerun()
    
    # Pulse button
    if st.button("🔘 Generate ERC721 Contract", use_container_width=True, type="primary"):
        if st.session_state.api_key_set:
            # Get owner address
            owner_addr = get_owner_address()
            if not owner_addr:
                st.error("⚠️ Please set the owner address above before generating contracts.")
            else:
                with st.spinner("Generating ERC721 contract..."):
                    result = pulse_button(owner_address=owner_addr)
                    st.success("✅ Contract generated!")
                    st.info(result)
        else:
            st.warning("⚠️ Please initialize the agent first")

# Main content area
st.markdown('<div class="main-header">🤖 Agent Chatbot</div>', unsafe_allow_html=True)

# Load chat history if agent is initialized
if st.session_state.api_key_set:
    load_chat_history_to_session()

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if st.session_state.api_key_set:
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        add_to_chat_history("user", prompt)
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Run agent asynchronously
                    # Handle event loop for Streamlit compatibility
                    try:
                        loop = asyncio.get_event_loop()
                        if loop.is_running():
                            # Use nest_asyncio if loop is already running
                            import nest_asyncio
                            nest_asyncio.apply()
                            response = asyncio.run(st.session_state.agent.run(prompt))
                        else:
                            response = loop.run_until_complete(
                                st.session_state.agent.run(prompt)
                            )
                    except RuntimeError:
                        # No event loop exists, create one
                        response = asyncio.run(st.session_state.agent.run(prompt))
                    
                    st.markdown(response)
                    
                    # Add assistant response to chat
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    add_to_chat_history("assistant", response)
                    
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
else:
    st.info("👆 Please enter your API key in the sidebar and click 'Initialize Agent' to start chatting.")

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption(f"💬 Messages: {len(st.session_state.messages)}")
with col2:
    if st.session_state.api_key_set:
        st.caption("✅ Agent Active")
    else:
        st.caption("⚠️ Agent Inactive")
with col3:
    owner_addr = get_owner_address()
    if owner_addr:
        st.caption(f"🔐 Owner: {owner_addr[:10]}...")
    else:
        st.caption("🔐 Owner: Not set")

