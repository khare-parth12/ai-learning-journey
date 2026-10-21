from importlib.metadata import version

from groq import Groq

print("groq", version("groq"))

client = Groq()  # reads GROQ_API_KEY from the environment
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "Reply with the single word: ready"}],
)
print(response.choices[0].message.content)