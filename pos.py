# skills_map.py
job_titles = [
    # Software Development
    "Python Developer Intern", "Junior Python Developer", "Associate Python Developer",
    "Senior Python Developer",
    "Software Engineer Intern", "Junior Software Engineer", "Associate Software Engineer",
    "Senior Software Engineer",
    "ML Engineer Intern", "Junior ML Engineer", "Associate ML Engineer",
    "Senior ML Engineer",
    "Frontend Engineer Intern", "Junior Frontend Engineer", "Associate Frontend Engineer",
    "Senior Frontend Engineer",
    "Backend Engineer Intern", "Junior Backend Engineer", "Associate Backend Engineer",
    "Senior Backend Engineer",
    "Full Stack Engineer Intern", "Junior Full Stack Engineer", "Associate Full Stack Engineer",
    "Senior Full Stack Engineer",
    "AI Engineer Intern", "Junior AI Engineer", "Associate AI Engineer",
    "Senior AI Engineer",
    "Generative AI Engineer Intern", "Junior Generative AI Engineer", "Associate Generative AI Engineer",
    "Senior Generative AI Engineer",

    # Data & Analytics
    "Data Scientist Intern", "Junior Data Scientist", "Associate Data Scientist",
    "Senior Data Scientist",
    "Data Analyst Intern", "Junior Data Analyst", "Associate Data Analyst",
    "Senior Data Analyst",
    "Business Intelligence (BI) Analyst", "Data Engineer", "Machine Learning Engineer",

    # Product Management
    "Product Manager Intern", "Junior Product Manager", "Associate Product Manager",
    "Senior Product Manager", "Product Owner",

    # Quality Assurance (QA) & Testing
    "QA Engineer Intern", "Junior QA Engineer", "Associate QA Engineer",
    "Senior QA Engineer", "Automation Test Engineer", "Performance Test Engineer",
    "Security Test Engineer",

    # DevOps & Infrastructure
    "DevOps Engineer Intern", "Junior DevOps Engineer", "Associate DevOps Engineer",
    "Senior DevOps Engineer", "Site Reliability Engineer (SRE)", "Cloud Engineer",
    "Systems Administrator",

    # Cybersecurity
    "Cybersecurity Analyst Intern", "Junior Cybersecurity Analyst", "Associate Cybersecurity Analyst",
    "Senior Cybersecurity Analyst", "Security Engineer", "Penetration Tester",
    "Security Architect",

    # Sales & Marketing
    "Marketing Intern", "Junior Marketing Specialist", "Associate Marketing Specialist",
    "Senior Marketing Specialist", "Sales Representative", "Account Manager",
    "Sales Engineer", "Digital Marketing Specialist", "Content Strategist", 
    "Growth Hacker", "SEO Specialist",

    # Customer Support & Success
    "Customer Support Intern", "Junior Customer Support Specialist", "Customer Success Manager",
    "Technical Support Engineer", "Client Relationship Manager",

    # Human Resources (HR)
    "HR Generalist", "HR Business Partner", "Recruiter",
    "Talent Acquisition Specialist", "Compensation and Benefits Specialist",
    "Employee Engagement Specialist",

    # UI/UX Design
    "UI/UX Design Intern", "Junior UI/UX Designer", "Associate UI/UX Designer",
    "Senior UI/UX Designer",

    # Design
    "Graphic Designer", "Motion Graphics Designer", "Creative Director",
    "Interaction Designer", "UX Researcher",

    # Project Management
    "Project Manager Intern", "Junior Project Manager", "Associate Project Manager",
    "Senior Project Manager", "Scrum Master", "Agile Coach",

    # Software Development (Additional Specializations)
    "Mobile App Developer (iOS, Android)", "Blockchain Developer", 
    "Embedded Systems Engineer", "Game Developer", "AR/VR Developer",

    # Artificial Intelligence & Machine Learning
    "NLP Engineer", "Computer Vision Engineer", "Deep Learning Specialist",
    "AI Research Scientist",

    # Technical Writing
    "Technical Writer Intern", "Junior Technical Writer", "Senior Technical Writer",
    "Documentation Specialist",

    # Legal & Compliance
    "Compliance Officer", "Legal Counsel", "Contract Manager",

    # Finance & Accounting
    "Financial Analyst", "Accountant", "Controller", "Chief Financial Officer (CFO)",

    # Operations & Administration
    "Office Manager", "Operations Manager", "Administrative Assistant"
]



