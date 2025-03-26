import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Initialize Agents
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

st.set_page_config(page_title="Financial AI Agent", page_icon="💰")
st.title("📈 Financial AI Agent")
st.write("Enter a stock symbol to get financial insights.")

stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT):", "")

if st.button("Get Insights"):
    if stock_symbol:
        query = f"Summarize analyst recommendation and share the latest news for {stock_symbol}"
        with st.spinner("Fetching data..."):
            response = multi_ai_agent.run(query)
        st.markdown(response.content)
    else:
        st.warning("Please enter a stock symbol!")

st.sidebar.title("🔍 About")
st.sidebar.info("This AI-powered financial agent fetches stock market insights and latest news.")