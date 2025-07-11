from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message.content )
