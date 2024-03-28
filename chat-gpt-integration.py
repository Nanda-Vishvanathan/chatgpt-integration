from openai import OpenAI

client = client = OpenAI(
    api_key="###############################",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"user", "content":"Lets talk about chatgpt-integration; shall we?"
        }
    ]
)

print("Completion::", completion[0].message)