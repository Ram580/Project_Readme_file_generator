# Project Readme.md file generator AI System

## Overview
The Project Readme File Generator is a CrewAI-based system designed to analyze a GitHub repository and generate a comprehensive README.md file. The system inspects the repository structure, extracts key features, identifies the technologies used, and compiles this information into a detailed and informative README.md file.

## Features
- **Repository Analysis:** Analyzes the directory structure and identifies key components of the project.
- **Feature Extraction:** Extracts and describes the main features and functionalities of the project.
- **Technology Identification:** Identifies and explains the technologies used in the project.
- **README Compilation:** Compiles the gathered information into a well-structured README.md file.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ram580/Project_Readme_file_generator.git
Navigate to the project directory:
bash
Copy code
cd Project_Readme_file_generator
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
Run the main script:
bash
Copy code
python main.py --repo_url <GitHub_Repository_URL>
Replace <GitHub_Repository_URL> with the URL of the GitHub repository you want to analyze.
Components
Agents
Repository Analyzer (Code Analyst)

Goal: Analyze the GitHub repository to understand its structure and identify key components.
Tools: DirectoryReadTool, GithubSearchTool, CodeDocsSearchTool.
Feature Extractor (Feature Specialist)

Goal: Extract and describe the main features and functionalities of the project.
Tools: FileReadTool, CodeDocsSearchTool.
Technology Reviewer (Technology Analyst)

Goal: Identify and describe the technologies used in the project.
Tools: FileReadTool, CodeDocsSearchTool, GithubSearchTool.
Documentation Specialist (Documentation Expert)

Goal: Compile the analysis, features, and technology descriptions into a comprehensive README.md file.
Tools: TextEditorTool.
Tasks
Repository Structure Analysis

Description: Analyze the directory structure to understand the organization and identify key components.
Agent: Repository Analyzer.
Feature Extraction

Description: Identify and describe the main features of the project.
Agent: Feature Extractor.
Technology Identification

Description: Identify the technologies used in the project and provide detailed explanations.
Agent: Technology Reviewer.
README Compilation

Description: Compile the information into a comprehensive README.md file.
Agent: Documentation Specialist.
Example
python
Copy code
from crewai import Crew, Process

# Define tools and agents (as described above)

# Define tasks (as described above)

# Form the crew
crew = Crew(
  agents=[analyzer, feature_extractor, tech_reviewer, doc_specialist],
  tasks=[repo_analysis_task, feature_extraction_task, tech_identification_task, readme_compilation_task],
  process=Process.sequential
)

# Kickoff the crew
result = crew.kickoff(inputs={'github_url': 'https://github.com/example/repository'})
print(result)
Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Thanks to the developers of CrewAI for providing the framework to build this project.

