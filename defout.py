from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    max_new_tokens=2000,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)
llm = ChatHuggingFace(llm=llm)
class joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
    
outputparser = JsonOutputParser(pydantic_object=joke)
instrction= outputparser.get_format_instructions()

prompt = PromptTemplate(
    template = "Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables = ["query"],
    partial_variables={"format_instructions": instrction}
)
chain = prompt | llm |outputparser
result = chain.invoke({"query": "Tell me a joke about cats."})
print(result)
    
