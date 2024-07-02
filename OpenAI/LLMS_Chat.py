from OpenAI.Constant import API_KEY, CHAT_RULES
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Tạo một PromptTemplate để kiểm tra tính liên quan đến khoa học máy tính
# template = "Just answer true or false if the following question belongs to the field of computer science. The question is: "
cs_check_template = PromptTemplate.from_template(
    CHAT_RULES+ "{user_input}"
)

 # ChatOpenAI Model
llm = ChatOpenAI(
        model="gpt-3.5-turbo-0125", 
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=API_KEY
    )

# Hàm kiểm tra câu hỏi có liên quan đến khoa học máy tính không
def is_cs_question(user_input):
    formatted_prompt = cs_check_template.format(user_input=user_input)
    response = llm.invoke(formatted_prompt)
    return response.content == "True"



def disscus(message, chat_history):
    if(is_cs_question(message)==False):
         return "Do not handle requests unrelated to computer science."
    prompt  = ""
    for entry in chat_history:
            prompt += f"Human: {entry['message']}\nBot: {entry['response']}\n"

    prompt += f"Human: {message}\n"

        # Invoke LangChain to get response
    response = llm.invoke(prompt)
    return response.content