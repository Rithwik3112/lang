import gradio as gr
def per(name: str,file,number) -> str:
    return f"Hello {name}{file}{number}!"
demo = gr.Interface(
    fn = per,
    inputs = [gr.Textbox(label="Enter your name"),gr.File(label="Upload a file"),gr.Slider(label="Select a number", minimum=0, maximum=100)],
    outputs = gr.Textbox(label="Greeting")
    
    
)
demo.launch()