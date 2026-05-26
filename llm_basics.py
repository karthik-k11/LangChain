from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

##Load environment variables
load_dotenv()

##Creating gemini model object
llm = ChatGoogleGenerativeAI(
    model= "gemini-2.5-flash"
)

##Sending prompt to model
response= llm.invoke("What is Artificial Intelligence ?")

##Print the generated text, .content is for extracting the plain text from the response
print(response.content)