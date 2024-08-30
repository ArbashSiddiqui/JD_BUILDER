import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts import JD_PROMPT
from skill_maps import job_titles, tech_stack

OPENAI_API_KEY=''
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY, temperature=0.7)

prompt = PromptTemplate(
    template=JD_PROMPT,
    input_variables=[
        "company_name", "job_title", "require_skills", "experience",
        "location", "qualifications", "salary",
        "job_type", "benefits"
    ]
)

chain = prompt | llm | StrOutputParser()

def main():
    st.title("Job Description Builder")

    company_name = st.text_input("Company name:")
    job_title = st.selectbox("Select Job Title:", job_titles)  
    
  
    if job_title:
        available_skills = tech_stack.get(job_title, [])
        require_skills = st.multiselect("Select Required Skills:", available_skills, default=available_skills)
    
    experience = st.text_input("Experience:")
    location = st.text_input("Location:")
    qualifications = st.text_input("Qualifications:")
    salary = st.text_input("Salary:")
    job_type = st.text_input("Job Type:")
    benefits = st.text_input("Benefits:")

    if st.button("Generate Job Description"):
        user_inputs = {
            "company_name": company_name,
            "job_title": job_title,
            "require_skills": ", ".join(require_skills),
            "experience": experience,
            "location": location,
            "qualifications": qualifications,
            "salary": salary,
            "job_type": job_type,
            "benefits": benefits,
        }
        
        response = chain.invoke(user_inputs)
        output_text = response
        
        sections = output_text.split("\n\n")
        
        for section in sections:
            st.markdown(section)

