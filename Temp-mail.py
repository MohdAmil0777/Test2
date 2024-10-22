#This Tool is made by HERON AFRIDI 
 
 
try:
	import requests as r, random, json, os , time, sys
	from time import sleep
except ModuleNotFoundError:
	exit("[!] Module not installed")


Heron_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
url = "https://cryptogmail.com/"
num = 0
from os import system as HERON

def get_teks(accept, key):
	cek = r.get(url+"api/emails/"+key, headers={"accept": accept}).text
	if "error" in cek:
		return "-"
	else:
		return cek.strip()



def get_random(digit):
	lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
	dig = [random.choice(lis) for _ in range(digit)]
	return "".join(dig), random.choice(Heron_mail)

def animate(teks):
	lis = list("😁🦉🥱🙃😂😏🥴😑💬🍎😹😻😘😍😍🤐😐🤫🤭🐲😆😅🤣😔🥺🧐😳👿😈💋🖕🤲")
	for cy in lis:
		print(f"\r"+str(teks)+"..."+cy+"    ", end="")
		sleep(0.5)
		
def ___HERON___(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
HERON ("pkg install espeak")
def run(email):
	while True:
		try:
			colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m'])
			animate(f" \t{colorful}WAITING FOR YOUR MESSAGE")
			HERON("espeak \"waiting for your message\"")
			raun = r.get(url+"api/emails?inbox="+email).text
			if "404" in raun:
				continue
			elif "data" in raun:
				z = json.loads(raun)
				for data in z["data"]:
					HERON ("espeak \"you get a message \"")
					print("\r[♞] ID: "+data["id"], end="\n")
					got = json.loads(r.get(url+"api/emails/"+data["id"]).text)
					pengirim = got["data"]["sender"]["display_name"]
					email_pe = got["data"]["sender"]["email"]
					subject  = got["data"]["subject"]
					print("\r[♞] Sender Name: "+pengirim, end="\n")
					print("\r[♞] Sender mail: "+email_pe, end="\n")
					print("\r[♞] Subject    : "+subject, end="\n")
					atc = got["data"]["attachments"]
					if atc == []:
						print("\r[♞] attachments: -", end="\n")
					else:
						___HERON___("[♞] attachments: ")
						for atch in atc:
							id = atch["id"]
							name = atch["file_name"]
							name = name.split(".")[-1]
							svee = r.get("https://cryptogmail.com/api/emails/"+data["id"]+"/attachments/"+id)
							open(id+"."+name, "wb").write(svee.content)
							print("      ~ "+id+"."+name)
					___HERON___("-"*45)
					r.delete(url+"api/emails/"+data["id"])
				continue
			else:
				continue
		except (KeyboardInterrupt,EOFError):
				exit("\n[✓] Program finished, exiting...\n")
				HERON("espeak \"Program finished, exiting.\"")

def heron():
	print("""\n\033[1;90m██   ██ ███████ ██████   ██████ \033[1;91m ███    ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██\033[1;91m ████   ██ \n\033[1;90m███████ █████   ██████  ██    ██\033[1;91m ██ ██  ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██\033[1;91m ██  ██ ██ \n\033[1;90m██   ██ ███████ ██   ██  ██████  \033[1;91m██   ████\n\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30mAUTHOR        \033[1;35m:  \033[1;37mHERON AFRIDI      \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30mGITHUB        \033[1;35m:  \033[1;37mheroncyber99      \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30mWHATSAPP      \033[1;35m:  \033[1;37m01722183463       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30mPOWER         \033[1;35m:  \033[1;31mHERON AFRIDI      \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n""")


def main():
	os.system('clear')
	global num
	heron()
	___HERON___ ('\033[1;92m[\033[1;92m01\033[1;92m]\033[1;97m RANDOM EMAIL')
	___HERON___ ('\033[1;92m[\033[1;92m02\033[1;92m]\033[1;97m CUSTOM EMAIL  [BEST]')
	___HERON___ ('\033[1;92m[\033[1;92m03\033[1;92m]\033[1;97m FOLLOW MY PAGE')
	os.system('xdg-open https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN')
	print('____________________________________________________')
	print (' ')

	pil = input("\033[1;92m[\033[1;92m•\033[1;92m] \033[1;97mCHOOSE: \033[1;97m")
	while pil == "" or not pil.isdigit():
		pil = input("\033[1;92m[\033[1;97m?\033[1;92m] \033[1;97mCHOOSE: \033[1;97m")
	if pil in ["01","1"]:
		HERON("espeak \"you choose random temp mail\"")
		set_name, set_email = get_random(10)
		HERON("espeak \"hare is your email\"")
		print("\n\033[1;92m[\033[1;92m•\033[1;92m] \033[1;97mYOUR EMAIL: "+set_name+"@"+set_email)
		print("\033[1;97m-"*45)
		run(set_name+"@"+set_email)
	elif pil in ["02","2"]:
		HERON("espeak \"import your email name\"")
		set_name = input("\033[1;92m[\033[1;92m•\033[1;92m] \033[1;97mSET MAIL NAME: ")
		print()
		for cy in Heron_mail:
			num += 1
			print(" "*5,"["+str(num)+"] @"+cy)
		print()
		set_email = input("\033[1;97m[\033[1;97m•\033[1;97m]\033[1;97m SELECT: ")
		while set_email == "" or not set_email.isdigit() or int(set_email) > len(Heron_mail):
			set_email = input("[•] Select: ")
		mail = Heron_mail[int(set_email)-1]
		print("\n\033[1;97m[\033[1;97m+\033[1;97m] YOUR EMAIL: "+set_name+"@"+mail)
		print("-"*45)
		run(set_name+"@"+mail)
	elif pil in ["03","3"]:
		HERON("espeak \"please follow me on Facebook\"")
		os.system('xdg-open https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN')
		time.sleep(2)
		print (" ")
		n = input("[ \033[1;97mEnter \033[1;97m]")
		time.sleep(2)
		main()
		
if __name__ == "__main__":
	main()
