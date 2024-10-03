from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful assisstant"),
        ("human", "Tell me a joke about {something}"),
    ]
)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"something": "cats"})
print(result)
