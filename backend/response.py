import openai
from dotenv import load_dotenv
import base64
import os
from openai import OpenAI

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_response(image_path,question):
    base64_image = encode_image(image_path)
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": question},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
        stream= True,
    )
    for event in response:
        yield event
        

