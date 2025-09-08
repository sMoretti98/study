from openai import OpenAI

client = OpenAI()

user_prompt = input("Enter a prompt: ")
system_prompt = "You are a helpful assistant."

response = client.chat.completions.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)
