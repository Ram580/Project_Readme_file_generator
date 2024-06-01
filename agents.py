from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI

## Initialize the tool for internet searching capabilities
os.environ['SERPER_API_KEY'] = os.getenv('serper')

os.environ['Github_token'] = os.getenv('Github_token')
content_types = ["code", "issues", "pull_requests", "discussions"]

# call the gemini models
llm=ChatGoogleGenerativeAI(#model="gemini-1.5-flash",
                           model="gemini-pro",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))


from crewai_tools import (
  CodeDocsSearchTool,
  GithubSearchTool,
  DirectoryReadTool,
  FileReadTool,
  ScrapeWebsiteTool,
  #MDXSearchTool,
  PDFSearchTool,
  SerperDevTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
file_read_tool = FileReadTool()
directory_read_tool = DirectoryReadTool()
CodeDocs_Search_tool = CodeDocsSearchTool()
Github_Search_tool = GithubSearchTool(gh_token= os.getenv('Github_token'),content_types=content_types)
# semantic_search_resume = PDFSearchTool(mdx=r"inputs\Ram_Resume_2024.pdf")

from crewai import Agent

## Creating Agents 

# 1)Repository Analyzer
analyzer = Agent(
  role='Code Analyst',
  goal='Analyze the GitHub repository to understand its structure and identify key components and structure.',
  backstory='A meticulous software engineer with years of experience in code analysis and project documentation. known for diving deep into codebases and extracting valuable insights.',
  tools=[Github_Search_tool, CodeDocs_Search_tool, directory_read_tool, file_read_tool, search_tool, scrape_tool],
  verbose=True,
  llm=llm,
  allow_delegation=True
)

# 2)Feature Extractor
feature_extractor = Agent(
  role='Feature Specialist',
  goal='Extract and describe the main features and functionalities of the project.highlighting what makes the project unique and valuable.',
  backstory='A dedicated senior software developer who is an expert and excels in understanding and explaining project features in a detailed manner and user-friendly manner, ensuring that every feature is well-documented and appreciated.',
  tools=[Github_Search_tool, CodeDocs_Search_tool, file_read_tool, search_tool, scrape_tool, CodeDocs_Search_tool],
  verbose=True,
  llm=llm
)

# 3)Technology Reviewer
tech_reviewer = Agent(
  role='Technology Analyst',
  goal='Identify and describe the technologies used in the project.explaining their roles and benefits in the context of the project.',
  backstory='An experienced technologist with a deep understanding of various programming languages, frameworks, and tools. adept at evaluating and articulating the strengths and applications of each technology.',
  tools=[Github_Search_tool, CodeDocs_Search_tool, file_read_tool, search_tool, CodeDocs_Search_tool],
  verbose=True,
  llm=llm
)

# 4) Documentation Specialist
doc_specialist = Agent(
  role='Documentation Expert',
  goal='Compile the analysis, features, and technology descriptions into a coherent and comprehensive README file that is both informative and engaging.',
  backstory='A skilled technical writer who specializes in creating clear, comprehensive, and engaging documentation.ensuring that the project README is a valuable resource for users and developers alike.',
  tools=[Github_Search_tool, CodeDocs_Search_tool,file_read_tool, search_tool ],
  verbose=True,
  llm=llm,
  allow_delegation=True
)

