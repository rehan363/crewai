from crewai.flow import Flow, listen, start
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

class LitellmFlow(Flow):

    @start()
    def start_function(self):
        print("starting...")
        output = completion(
            model= "gemini/gemini-2.0-flash",
            api_key=os.getenv("GEMINI_API_KEY"),
            messages=[
            {
                'role':'user',
                'content':'who is founder of piaic.'
            }
        ])
        
        return output['choices'][0]['message']['content']    



def run_litellm():
    obj= LitellmFlow()
    result= obj.kickoff()
    print(result)