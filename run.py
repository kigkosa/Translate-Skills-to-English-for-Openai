import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

with open('Skills.txt', 'r',encoding="utf-8") as f:
   contents = f.read().split('#')
data = []
for tx in contents:
    if tx:
        text = "This translation is English '"+tx+"'"
        response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0, max_tokens=100)
        data.append(response['choices'][0]['text'].strip('\n'))
with open('Skills_en.txt','w') as f:
    for d in data:
        f.write('#'+d+'\n')

print("สำเร็จ")