import os
import httpx 
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# =========================================================
# SSL BYPASS — FOR NETFREE / FILTERED ENVIRONMENTS ONLY
# In environments with SSL inspection (e.g., NetFree, 
# corporate firewalls), Python's httpx may crash with
# certificate errors. This disables local cert validation.
# WARNING: Remove this block in production environments.
# =========================================================
os.environ.pop('SSL_CERT_FILE', None)
unsafe_transport = httpx.HTTPTransport(verify=False)
unsafe_client = httpx.Client(transport=unsafe_transport)
if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]

#api_key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    http_client=unsafe_client
)

#prompt from file
def load_prompt(version):
    path = f"prompts/{version}.md"
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

SYSTEM_PROMPT = load_prompt("v3")

def translate_to_cli(user_input):
    current_prompt = load_prompt("v3") 
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": current_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

#gradio interface
with gr.Blocks(title="CLI Agent - Iteration 1") as demo:
    gr.Markdown("# 🖥️ NL to CLI Agent (Groq Speed!)")
    with gr.Row():
        input_text = gr.Textbox(label="Instruction")
        output_text = gr.Textbox(label="Generated Command")
    submit_btn = gr.Button("Generate")
    submit_btn.click(fn=translate_to_cli, inputs=input_text, outputs=output_text)

if __name__ == "__main__":
    demo.launch()