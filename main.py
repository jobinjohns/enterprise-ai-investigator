from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.2
    )


response = llm.invoke(" explain what an ai agent is in 100 words")

print(response.content[0].text)