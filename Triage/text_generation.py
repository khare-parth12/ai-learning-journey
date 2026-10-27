from groq import Groq

client = Groq()  # reads GROQ_API_KEY from the environment

stream = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "Write a one-sentence apology to a customer whose parcel is late."}],
    stream=True,
)
for chunk in stream:
    piece = chunk.choices[0].delta.content
    if piece:
        print(piece, end="|")
print()