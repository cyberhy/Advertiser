import requests
import time
from colorama import Fore, init
from config import *

init(autoreset=True)

Token = "TokenHere"

ChannelID = input("Channel ID>")
Message = input("Message>")
Delay = input("Delay>")
IntDelay = int(Delay)
Amount = input("How many times to send the message>")
IAmount = int(Amount)
IntAmount = IAmount + 1
URL = f"https://discord.com/api/v9/channels/{ChannelID}/messages"

Headers = {
	"Authorization": Token,
    "Content-Type": "application/json",
}

Payload = {
    "content": Message,
}

def sendrequest():
	request = requests.post(URL, headers=Headers, json=Payload)
	status = request.status_code
	if status == 200:
		print(f"{Fore.GREEN}sent message")
	else:
		print(f"{Fore.RED}something went wrong")

for _ in range(1, IntAmount):
	sendrequest()
	time.sleep(IntDelay)