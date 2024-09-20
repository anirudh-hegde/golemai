import google.generativeai as genai
import os
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="GolemAI", page_icon="🤖")

st.sidebar.title('Navigation')
with st.sidebar:
    pages = option_menu("Go to", ['About', 'Golang Code Generator', 'Golang Formatter', 'Golang Code Explainer'])
    API_KEY = st.sidebar.text_input("Enter the google api")


def configure():
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    return model

def generate_go_snippet(model, input_prompt):
    template = """
        Create a Golang code snippet using the below text:

        ```
        {text_input}
        ```  
        i just want a Golang code snippet         
    """
    formatted_template = template.format(text_input=input_prompt)
    response = model.generate_content(formatted_template)
    go_snippet = response.text.strip().lstrip("```go").rstrip("```")
    return go_snippet


def generate_expected_output(model, go_snippet):
    expected_output = """
        What would be the expected response of this Golang snippet:

        ```
        {go_snippet}
        ```  
        Provide sample code with no explanation        
    """
    expected_output_formatted = expected_output.format(go_snippet=go_snippet)
    response = model.generate_content(expected_output_formatted)
    return response.text


def generate_explanation(model, go_snippet):
    explanation = """
        Explain this Golang code snippet:

        ```
        {go_snippet}
        ```  
        Please provide the simplest explanation:       
    """
    explanation_formatted = explanation.format(go_snippet=go_snippet)
    response = model.generate_content(explanation_formatted)
    return response.text


def golang_formatter(model, go_code):
    template = """
        Format this Golang code block:

        ```
        {go_code}
        ```  
        Format this Golang code        
    """
    formatted_template = template.format(go_code=go_code)
    response = model.generate_content(formatted_template)
    formatted_golang = response.text.strip().lstrip("```go").rstrip("```")
    return formatted_golang


def golang_code_explainer(model, go_syntax):
    explanation = """
        Explain each part of this Golang code:

        ```
        {go_syntax}
        ```  
        Please break down the query and explain each important concept or word:      
    """
    explanation_formatted = explanation.format(go_syntax=go_syntax)
    response = model.generate_content(explanation_formatted)
    return response.text


def main():
    model = configure()
    if pages == 'About':
        st.markdown(
            """
            <div style="text-align:center;">
            <h1>GolemAI 🤖</h1>
            <h3>Your Personal Golang code Assistant</h3>
            <p> Welcome to GolemAI! Our project is your personal Golang code assistant powered by Google's 
            Generative AI tools. 
            With GenQuery, you can effortlessly generate Golang code snippets and receive detailed explanations, 
            and also format your for readability and consistency. Let's simplifying your data retrieval process!</p>           
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif pages == 'Golang Code Generator':
        st.markdown(
            """
            <div style="text-align:center;">
            <h1>Golang Code Generator 📝</h1>
            <p>Use the Golang Code Generator to create Golang code snippets from natural language prompts.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        text_input = st.text_area("Type your desired query below to unlock the power of Golang code Genie! 💬")
        submit = st.button("Generate Golang code")

        if submit:
            with st.spinner("Generating Golang code.."):
                go_snippet = generate_go_snippet(model, text_input)
                eoutput = generate_expected_output(model, go_snippet)
                explanation = generate_explanation(model, go_snippet)
                with st.container():
                    st.success(
                        "Your Golang code snippet has been successfully generated. "
                        "Feel free to copy and paste it into your IDE or code editor "
                        "system to run the requested code snippet.")
                    st.code(go_snippet, language="go")

                    st.markdown(
                        """
                        <div style="background-color: #d4edda; padding: 10px; border-radius: 5px;">
                            Expected output of this Golang code snippet.<br>
                            If the structure of the query isn't displayed, please click again on the 
                            'Generate Golang code snippet' button.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown(eoutput)

                    st.success("Explanation of SQL Query")
                    st.markdown(explanation)

    elif pages == 'Golang Formatter':
        st.markdown(
            """
            <div style="text-align:center;">
            <h1>Golang Formatter 📋</h1>
            <p>Use the Golang formatter to format your Golang queries for readability and consistency.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        go_input = st.text_area("Paste your Golang code here:")
        format_button = st.button("Format Golang")

        if format_button:
            if go_input:
                formatted_go = golang_formatter(model, go_input)
                st.code(formatted_go, language='go')

    elif pages == 'Golang Code Explainer':
        st.markdown(
            """
            <div style="text-align:center;">
            <h1>Code Explainer 📢</h1>
            <p>Understand each part of your Golang code snippet with explanations.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        go_syntax = st.text_area("Paste your Golang syntax here:")
        explain_button = st.button("Explain the Code")

        if explain_button:
            if go_syntax:
                explanation = golang_code_explainer(model, go_syntax)
                st.markdown(explanation)


if __name__ == "__main__":
    main()
