# app.py

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts import JD_PROMPT
from pos import job_titles, tech_stack




# Setup OpenAI API key and model
OPENAI_API_KEY = ''
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY, temperature=0.7)

# Prompt template
prompt = PromptTemplate(
    template=JD_PROMPT,
    input_variables=[
        "company_name", "job_title", "require_skills", "experience",
        "location", "qualifications", "salary",
        "job_type", "benefits"
    ]
)

chain = prompt | llm | StrOutputParser()

# Streamlit app
def main():
    st.title("------BRB JD Builder-----")

    company_name = st.text_input("Company name:")
    job_title = st.selectbox("Select Job Title:", job_titles)  # job_titles is a list of strings
    
    # Automatically fill skills based on the selected job title
    if job_title:
        available_skills = tech_stack.get(job_title, [])
        require_skills = st.multiselect("Select Required Skills:", available_skills, default=available_skills)
        
        # Input field for adding new skills
        new_skill = st.text_input("Add a new skill if not listed above:")
        if new_skill:
            require_skills.append(new_skill)


    


    
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
        
        # Split the output into sections
        sections = output_text.split("\n\n")
        
        # Display each section separately
        for section in sections:
            st.markdown(section)

if __name__ == "__main__":
    main()
