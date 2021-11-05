import os
os.system("pip3 install amino-new.py==4.2.2")
import time
from os import path
from time import sleep
import json
from amino import Client
from amino.lib.util.exceptions import *
from concurrent.futures import ThreadPoolExecutor
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet

colorama.init()
print(colorama.Fore.GREEN)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('TECH'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('VISION'))
f = pyfiglet.Figlet(font='digital')
print (f.renderText('Online Bot'))
dec = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' 
print("""
Youtube:
https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg

Discord Server:
https://discord.gg/YMfvAxm6zF
""")
print(dec)
THIS_FOLDER=path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,'accounts.json')

link=input("Paste community link :")
xd=Client().get_from_code(link)
cid=xd.path[1:xd.path.index("/")]

dictlist=[]
with open(emailfile)as f:
	dictlist=json.load(f)

def online_bot(cli, comId):
        data = {
            "o": {
                "actions": ["Browsing"],
                "target": f"ndc://x{comId}/",
                "ndcId": int(comId),
                "id": "82333"
            },
            "t":304}
        data = json.dumps(data)
        sleep(2)
        cli.socket.send(data)

def log(cli : Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
        print(f'\33[0m'+dec+f"\nLogged in with {email}")
    except Exception as t:
    	print(t)
        	
def threadit(acc : dict):
	email=acc["email"]
	password=acc["password"]
	client=Client()
	log(cli=client,email=email,password=password)
	client.join_community(comId=cid)
	online_bot(cli=client,comId=cid)
	print(f'\33[0m'+ dec+ f" \n{email} is Online")
	client.logout()
    
def main():
    print(f'\33[0m' +dec+ f" \nTotal accounts : {len(dictlist)}")
    for amp in dictlist:
    	threadit(amp)
    print(f'\33[0m'+ dec+ f"\nAll the {len(dictlist)} accounts are online in the community")
    time.sleep(300)

if __name__ == '__main__':
    while True:
    	main()  