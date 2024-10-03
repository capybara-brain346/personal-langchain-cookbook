from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    SystemMessage(content="You are n helpful assisstant"),
    HumanMessage(content="What is chemical formula for Salt?"),
]

result = model.invoke(messages)
print(result)
