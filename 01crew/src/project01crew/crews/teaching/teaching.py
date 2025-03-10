from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
import yaml
@CrewBase
class TeachingCrew:
    def first(self):
        agents_config = "config/agents.yaml"
        tasks_config = "config/tasks.yaml"


        # with open ("config/agents.yaml", "r") as f:
        #     self.agents_config = yaml.safe_load(f)
        # with open ("config/tasks.yaml", "r") as f:
        #     self.tasks_config = yaml.safe_load(f)
    
        

      
    @agent
    def sir(self) ->Agent:
        return Agent(
           
            config=self.agents_config['sir'],
        )
    
    @task
    def explain_topic(self) -> Task:
        return Task(
            
            config=self.tasks_config['explain_topic'],
        )

    @crew
    def crew(self) ->Crew:
        return Crew(
            agents= self.agents,
            tasks= self.tasks,
            verbose=True
        )