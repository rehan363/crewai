Overview
This project leverages the CrewAI framework to generate a trending AI topic for 2025 and explain it using a language model. It features two key components:

PanaFlow: Generates a trending AI topic.
TeachingCrew: Explains the topic using an agent and task setup.
The project uses the litellm library with the "gemini/gemini-1.5-flash" model for language model interactions.

1.Setup
Install Dependencies
Ensure Python 3.8+ is installed, then run:
pip install crewai litellm pyyaml

2.Set Environment Variables
Create a .env file in the root directory:
API_KEY=your_api_key_here
Configuration Files

3.Ensure config/agents.yaml and config/tasks.yaml exist with agent and task definitions.


4.Usage
Run the main script:

python main.py
The program generates a trending AI topic and prints its explanation.

Troubleshooting
File Errors: Verify config/agents.yaml and config/tasks.yaml paths.
API Issues: Check your API key in .env.

Contributing
Contributions are welcome! Fork the repo, create a branch, and submit a pull request.

