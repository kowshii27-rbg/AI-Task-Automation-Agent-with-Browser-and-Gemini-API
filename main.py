import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio


os.environ["GOOGLE_API_KEY"] = "Your gemini api key"  

async def main():
    agent = Agent(
        task="1. Go to LinkedIn and sign in with 'Your email' and 'Your password' 2.write a article on 'AI' ", #(any task you want to do)
        llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())