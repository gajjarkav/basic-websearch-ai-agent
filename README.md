# 🤖 AI Agent with Web Search & Weather Tools

An intelligent AI chatbot agent powered by LangChain that can search the web, provide weather information, and maintain conversation memory.

---

## 📋 Overview

This project provides a ReAct agent that can:
- **Chat intelligently** using Groq or OpenRouter LLMs
- **Search the web** using DuckDuckGo (no API key required)
- **Get weather information** from OpenWeatherMap
- **Remember conversation context** during the session
- **Handle multiple tools** dynamically

---

## ✨ Key Features

| Feature | Details |
|---------|---------|
| **LLM Support** | Groq (free) or OpenRouter - choose your provider |
| **Web Search** | DuckDuckGo integration - no API key needed |
| **Weather Tool** | Real-time weather data from OpenWeatherMap |
| **Conversation Memory** | Remembers last 6 exchanges in session |
| **ReAct Agent** | Intelligent reasoning and action loop |
| **Easy Config** | All settings via `.env` file |

---

## 🚀 Quick Start

### 1️⃣ Prerequisites
- Python 3.8 or higher
- An API key from [Groq](https://console.groq.com/keys) (free) or [OpenRouter](https://openrouter.ai)
- (Optional) OpenWeatherMap API key for weather tool

### 2️⃣ Installation

```bash
# Clone or download the project
cd basic-websearch-ai-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configuration

Create a `.env` file in the project root:

```env
# Choose ONE LLM provider:
# Option 1: Groq (Free)
GROQ_API_KEY=your-groq-api-key-here
GROQ_LLM_MODEL=llama3-8b-8192

# Option 2: OpenRouter
# OPENROUTER_API_KEY=your-openrouter-api-key-here
# OPENROUTER_LLM_MODEL=openai/gpt-3.5-turbo

# Optional: Weather tool
OPENWEATHER_API_KEY=your-openweather-api-key-here

# Model settings
TEMPERATURE=0.7
```

### 4️⃣ Run the Agent

```bash
python agent.py
```

---

## 💬 Usage Examples

```
🤖 Agent is ready! Type 'exit' to end the chat.

You: What's the current weather in New York?
Agent: The current weather in New York is partly cloudy. 
       The temperature is 18°C, but it feels like 15°C. 
       Humidity is at 65%, and the wind speed is 8 m/s.

You: Search for latest AI news
Agent: [Searches web and provides recent AI news articles]

You: Remember what I asked about weather?
Agent: [Uses memory to provide context-aware response]

You: exit
👋 Goodbye!
```

---

## 📁 Project Structure

```
basic-websearch-ai-agent/
├── agent.py              # Main agent execution
├── setting.py            # Pydantic configuration management
├── time_tool.py          # Get current time tool
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore rules
├── weather/
│   ├── logic.py          # Weather API integration
│   └── schema.py         # Input validation schema
└── README.md             # This file
```

---

## 🛠️ Tools Available

### 1. **Web Search Tool**
- Provider: DuckDuckGo
- No API key needed
- Returns recent web search results

### 2. **Weather Tool**
- Provider: OpenWeatherMap
- Requires: API key
- Returns: Temperature, humidity, wind speed, description

### 3. **Time Tool**
- Gets current date and time
- Useful for time-sensitive queries

---

## 🔧 Configuration Details

### LLM Providers

| Provider | Free Tier | Speed | Best For |
|----------|-----------|-------|----------|
| **Groq** | ✅ Yes | ⚡ Very Fast | Best choice for beginners |
| **OpenRouter** | ✅ Limited | 🔄 Variable | Multiple model options |

### Environment Variables Explained

```
GROQ_API_KEY              # Your Groq API key
GROQ_LLM_MODEL            # Model name (e.g., llama3-8b-8192)
OPENROUTER_API_KEY        # Alternative to Groq
OPENROUTER_LLM_MODEL      # Model name for OpenRouter
OPENWEATHER_API_KEY       # Optional - for weather tool
TEMPERATURE               # 0.0 (deterministic) to 1.0 (creative)
```

---

## 🎯 How It Works

1. **User Input** → You type a question
2. **Agent Reasoning** → Agent decides which tool(s) to use
3. **Tool Execution** → Calls web search, weather, or time tool
4. **Response Generation** → LLM creates intelligent response
5. **Memory Update** → Stores conversation for context
6. **Output** → Agent responds to you

---

## 📝 Example Queries

- "What's the weather in London?"
- "Search for machine learning tutorials"
- "What time is it now?"
- "What are the latest technology trends?"
- "Tell me about climate change" (searches web + provides info)

---

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "No API key found" | Check `.env` file has GROQ_API_KEY or OPENROUTER_API_KEY |
| Weather tool fails | Ensure OPENWEATHER_API_KEY is set in `.env` |
| Slow responses | Check internet connection or LLM provider status |
| Memory errors | Restart the agent (memory resets between sessions) |

---

## 🔐 Security Notes

- ✅ Never commit `.env` file to git (already in `.gitignore`)
- ✅ Keep API keys private
- ✅ Don't share `.env` file
- ✅ Use read-only API keys if provider allows

---

## 📚 Dependencies

Key libraries used:
- **LangChain** - Agent framework
- **Groq/OpenAI** - LLM providers
- **DuckDuckGo** - Web search
- **Pydantic** - Configuration & validation
- **Requests** - HTTP library

---

## 🤝 Contributing

Feel free to:
- Add new tools (calculator, code executor, etc.)
- Switch LLM providers
- Improve prompts
- Add persistent memory/database

---

## 📄 License

This project is open source. Use freely!

---

## 💡 Tips

1. **Free Usage**: Use Groq API (completely free with good limits)
2. **Customize**: Modify `setting.py` to add new environment variables
3. **Extend**: Add more tools in `agent.py` tools list
4. **Debug**: Set `verbose=True` in `AgentExecutor` to see agent reasoning

---

**Last Updated**: October 2025 | **Status**: Active Development
