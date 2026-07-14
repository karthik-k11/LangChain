from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

##Load environment variables
load_dotenv()

##Create the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

##Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words for a beginner."
)

##Create a chain
chain = prompt | llm

##Execute the chain
response = chain.invoke(
    {
        "topic": "Artificial Intelligence"
    }
)

##Print only the generated response
print(response.content)