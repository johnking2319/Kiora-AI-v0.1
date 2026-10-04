from google import genai
question=input("You :")
client=genai.client(api_key="")
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

print("Kiora AI :",response.text)