from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

##Loading environment variables
load_dotenv()

##Creating Gemini model object
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

##Create prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],  ##Tells the langchain which placeholders are ecpected inside the template
    template="Explain {topic} in simple words for beginners."
)

##To Fill placeholder dynamically
final_prompt = prompt_template.format(topic="Artificial Intelligence")

##Send prompt to model
response = llm.invoke(final_prompt)

##Print generated answer
print(response.content)