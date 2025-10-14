# AI Agent with Web Search

A simple AI chatbot agent that can search the web and remember conversation history.

## What it does

- **AI Chat**: Uses Groq or OpenRouter LLM providers for conversations
- **Web Search**: Built-in DuckDuckGo search (no API key needed)
- **Memory**: Remembers last 6 conversations in the session
- **Environment Config**: Uses `.env` file for API keys and settings

## Features

- Chat with AI assistant
- Ask questions that require web search
- Conversation memory during session
- Support for Groq (free tier) or OpenRouter API
- No database needed - memory resets when you restart

## Installation

1. **Clone/Download** this project
2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install requirements**:
   ```bash
   pip install langchain langchain-community langchain-groq langchain-openai pydantic-settings
   ```

5. **Setup API Key**:
   - Get free API key from [Groq](https://console.groq.com/keys)
   - Add your key to `.env` file:
   ```
   GROQ_API_KEY="your-api-key-here"
   GROQ_LLM_MODEL="llama3-8b-8192"
   TEMPERATURE=0.7
   ```

## Usage

1. Activate virtual environment
2. Run: `python agent.py`
3. Start chatting!
4. Type `exit` to quit

## Example

```
You: What's the weather like in Tokyo today?
Agent: [Searches web and provides current weather information]

You: Tell me more about Japanese culture
Agent: [Remembers context and provides detailed response]
```

## Files

- `agent.py` - Main chatbot code
- `setting.py` - Configuration management with Pydantic
- `.env` - Environment variables (API keys)
