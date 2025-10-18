# Basic Web Search AI Agent

A conversational AI agent built with LangChain that can search the web, check weather, tell time, and maintain conversation context.

## 🎯 What This Project Does

This is an intelligent chatbot that combines:
- **LLM-powered conversations** using Groq or OpenRouter
- **Web search capability** via DuckDuckGo (no API key required)
- **Weather information** from OpenWeatherMap API
- **Time queries** with timezone support
- **Conversation memory** that remembers recent interactions

## ✨ Key Features

1. **Multiple AI Provider Support**
   - Groq API (free tier available)
   - OpenRouter API
   - Only one provider needed to run

2. **Built-in Tools**
   - Web search (DuckDuckGo - free, no API key)
   - Weather information (requires OpenWeatherMap API key)
   - Current time with timezone support
   - Extensible architecture for adding custom tools

3. **Smart Memory**
   - Remembers last 6 conversation turns
   - Maintains context within session
   - Resets on restart (no persistent storage)

4. **Easy Configuration**
   - Environment-based settings via `.env` file
   - Pydantic-powered configuration management
   - Configurable LLM model and temperature

## 📋 Use Cases

- Ask questions that require real-time web information
- Get current weather for any city
- Check time in different timezones
- Have contextual conversations with memory
- Build and test custom LangChain tools

## 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- API key from Groq (free) or OpenRouter
- OpenWeatherMap API key (optional, for weather feature)

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/gajjarkav/basic-websearch-ai-agent.git
cd basic-websearch-ai-agent
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Step 1: Create Environment File
Copy the example environment file:
```bash
cp .env.example .env
```

### Step 2: Add API Keys
Edit `.env` file with your API keys:

```env
# Required: Choose ONE LLM provider
GROQ_API_KEY="your-groq-api-key"
GROQ_LLM_MODEL="llama-3.3-70b-versatile"

# OR use OpenRouter instead
OPENROUTER_API_KEY="your-openrouter-api-key"
OPENROUTER_LLM_MODEL="mistralai/mistral-7b-instruct"

# LLM Configuration
TEMPERATURE=1.0

# Optional: For weather feature
OPENWEATHER_API_KEY="your-openweather-api-key"
```

### Step 3: Get API Keys

**Groq API (Recommended - Free Tier):**
1. Visit [https://console.groq.com/keys](https://console.groq.com/keys)
2. Sign up and get your free API key
3. Add to `.env` file

**OpenWeatherMap API (Optional):**
1. Visit [https://openweathermap.org/api](https://openweathermap.org/api)
2. Sign up for free tier
3. Get API key from your account
4. Add to `.env` file

## 🚀 Usage

### Start the Agent
```bash
python agent.py
```

### Chat with the Agent
Once running, you can:
- Ask questions
- Request web searches
- Check weather
- Get current time
- Have contextual conversations

### Exit the Agent
Type `exit` to quit the program.

## 💬 Example Interactions

**Web Search:**
```
You: What are the latest developments in AI?
Agent: [Searches web and provides current information]
```

**Weather Check:**
```
You: What's the weather in Tokyo?
Agent: The current weather in Tokyo is clear sky. The temperature is 22°C...
```

**Time Query:**
```
You: What time is it in New York?
Agent: Tuesday January 21, 2025 03:45:30 PM (EST)
```

**Contextual Conversation:**
```
You: Tell me about Python programming
Agent: [Provides information about Python]

You: What are its main use cases?
Agent: [Remembers context and answers about Python's use cases]
```

## 📁 Project Structure

```
basic-websearch-ai-agent/
├── agent.py              # Main agent implementation
├── setting.py            # Configuration with Pydantic
├── time_tool.py          # Custom tool for time queries
├── weather/              # Weather tool module
│   ├── logic.py         # Weather API logic
│   └── schema.py        # Pydantic schema for weather
├── requirements.txt      # Python dependencies
├── .env.example         # Example environment file
└── README.md            # This file
```

## 🛠️ Available Tools

1. **DuckDuckGo Search**
   - Free web search
   - No API key required
   - Returns recent web information

2. **Weather Tool**
   - Get current weather for any city
   - Temperature, humidity, wind speed
   - Requires OpenWeatherMap API key

3. **Time Tool**
   - Get current time in any timezone
   - Fallback to local system time
   - Timezone-aware queries

## 🔍 How It Works

This agent uses the **ReAct (Reasoning + Acting)** pattern:
1. User asks a question
2. Agent reasons about which tool to use
3. Agent executes the tool
4. Agent processes results and responds
5. Conversation history is maintained for context

## ⚠️ Troubleshooting

**"No API key found" error:**
- Ensure `.env` file exists in project root
- Check that you've added either GROQ_API_KEY or OPENROUTER_API_KEY
- Verify there are no typos in the key names

**Weather tool not working:**
- Verify OPENWEATHER_API_KEY is set in `.env`
- Check that the city name is spelled correctly
- Ensure your API key is valid and active

**Import errors:**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again
- Verify Python version is 3.8+

**Agent not responding:**
- Check your internet connection
- Verify API keys are valid
- Look at console output for error messages

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Groq API Documentation](https://console.groq.com/docs)
- [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629)

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests to improve this project!
