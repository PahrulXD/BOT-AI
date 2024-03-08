import requests, json, os

logo = ("""
888888b.            888                d8888 d8b 
888  "88b           888               d88888 Y8P 
888  .88P           888              d88P888     
8888888K.   .d88b.  888888          d88P 888 888 
888  "Y88b d88""88b 888            d88P  888 888 
888    888 888  888 888           d88P   888 888 
888   d88P Y88..88P Y88b.        d8888888888 888 
8888888P"   "Y88P"   "Y888      d88P     888 888 
 """)

def bot():
	os.system ("clear")
	print ("\033[1;95m"+logo)
	print ("\033[1;97m- Coding By : Pahrul Aguspriana X\n")
	while True:
		pesan = input ("\033[1;91m> \033[1;97mYOU : \033[1;92m")
		if pesan in ["stop","Stop"]:exit()
		ai = requests.get(f"https://langapi.cyclic.app/api/openai?text={pesan}")
		data = ai.json()
		print ("\033[1;91m> \033[1;97mBOT :\033[1;96m\n"+data["result"])
			
			
bot()