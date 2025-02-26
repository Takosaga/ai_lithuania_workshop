import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

from dotenv import load_dotenv
# loading variables from .env file
load_dotenv() # pass a path if it's not a .env in the current working directory 
 
# accessing and printing value
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

import asyncio

from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI


async def main():
    agent = Agent(
        task="Go to walmart website and find out what items are on sales, export as item name: sale price",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp"),
    )
    result = await agent.run()
    print(result)


asyncio.run(main())