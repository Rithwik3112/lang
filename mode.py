from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



# Load modelf
llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=1024,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)
chat_model = ChatHuggingFace(llm=llm)

while True:
        user_put = input("User: ")
        message  =  [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=user_put),
            
        ]
        for chunk in chat_model.stream(message):
            print(chunk.content, end="", flush=True)
