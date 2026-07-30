from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from app.utils.logger import setup_logger 

load_dotenv()
logger = setup_logger()
logger.info("Initializing Gemini model...")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.2,
)

logger.info("Sending prompt to Gemini...")

response = llm.invoke(
    "Explain what an AI Agent is in 100 words."
)

logger.info("Response received successfully.")

logger.info(response.content[0].text)
logger.info(type(response))