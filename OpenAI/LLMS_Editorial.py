from OpenAI.Constant import API_KEY, GENERAL_EDITORIAL_TEMPLATE
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def get_algorithm_analysis(problem_description):
   
    # Khởi tạo mô hình ChatOpenAI
    llm = ChatOpenAI(
        model="gpt-3.5-turbo-0125",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=API_KEY #
    )
    cs_check_template = PromptTemplate.from_template(
        GENERAL_EDITORIAL_TEMPLATE + "{user_input}"
    )
    formatted_prompt = cs_check_template.format(user_input=problem_description)
    response = llm.invoke(formatted_prompt)
    return response.content
