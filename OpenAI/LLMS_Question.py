from OpenAI.Constant import API_KEY, MCQ_TEMPLATE
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from typing import List


class Question(BaseModel):
    content: str = Field(description="The question's content")
    options: List[str] = Field(description="A list of answer options")
    correctAnswer: str = Field(description="The correct answer")


parser = JsonOutputParser(pydantic_object=Question)

def getInterviewQuestionsJS():
     # Initialize the OpenAI model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo-0125",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=API_KEY
    )

    prompt = PromptTemplate(template=MCQ_TEMPLATE+ "\n{format_instructions}\n",
                            partial_variables={"format_instructions": parser.get_format_instructions()})
    formatted_prompt = prompt.format()
    response = llm.invoke(formatted_prompt)
    questions = parser.invoke(response)
    return questions



if __name__ == "__main__":
    getInterviewQuestionsJS()