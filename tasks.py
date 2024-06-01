from crewai import Task
from agents import analyzer, feature_extractor, tech_reviewer, doc_specialist
from agents import search_tool, scrape_tool, file_read_tool, directory_read_tool, CodeDocs_Search_tool, Github_Search_tool


# Define tasks
repo_analysis_task = Task(
  description='Analyze the directory structure of the {repo} github repository to understand the overall organization and identify key components. Provide a detailed overview of the project\'s structure, identifying main directories, files, and their purposes.',
  expected_output='A comprehensive description of the repository structure, including the main directories, files, and their purposes.',
  agent=analyzer,
  tools=[Github_Search_tool, CodeDocs_Search_tool, directory_read_tool, file_read_tool, search_tool, scrape_tool]
)

feature_extraction_task = Task(
  description='Analyze the codes in {repo} github repository, Identify and describe the main features and functionalities of the project. Highlight the unique aspects and core features that make the project stand out. Collaborate with the Repository Analyzer to ensure no important feature is overlooked.',
  expected_output='A detailed list of key features with thorough descriptions, explaining their functionalities and benefits.',
  agent=feature_extractor,
  tools=[Github_Search_tool, CodeDocs_Search_tool, file_read_tool, search_tool, scrape_tool, CodeDocs_Search_tool],
)

tech_identification_task = Task(
  description='Analyze the project in detailed in {repo} github repository, Identify the technologies used in the project and provide a detailed explanation of each, including their roles and advantages within the project. Work closely with the Repository Analyzer to gather accurate information.',
  expected_output='A comprehensive summary of the technologies used, including languages, frameworks, and tools, with detailed explanations of their roles and benefits.',
  agent=tech_reviewer,
  tools=[Github_Search_tool, CodeDocs_Search_tool, file_read_tool, search_tool, CodeDocs_Search_tool]
)

readme_compilation_task = Task(
  description='Compile the information gathered by the other agents into a comprehensive README.md file. Ensure the README is clear, informative, and engaging, covering all essential aspects of the project. Collaborate with other agents to fill any gaps in information.',
  expected_output='A formatted README.md file with project description, features, technologies, and code explanations.',
  agent=doc_specialist,
  tools=[Github_Search_tool, CodeDocs_Search_tool,file_read_tool, search_tool ],
  verbose=True,
  output_file='Repository_Readme.md'
)