# Web UI Quick Start Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `agent-framework` - Agent framework
- `streamlit` - Web UI framework
- Other dependencies

### 2. Launch the UI
```bash
python run_ui.py
```

Or directly:
```bash
streamlit run ui.py
```

### 3. Use the UI

1. **The web browser will open automatically** (usually at http://localhost:8501)
2. **In the sidebar**, paste your OpenAI API key
3. **Select your model** (default: gpt-4o-mini)
4. **Click "Initialize Agent"**
5. **Start chatting!**

## 🎯 Features

### Sidebar Controls
- **API Key Input** - Paste your OpenAI API key (password field for security)
- **Model Selection** - Choose between gpt-4o-mini, gpt-4o, gpt-4, or gpt-3.5-turbo
- **Initialize Button** - Start the agent with your API key
- **Status Display** - See if agent is ready
- **Contract Owner Address** - Set and view the owner address for ERC721 contracts
- **Clear History** - Clear all chat messages
- **Pulse Button** - Generate ERC721 contract with chat history

### Main Chat Area
- **Real-time chat** with the agent
- **Message history** displayed in chat bubbles
- **Streaming responses** (when available)
- **Chat input** at the bottom

## 💡 Tips

- Your API key is stored only in the browser session (not saved to disk)
- Refresh the page to reset the session
- The pulse button generates contracts in the current directory
- Chat history is maintained during the session

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### UI doesn't open automatically
- Manually open: http://localhost:8501
- Check if port 8501 is available

### Agent initialization fails
- Check your API key is correct
- Make sure you have credits in your OpenAI account
- Try a different model (gpt-4o-mini is cheapest)

## 📱 Access from Other Devices

To access the UI from other devices on your network:
```bash
streamlit run ui.py --server.address 0.0.0.0
```

Then access via: `http://YOUR_IP:8501`

