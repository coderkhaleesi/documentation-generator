from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
import json

from env import OPEN_API_KEY

def get_documentation(details, text):

    prompt_str = "This is a project with details given here: {details} \
A code snippet/file is given below in delimiters \
''' {text} '''\
Generate documentation as per the general details and code.\
If any code is missing, do not write documentation for that."

    gpt4_prompt = PromptTemplate(
                template=prompt_str,
                input_variables=["details", "text"]
            )
    system_message_prompt = SystemMessagePromptTemplate(prompt=gpt4_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    messages = chat_prompt.format_prompt(details=details, text=text).to_messages()
    
    chat = ChatOpenAI(model_name="gpt-4-0613", temperature=0, openai_api_key=OPEN_API_KEY)
    resp = chat(messages)

    print(resp.content)
    
    return resp.content

def combine_documentation(details, text):
    prompt_str = "This is a project with details given here: {details} \
Given here is the separate documentation from different code files: {text} \
Combine the entire documentation into a comprehensive and cohesive documentation document. \
Return the documentaion as markdown and in a proper document structure with - overview, code explanation, and usage."

    gpt4_prompt = PromptTemplate(
                template=prompt_str,
                input_variables=["details", "text"]
            )
    system_message_prompt = SystemMessagePromptTemplate(prompt=gpt4_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    messages = chat_prompt.format_prompt(details=details, text=text).to_messages()
    
    chat = ChatOpenAI(model_name="gpt-4-0613", temperature=0, openai_api_key=OPEN_API_KEY)
    resp = chat(messages)

    print(resp.content)
    
    return resp.content

if __name__=="__main__":
    print(get_documentation("x = 1", "declaring a var"))