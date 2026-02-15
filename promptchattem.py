from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# Load modelf
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=2000,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)
chat_model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_messages([
 ("system", "You are a helpful assistant"),
 ("user", "tell me about {topic} in 3000 words")
])

chain = prompt | chat_model | StrOutputParser()

for chunk in chain.stream({"topic":"money"}):
    print(chunk, end="", flush=True)
