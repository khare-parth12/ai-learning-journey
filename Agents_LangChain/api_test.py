from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()   # copies the keys in .env into the environment

model = init_chat_model("groq:openai/gpt-oss-120b", temperature=0)
print(model.invoke("In one sentence, what is LangChain?").text)