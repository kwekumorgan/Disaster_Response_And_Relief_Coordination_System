import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from environment import get_disaster_state


class SensorAgent(Agent):
    """Agent responsible for monitoring environmental disaster states."""
    
    class MonitorBehaviour(CyclicBehaviour):
        """Continuously monitors and logs disaster events."""
        
        async def run(self):
            # Retrieve current disaster state
            state = get_disaster_state()
            disaster = state["disaster_type"]
            severity = state["severity_level"]

            # Format log entry
            log_entry = f"Perceived Event -> Disaster: {disaster}, Severity: {severity}"
            print(log_entry)

            # Persist to log file
            with open("event_log.txt", "a") as log_file:
                log_file.write(log_entry + "\n")

            await asyncio.sleep(3)

    async def setup(self):
        """Initialize agent and start monitoring behaviour."""
        print("SensorAgent started and monitoring environment...")
        monitor = self.MonitorBehaviour()
        self.add_behaviour(monitor)


async def main():
    """Main execution function."""
    # Initialize and configure agent
    agent = SensorAgent(
        jid="kwekumorgan@xmpp.jp",
        password="MGK_042004",
        verify_security=False
    )
    
    await agent.start()
    print("Agent running...")
    
    # Run monitoring for specified duration
    await asyncio.sleep(20)
    
    # Cleanup
    await agent.stop()
    print("SensorAgent stopped.")


if __name__ == "__main__":
    asyncio.run(main())