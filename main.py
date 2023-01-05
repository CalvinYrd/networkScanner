import subprocess, socket, os

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

def ipExists(ip_address):
	result = subprocess.run(["ping", "-n", "1", ip_address], stdout=subprocess.PIPE)
	result = result.stdout
	return b"Impossible" not in result

def getPotentialIps(ip):
	pass

############################
########### MAIN ###########
############################

clear()
ip = input("Saisissez l'adresse IP et le masque sous réseau (<IP>/<MASQUE>)")
ips = getPotentialIps(ip)

"""

 x . x . x . x
 0 . 1 . 2
 8 . 16. 24

"""


