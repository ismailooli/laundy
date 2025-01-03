import openai
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Securely handle the API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Function to encode image to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Encode the image
image_path = "path_to_your_image.jpg"
base64_image = encode_image_to_base64(image_path)

# Prepare the API request
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "This is a laundry care label. Please analyze it and provide:\n"
                       "1. Washing temperature\n"
                       "2. Cycle type\n"
                       "3. Washing instructions\n"
                       "4. Drying instructions\n"
                       "5. Ironing instructions\n"
                       "6. Any special care instructions\n"
                       "Be concise and direct."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }
]

# Make the API request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Print out the response
print(response.choices[0].message['content'])