import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

# Agent class
class InitAgent(Agent):
    
    # Behaviour class
    class HeartbeatBehaviour(PeriodicBehaviour):
        
       
        async def run(self):
            # Print a message to show the agent is working
            print("InitAgent is alive and Active")
    
    #  sets up our agent when it first starts
    async def setup(self):
        # Print a message when the agent starts
        print("InitAgent started")
        
        # Add the heartbeat behavior to run every 2 seconds
        heartbeat = self.HeartbeatBehaviour(period=2)
        self.add_behaviour(heartbeat)



async def main():
    # Create agent with username and password
    
    username = "kwekumorgan@xmpp.jp"
    password = "MGK_042004"
    
    # Create the agent
    agent = InitAgent(
        username,
        password,
        verify_security=False  
    )
    
    # Start the agent 
    await agent.start(auto_register=True)
    
    # Wait for 6 seconds while the agent runs
   
    print("Agent is running...")
    await asyncio.sleep(6)
    
    # Stop the agent
    print("Stopping agent...")
    await agent.stop()
    print("Agent stopped!")


# This checks if we're running this file directly 
if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())