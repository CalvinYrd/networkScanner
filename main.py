import subprocess, os, colorama

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

def ipExists(ip_address):
	result = subprocess.run(["ping", "-n", "1", ip_address], stdout=subprocess.PIPE)
	result = result.stdout

	errors = [
		"Impossible",
		"lai d'attente de la demande d"
	]
	exists = ((errors[0].encode() not in result) and (errors[1].encode() not in result))
	return exists

def getIpsRange(start_ip, end_ip):
	start = list(map(int, start_ip.split(".")))
	end = list(map(int, end_ip.split(".")))
	temp = start
	ips = []

	while temp != end:
		ips.append(".".join(map(str, temp)))
		temp[3] += 1
		for i in (3, 2, 1):
			if temp[i] == 256:
				temp[i] = 0
				temp[i-1] += 1
	ips.append(".".join(map(str, temp)))
	return ips

def getPotentialIps(ip):
	# constitution obj ip
	ip = ip.split("/")
	ip[0] = [int(i) for i in ip[0].split(".")]
	ip[1] = int(ip[1])

	# constitution de l'adresse réseau
	index = int(ip[1] / 12)
	for i in range(len(ip[0])):
		if (i > index):
			ip[0][i] = 0

	# constitution des adresses potentielles
	ip = [str(i) for i in ip[0]]
	ip = ".".join(ip)
	ip = [ip, ip.replace(".0", ".255")]

	ips = getIpsRange(ip[0], ip[1])
	return ips

############################
########### MAIN ###########
############################

clear()
baseIp = input("Saisissez l'adresse IP et le masque sous réseau (<IP>/<MASQUE>) :\n> ")
netMask = baseIp.split("/")[1]
try:
	ips = getPotentialIps(baseIp)
	foundedIps = []

	for i in range(len(ips)):
		clear()
		message = f"Scan du réseau en cours... (n°{i+1}/{len(ips)} : {colorama.Fore.GREEN+ ips[i]}/{netMask + colorama.Fore.RESET})\n\n"

		for ip in foundedIps:
			ip = colorama.Fore.RED + ip + "/" + netMask + colorama.Fore.RESET

			message += f"Adresse ip ({ip}) trouvée dans le réseau ({colorama.Fore.CYAN + baseIp + colorama.Fore.RESET}) \n"

		print(message)
		exists = ipExists(ips[i])
		if (exists): foundedIps.append(ips[i])

except :
	clear()
	print("Une erreur est survenue, l'adresse IP saisie semble incorrecte\nil est possible que vous ayez oublié le masque")

