# AI API Providers Guide

This agent template supports multiple AI providers. Choose the one that best fits your needs.

## Supported Providers

### 1. OpenAI (Default)
- **Models**: gpt-4o-mini, gpt-4o, gpt-4-turbo, gpt-4, gpt-3.5-turbo
- **Best for**: General purpose, cost-effective (gpt-4o-mini)
- **Setup**: Requires OpenAI API key

### 2. Anthropic (Claude)
- **Models**: claude-3-5-sonnet-20241022, claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307
- **Best for**: Long context, detailed analysis, creative writing
- **Setup**: Requires Anthropic API key

### 3. Azure OpenAI
- **Models**: Same as OpenAI (gpt-4o-mini, gpt-4o, gpt-4-turbo, etc.)
- **Best for**: Enterprise deployments, compliance requirements
- **Setup**: Requires Azure OpenAI endpoint, API key, and API version

## Configuration Methods

### Method 1: Web UI (Recommended)

1. Launch the UI: `python run_ui.py`
2. Select your provider from the dropdown
3. Enter your API key
4. For Azure: Enter endpoint and API version
5. Select your model
6. Click "Initialize Agent"

### Method 2: Environment Variables

#### OpenAI
```bash
export AI_PROVIDER="openai"
export OPENAI_API_KEY="sk-..."
export OPENAI_CHAT_MODEL_ID="gpt-4o-mini"
```

#### Anthropic
```bash
export AI_PROVIDER="anthropic"
export ANTHROPIC_API_KEY="sk-ant-..."
export ANTHROPIC_CHAT_MODEL_ID="claude-3-5-sonnet-20241022"
```

#### Azure OpenAI
```bash
export AI_PROVIDER="azure"
export AZURE_OPENAI_API_KEY="your-azure-key"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_API_VERSION="2024-02-15-preview"
export OPENAI_CHAT_MODEL_ID="gpt-4o-mini"
```

### Method 3: Python Code

```python
from agent import get_agent

# OpenAI
agent = get_agent(
    api_key="sk-...",
    model_id="gpt-4o-mini",
    provider="openai"
)

# Anthropic
agent = get_agent(
    api_key="sk-ant-...",
    model_id="claude-3-5-sonnet-20241022",
    provider="anthropic"
)

# Azure OpenAI
agent = get_agent(
    api_key="your-azure-key",
    model_id="gpt-4o-mini",
    provider="azure",
    azure_endpoint="https://your-resource.openai.azure.com/",
    api_version="2024-02-15-preview"
)
```

## Provider Comparison

| Feature | OpenAI | Anthropic | Azure OpenAI |
|---------|--------|----------|-------------|
| Cost (cheapest) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Context Length | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Enterprise Features | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Ease of Setup | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

## Getting API Keys

### OpenAI
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy the key (starts with `sk-`)

### Anthropic
1. Go to https://console.anthropic.com/
2. Navigate to API Keys
3. Create a new key
4. Copy the key (starts with `sk-ant-`)

### Azure OpenAI
1. Create an Azure OpenAI resource in Azure Portal
2. Go to "Keys and Endpoint"
3. Copy the endpoint URL and API key
4. Note the API version (usually `2024-02-15-preview`)

## Model Recommendations

### For Cost-Conscious Users
- **OpenAI**: `gpt-4o-mini` (cheapest, fast)
- **Anthropic**: `claude-3-haiku-20240307` (fast, cost-effective)

### For Best Quality
- **OpenAI**: `gpt-4o` (best balance)
- **Anthropic**: `claude-3-5-sonnet-20241022` (excellent reasoning)

### For Long Context
- **Anthropic**: `claude-3-opus-20240229` (200k tokens)
- **OpenAI**: `gpt-4-turbo` (128k tokens)

## Troubleshooting

### "Provider not supported"
- Make sure you're using a supported provider: `openai`, `anthropic`, or `azure`
- Check spelling (case-insensitive)

### "API key required"
- Verify your API key is correct
- Check environment variables are set
- For Azure, ensure endpoint is also set

### "ImportError: Anthropic support not available"
```bash
pip install anthropic
```

### Azure Connection Issues
- Verify endpoint URL is correct (should end with `/`)
- Check API version matches your Azure resource
- Ensure your IP is whitelisted (if required)

## Switching Providers

You can switch providers anytime:
1. In UI: Change provider dropdown and re-initialize
2. Via environment: Change `AI_PROVIDER` and restart
3. In code: Call `get_agent()` with different `provider` parameter

All chat history is preserved when switching providers!

