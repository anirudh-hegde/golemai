# GolemAI 🤖

Welcome to **GolemAI**! This project is your personal Golang code assistant powered 
by Google's Generative AI tools.GolemAI provides functionalities to generate, format, 
and explain Golang code snippets based on natural language prompts.
Application is deployed on AWS Cloud utilizing the service of AWS Elastic Beanstalk.

## Demo
https://youtu.be/WfqIt4PzYFw

## Intro
GolemAI aims to simplify the process of working with Golang by providing an intuitive 
interface for generating and understanding code.Using Google's Generative AI, 
GolemAI can generate Golang code snippets, format them for better readability, 
and provide detailed explanations.

## Problem
Challenges are:
* Developers who wanna learn Golang which might increase their learning curve.
* Who lacks expertise in Golang.
* Human Error.
* Language specific challenges as Golang has paradigms that can be difficult to matter.

## Solution
* GolemAl bridges the gap for new developers by providing simple, understandable, and
  functional Go code examples that can help them quickly learn and implement Golang features.
* GolemAl generates Go code snippets based on natural language descriptions, allowing users
  to quickly convert their thoughts or project needs into code.
* GolemAl generates code that effectively handles these Go-specific constructs, helping developers
  overcome challenges unique to Go.
* GolemAl can automate the generation of these common Go structures, reducing manual effort and
  allowing developers to focus on more complex logic.

## Features
* **Golang Code Generator**: Create Golang code snippets from natural language prompts.
* **Golang Formatter**: Format your Golang code for consistency and readability.
* **Golang Code Explainer**: Get detailed explanations of Golang code snippets.

## Getting Started
### Prerequisites
- Python 3.7+
- Streamlit
- Google Generative AI API access
### API/Service Details
- Go to https://aistudio.google.com/app/apikey
- Create API key.
- Navigate to Google Cloud->Actvate your account->Under API & Services->Enable Generative Language API.
- Copy the API key in the application.

## Utilizing AWS
![image](https://github.com/user-attachments/assets/a9d9ba70-d874-4d83-8bee-4723718fa1f1)
![golemai-aws-architecture](https://github.com/user-attachments/assets/7af1e8b1-9704-40e6-9932-0af34cdd6f2b)

![image](https://github.com/user-attachments/assets/ddb3118b-b172-473c-a52c-1222474604ca)
* **Developed a Golang-Powered AI Code Assistant**: Spearheaded the development of **GolemAI**, an intelligent code assistant for Golang utilizing **Google's Generative AI** tools to generate, format, and explain code snippets based on user prompts. This involved deep integration of natural language processing (NLP) capabilities with Golang-specific features.

* **Deployed Scalable Application on AWS Cloud**: Implemented a fully scalable application architecture on AWS using Elastic Beanstalk by choosing **Docker** as platform, ensuring high availability and efficient resource management. **Automated CI/CD pipelines** through **AWS CodeBuild and CodePipeline**, enabling **continuous delivery** and version control of the application.
* **Optimized Cloud Infrastructure for Performance**: Utilized AWS services such as **CodeBuild and Elastic Beanstalk** to streamline deployment and scaling processes, ensuring the GolemAI application maintained performance efficiency while handling dynamic user traffic and code generation requests in a cloud environment.

Access the application deployed using AWS: http://golemai.us-east-1.elasticbeanstalk.com/

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anirudh-hegde/golemai.git
   cd golemai
   python3 -m venv venv
   pip install -r requirements.txt
2. Run the app:
   ```bash
   python3 -m streamlit run golem.py


## Conclusion
Congratulations! You have successfully run the application 🚀️.

To view the GolemAI app 👉 https://golemai.streamlit.app/
