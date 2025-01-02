#API KEY
api_key = 3
#start up the ChatGPT model
client = OpenAI(api_key=api_key)

#Encode the image in a way we can send it to ChatGPT

#Make the API request as such 

    # messages = [
    #     {
    #         "role": "user",
    #         "content": [
    #             {
    #                 "type": "text",
    #                 "text": "This is a laundry care label. Please analyze it and provide:\n"
    #                        "1. Washing temperature\n"
    #                        "2. Cycle type\n"
    #                        "3. Washing instructions\n"
    #                        "4. Drying instructions\n"
    #                        "5. Ironing instructions\n"
    #                        "6. Any special care instructions\n"
    #                        "Be concise and direct."
    #             },
    #             {
    #                 "type": "image_url",
    #                 "image_url": {
    #                     "url": f"data:image/jpeg;base64,{base64_image}"
    #                 }
    #             }
    #         ]
    #     }
    # ]


#Print out the response 