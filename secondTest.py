import os
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Tu es un assistant intelligent"},
    {"role": "user", "content": "Explique simplement ce que tu es"},
    ],
    temperature=0,
)

print(completion['choices'][0]['message']['content'])