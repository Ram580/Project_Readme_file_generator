from crewai import Crew,Process
from tasks import repo_analysis_task, feature_extraction_task, tech_identification_task, readme_compilation_task
from agents import analyzer, feature_extractor, tech_reviewer, doc_specialist
import streamlit as st

# Form the crew
crew = Crew(
  agents=[analyzer, feature_extractor, tech_reviewer, doc_specialist],
  tasks=[repo_analysis_task, feature_extraction_task, tech_identification_task, readme_compilation_task],
  process=Process.sequential
)

## starting the task execution process wiht enhanced feedback

# result=crew.kickoff(inputs={'topic':'AI in Automotive Industry'})
# print(result)

# Create a Streamlit app
st.title("Projects Readme.md file Generator")

# Input Variables
repo = st.text_input("Enter the link of the Github repo")
input={'repo':repo}

# Run CrewAI
if st.button("Run CrewAI"):
    # Set inputs for the execution of the Crew
    result=crew.kickoff(inputs=input)
    st.markdown(result)