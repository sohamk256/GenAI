from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.7)

response = model.invoke("What is the capital of India?")
print(response.text) 

