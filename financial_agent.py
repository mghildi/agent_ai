from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent = Agent(
    name="Web_Search_Agent",
    role = "Search web for information",
    model = Groq(id = "llama-3.2-1b-preview"),
    tools= [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance_Agent",
    
    model = Groq(id = "llama-3.2-1b-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, 
                         stock_fundamentals=True, company_news=True),
                         ],
    instructions=["Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations for ECPG and latest news", stream=False)


