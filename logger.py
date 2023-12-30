import requests
import json

MessageLimit = 100
ChannelId = 0 # Channel Id Here #
URL = f"https://discord.com/api/v9/channels/{ChannelId}/messages?limit={MessageLimit}"
TOKEN = ""

with open("token","r") as file:
    TOKEN = file.read()


response = requests.get(URL,headers={
    "Authorization": TOKEN
})

JsonData = json.loads(response.text)

with open("data.json","w") as file:
    file.write(response.text)

for Person in JsonData:
    print(f'{Person["author"]["global_name"]}:{Person["content"]}')
