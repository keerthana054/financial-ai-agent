# financial-ai-agent
As a stepping stone of learning Agentic AI, inspired from the legend himself in AI, Krish Naik, I came across a video of him helping to create a financial agent using Phidata. As an add-on, I have used Streamlit to give UI for the same.
I have kept financial_agent_old.py, which contains the exact code that Krish Naik shows in the video, for reference.
This project is a Financial AI Agent that utilizes AI-powered models and tools to analyze stock market data, provide financial insights, and fetch the latest news. The agent is built using the Phi framework and Groq models.

## Features
- AI-driven financial insights
- Stock market analysis
- Latest company news retrieval
- Multi-agent collaboration

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip
- virtualenv or conda (recommended for environment management)

## Setup
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: ```pip install -r requirements.txt```
4. Configure API keys:
    Create a .env file in the root directory and add the following keys:
   ```
   GROQ_API_KEY=<your-groq-api-key>
   PHI_API_KEY=<your-phi-api-key>
   ```
5. Run the financial AI agent: ```python financial_ai_agent.py```

## Running the Streamlit UI
To interact with the agent using a web interface:
1. Run the Streamlit app: ```streamlit run streamlit_ui.py```

## Contributing
Feel free to contribute by submitting issues, feature requests, or pull requests.
