import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

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