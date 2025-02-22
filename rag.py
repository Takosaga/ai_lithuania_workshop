from praisonaiagents import Agent

agent = Agent(instructions="You are helpful Assisant", llm="qwen2.5:7b")

agent.start("Why sky is Blue?")