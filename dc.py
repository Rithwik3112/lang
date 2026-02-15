from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.runnables import RunnableLambda
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    max_new_tokens=2000,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)

llm = ChatHuggingFace(llm=llm,verbose=True)
class joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
class exp(BaseModel):
    joke:str = Field(description ="the joke")
    explaination:str = Field(description = "the explanation of joke" )

outputparser2 = JsonOutputParser(pydantic_object = exp)
instrction2 = outputparser2.get_format_instructions()
    
outputparser = JsonOutputParser(pydantic_object=joke)
instrction= outputparser.get_format_instructions()

prompt = PromptTemplate(
    template = "Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables = ["query"],
    partial_variables={"format_instructions": instrction}
)
prompt2 = PromptTemplate(
    template = "explain me the joke .\n{formate_in}\n{query}",
    input_variables =['query'],
    partial_variables={"formate_in": instrction2}

)
def format(jokes):
    return{
        "query": f"{jokes['setup']}\n{jokes['punchline']}"
    }
    
chain = prompt | llm |outputparser

chain2 = (chain|RunnableLambda(format)|prompt2| llm |outputparser2)

result = chain2.invoke({"query": "Tell me a joke about cats."})
print(result)
print({result['joke']})
print({result['explaination']})
