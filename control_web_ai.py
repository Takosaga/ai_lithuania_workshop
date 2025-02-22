import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

import asyncio

from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI


async def main():
    agent = Agent(
        task="Go to tsi.lv and find information of each masters degrees available, export and format in JSON",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp"),
    )
    result = await agent.run()
    print(result)


asyncio.run(main())