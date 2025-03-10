from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
from project01crew.crews.teaching.teaching import TeachingCrew

import os
os.environ["OTEL_TRACES_SAMPLER"] = "always_off"


bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):
    @start()
    def generate_topic(self):
         try:
                result = completion(
                model="gemini/gemini-1.5-flash",
                messages=[{
                    "role": "user",
                    "content": "generate a trending topic in AI in 2025"
                }],
                
                )
                self.state["topic"] = result["choices"][0]["message"]["content"]
                topic= self.state["topic"]
                print(f"Step1.Generated topic: {topic}")
         except Exception as e:
                print("error while generating topic..")
        
    
    @listen("generate_topic")
    def explain_topic(self):
        print("Step2 Generate content..")
        teaching_crew= TeachingCrew().crew().kickoff(
                inputs= {
                    "topic": self.state["topic"]
                }
                )
            
        
        
   
def kickoff():
    flow = PanaFlow()
    flow.kickoff()

if __name__ == "__main__":
    kickoff()