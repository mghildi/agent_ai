from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
from dotenv import load_dotenv
import os
import phi
from phi.playground import Playground ,serve_playground_app

#Load env variable
load_dotenv()
phi.api = os.getenv("phidata_api_key")
web_search_agent = Agent(
    name="Web_Search_Agent",
    role = "Search web for stock information",
    model = Groq(id = "llama-3.2-1b-preview"),
    tools= [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance_Agent",
    
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, 
                         stock_fundamentals=True, company_news=True),
                         ],
    instructions=["Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
app = Playground(agents = [web_search_agent,finance_agent]).get_app()
if __name__=="__main__":
    serve_playground_app("playground:app", reload = True)