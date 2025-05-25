import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os

async def run_memory_chat():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set")
    
    config_file = "browser_mcp.json"
    print("Initializing MCP client...")
    
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen-qwq-32b")
    
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
        verbose=True
    )

    print("Welcome to the MCP Demo!")
    print("Type 'exit' or 'quit' to exit the conversation.")
    print("Type 'clear' to clear the history of conversation.")
    print("=================================================\n")
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting conversation...")
                break
            
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Memory cleared. Starting fresh conversation...")
                continue
            
            print("\nAssistant: ", end="", flush=True)
            
            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"An error occurred: {e}")
      
    finally:
        if client and client.sessions:
            await client.close_all_sessions()
        print("\nMCP client closed.")
        
if __name__ == "__main__":
    asyncio.run(run_memory_chat())
        
        
        
        
    
