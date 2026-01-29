import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

class InitAgent(Agent):
    class HeartbeatBehaviour(PeriodicBehaviour):
        async def run(self):
            print("InitAgent is alive and Active")

    async def setup(self): 
        print("InitAgent started")
        self.add_behaviour(self.HeartbeatBehaviour(period=2))

async def main():
    agent = InitAgent(
        "kwekumorgan@xmpp.jp",
        "MGK_042004",
        verify_security=False
    )
    await agent.start(auto_register=True)
    await asyncio.sleep(6)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())