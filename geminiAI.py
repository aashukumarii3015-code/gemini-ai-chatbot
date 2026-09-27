from google import genai

api="YOUR_GEMINI_API_KEY" # Replace with your own Gemini API key

client = genai.Client(api_key=api)

 

# print(interaction.output_text)


while (1):
    prompt = input("User: ")
    interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input=prompt or "no prompt given"
    )
    print("AI: " + interaction.output_text)
   
    


