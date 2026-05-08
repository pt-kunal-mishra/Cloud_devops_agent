import os
import getpass
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

region=os.getenv('AWS_Region')
AWS_S3_bucket=os.getenv('AWS_S3_bucket')
model_id=os.getenv('GROQ_API_KEY')

# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
# os.environ["LANGSMITH_TRACING"] = "true"

llm=ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.7,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,  
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

