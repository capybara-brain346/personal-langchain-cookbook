from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chat_history = []
system_message = SystemMessage(content="You are n helpful assisstant")

while True:
    query = input("Enter your query: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(response)

print("----------History-----------\n", chat_history)