tech_stack = {
    # Python Developer
    "Python Developer Intern": [
        "Python Basics", "Django", "Flask", "FastAPI", "Pandas", "NumPy"
    ],
    "Junior Python Developer": [
        "Django", "Flask", "FastAPI", "Pandas", "NumPy",
        "Pydantic", "Basic Docker Usage", "API Development"
    ],
    "Associate Python Developer": [
        "Django", "Flask", "FastAPI", "Pandas", "NumPy", "PyTorch", "TensorFlow",
        "SQLAlchemy", "Gunicorn", "Pydantic", "Jupyter", "pytest", "Docker", "Advanced API Development"
    ],
    "Senior Python Developer": [
        "Django", "Flask", "FastAPI", "Pandas", "NumPy", "PyTorch", "TensorFlow",
        "SQLAlchemy", "Gunicorn", "uWSGI", "Pydantic", "Jupyter", "pytest", "Docker", "API Development",
        "System Architecture", "Microservices", "Scalability"
    ],

    # Software Engineer
    "Software Engineer Intern": [
        "Java Basics", "C++ Basics", "Python Basics", "Git Basics", "OOP Concepts", "Unit Testing", "SQL", "Linux Basics"
    ],
    "Junior Software Engineer": [
        "Java", "C++", "Python", "Git", "REST APIs", "OOP Concepts", "Unit Testing", "SQL", "NoSQL",
        "Agile Methodologies", "Docker", "CI/CD Basics", "Cloud Basics", "Linux"
    ],
    "Associate Software Engineer": [
        "Java", "C++", "Python", "Git", "REST APIs", "Microservices", "SQL", "NoSQL",
        "Agile Methodologies", "Docker", "CI/CD Pipelines", "Cloud", "Linux", "System Design"
    ],
    "Senior Software Engineer": [
        "Java", "C++", "Python", "Git", "REST APIs", "OOP Concepts", "Microservices", "Kubernetes",
        "CI/CD Pipelines", "Cloud Architecture", "Linux", "Agile Methodologies", "Design Patterns", "Leadership"
    ],

    # Machine Learning Engineer
    "ML Engineer Intern": [
        "TensorFlow Basics", "PyTorch Basics", "Scikit-learn", "Keras", "Pandas", "NumPy",
        "Basic ML Algorithms", "Python"
    ],
    "Junior ML Engineer": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "Pandas", "NumPy",
        "MLflow", "Basic Apache Spark", "Basic Docker Usage", "ML Algorithms", "Python"
    ],
    "Associate ML Engineer": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "Pandas", "NumPy",
        "MLflow", "Apache Spark", "Kubeflow", "Docker", "Airflow", "ONNX", "Advanced ML Algorithms", "Python"
    ],
    "Senior ML Engineer": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "Pandas", "NumPy",
        "MLflow", "Apache Spark", "Kubeflow", "H2O.ai", "Docker", "Airflow", "ONNX", "ML Algorithms",
        "Distributed Training", "Model Optimization", "Python", "AI Strategy"
    ],

    # Frontend Engineer
    "Frontend Engineer Intern": [
        "HTML/CSS", "JavaScript Basics", "React.js", "Basic Bootstrap", "Basic Web Accessibility"
    ],
    "Junior Frontend Engineer": [
        "React.js", "Angular", "Vue.js", "JavaScript", "TypeScript", "HTML/CSS",
        "SASS", "Webpack", "Bootstrap", "Tailwind CSS", "Material-UI", "Redux", "Basic GraphQL", "Next.js"
    ],
    "Associate Frontend Engineer": [
        "React.js", "Angular", "Vue.js", "JavaScript", "TypeScript", "HTML/CSS",
        "SASS", "Webpack", "Bootstrap", "Tailwind CSS", "Material-UI", "Redux", "GraphQL", "Next.js", "Gatsby"
    ],
    "Senior Frontend Engineer": [
        "React.js", "Angular", "Vue.js", "JavaScript", "TypeScript", "HTML/CSS",
        "SASS", "Webpack", "Bootstrap", "Tailwind CSS", "Material-UI", "Redux", "GraphQL", "Next.js", "Gatsby",
        "UI/UX Design", "Performance Optimization", "Advanced Web Accessibility", "Architecture Design"
    ],

    # Backend Engineer
    "Backend Engineer Intern": [
        "Node.js Basics", "Express.js", "Basic Django", "Basic Flask", "SQL Basics", "MongoDB Basics"
    ],
    "Junior Backend Engineer": [
        "Node.js", "Express.js", "Django", "Flask", "FastAPI", "Spring Boot",
        "PostgreSQL", "MongoDB", "Redis", "GraphQL", "Basic Docker Usage", "API Development"
    ],
    "Associate Backend Engineer": [
        "Node.js", "Express.js", "Django", "Flask", "FastAPI", "Spring Boot",
        "Ruby on Rails", "PostgreSQL", "MongoDB", "Redis", "GraphQL", "Kafka",
        "Docker", "Kubernetes", "gRPC", "SQL", "NoSQL", "API Development"
    ],
    "Senior Backend Engineer": [
        "Node.js", "Express.js", "Django", "Flask", "FastAPI", "Spring Boot",
        "Ruby on Rails", "PostgreSQL", "MongoDB", "Redis", "GraphQL", "Kafka",
        "RabbitMQ", "Docker", "Kubernetes", "gRPC", "SQL", "NoSQL", ".NET",
        "Microservices Architecture", "System Design", "Scalability", "Cloud Architecture"
    ],

    # Full Stack Engineer
    "Full Stack Engineer Intern": [
        "HTML/CSS", "JavaScript Basics", "Node.js Basics", "Express.js Basics", "React.js Basics", "MongoDB Basics"
    ],
    "Junior Full Stack Engineer": [
        "React.js", "Angular", "Vue.js", "Node.js", "Express.js", "Django",
        "Flask", "MongoDB", "PostgreSQL", "Docker Basics", "GraphQL", "Webpack"
    ],
    "Associate Full Stack Engineer": [
        "React.js", "Angular", "Vue.js", "Node.js", "Express.js", "Django",
        "Flask", "MongoDB", "PostgreSQL", "Docker", "Kubernetes", "GraphQL",
        "Webpack", "Nginx", "Heroku", "AWS"
    ],
    "Senior Full Stack Engineer": [
        "React.js", "Angular", "Vue.js", "Node.js", "Express.js", "Django",
        "Flask", "MongoDB", "PostgreSQL", "Docker", "Kubernetes", "GraphQL",
        "Webpack", "Nginx", "Heroku", "AWS", ".NET",
        "Microservices", "Scalability", "System Design", "Cloud Architecture"
    ],

    # AI Engineer
    "AI Engineer Intern": [
        "TensorFlow Basics", "PyTorch Basics", "Scikit-learn", "Keras", "Python", "Basic ML Algorithms"
    ],
    "Junior AI Engineer": [
        "TensorFlow", "PyTorch", "Keras", "OpenCV", "Scikit-learn", "Basic Reinforcement Learning",
        "Python", "Transformers", "Basic Natural Language Processing"
    ],
    "Associate AI Engineer": [
        "TensorFlow", "PyTorch", "Keras", "OpenCV", "Scikit-learn", "Reinforcement Learning",
        "Transformers", "Hugging Face", "Deep Learning", "Python", "NLP", "GANs", "AutoML"
    ],
    "Senior AI Engineer": [
        "TensorFlow", "PyTorch", "Keras", "OpenCV", "Natural Language Toolkit (NLTK)",
        "Transformers", "Hugging Face", "Scikit-learn", "Deep Learning", "Reinforcement Learning",
        "Python", "SpaCy", "AllenNLP", "ONNX", "GANs", "AutoML", "Ray",
        "AI Strategy", "Model Optimization", "System Design"
    ],

    # Generative AI Engineer
    "Generative AI Engineer Intern": [
        "OpenAI GPT Basics", "Hugging Face Transformers Basics", "PyTorch", "TensorFlow", "Basic NLP", "Python"
    ],
    "Junior Generative AI Engineer": [
        "OpenAI GPT", "Hugging Face Transformers", "DALL-E", "Stable Diffusion",
        "PyTorch", "TensorFlow", "Basic Reinforcement Learning",
        "GANs", "Natural Language Processing (NLP)", "LLMs", "LangChain", "AutoGPT"
    ],
    "Associate Generative AI Engineer": [
        "OpenAI GPT", "Hugging Face Transformers", "DALL-E", "Stable Diffusion",
        "PyTorch", "TensorFlow", "Reinforcement Learning",
        "Generative Adversarial Networks (GANs)", "Natural Language Processing (NLP)",
        "Large Language Models (LLMs)", "LangChain", "AutoGPT", "RAG (Retrieval Augmented Generation)"
    ],
    "Senior Generative AI Engineer": [
        "OpenAI GPT", "Hugging Face Transformers", "DALL-E", "Stable Diffusion",
        "PyTorch", "TensorFlow", "Reinforcement Learning",
        "Generative Adversarial Networks (GANs)", "Natural Language Processing (NLP)",
        "Large Language Models (LLMs)", "LangChain", "AutoGPT", "RAG (Retrieval Augmented Generation)",
        "System Design", "Scalability", "AI Ethics"
    ],

    # Data Scientist
    "Data Scientist Intern": [
        "Python Basics", "R Basics", "Pandas", "NumPy", "Scikit-learn", "Basic Data Visualization"
    ],
    "Junior Data Scientist": [
        "Python", "R", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras",
        "Matplotlib", "Seaborn", "SQL", "Data Wrangling"
    ],
    "Associate Data Scientist": [
        "Python", "R", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras",
        "Matplotlib", "Seaborn", "SQL", "Dask", "Statsmodels", "Data Engineering", "Machine Learning"
    ],
    "Senior Data Scientist": [
        "Python", "R", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras",
        "Matplotlib", "Seaborn", "SQL", "Dask", "Statsmodels", "Data Engineering",
        "Apache Spark", "Deep Learning", "AI Strategy", "Model Deployment"
    ],

    # Data Analyst
    "Data Analyst Intern": [
        "Excel", "SQL Basics", "Python Basics", "Basic Data Visualization", "Google Analytics Basics"
    ],
    "Junior Data Analyst": [
        "Excel", "SQL", "Python", "Tableau", "Power BI", "Google Analytics",
        "Data Cleaning", "Data Visualization", "Statistical Analysis"
    ],
    "Associate Data Analyst": [
        "Excel", "SQL", "Python", "Tableau", "Power BI", "Google Analytics",
        "Data Cleaning", "Data Visualization", "Advanced Statistical Analysis", "Data Modeling"
    ],
    "Senior Data Analyst": [
        "Excel", "SQL", "Python", "Tableau", "Power BI", "Google Analytics",
        "Data Cleaning", "Data Visualization", "Statistical Analysis", "Data Modeling",
        "Predictive Analytics", "Big Data Tools"
    ]
}
