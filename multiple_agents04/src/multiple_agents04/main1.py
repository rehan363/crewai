from crewai.flow import start, listen, Flow
from multiple_agents04.crews.dev_crew.dev_crew import DevCrew


class DevFlow(Flow):
    
    @start()
    def run_dev_crew(self):
        output= DevCrew().crew().kickoff(
            inputs={
                "problem":"write python logic code for making api."
            }
        )
        return output.raw
    
def run():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)


