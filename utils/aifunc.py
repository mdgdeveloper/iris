# Connections to OpenAI 
import os
from openai import AzureOpenAI

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_ENDPOINT")

def createAiResponse(destination, content, emailTone, previous=None ):
  client = AzureOpenAI(
      api_version = "2023-07-01-preview",
      azure_endpoint = azure_endpoint,
      api_key = api_key
)
  
  user_msg_content = f"destination: {destination}. {"" if previous==None else f"Responding to email: {previous}"}. Email content: {content}. Email tone: {emailTone}"

  role_msg = { "role": "system", "content": "You are an AI assistant that helps people to write emails"}
  user_msg = {"role":"user","content":user_msg_content}

  completion = client.chat.completions.create(
      model="ucefdev-gpt4",  # e.g. gpt-35-instant
      messages=[
          role_msg,
          user_msg
      ],
  )
  result = completion.choices[0].message.content

  # Remove first line of result, to create the variable subject with it 
  subject = result.splitlines()[0]
  mailcontent = result.splitlines()[1:]


  return {"subject": subject, "content": mailcontent}