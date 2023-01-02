import subprocess

def ipExists(ip_address):
	result = subprocess.run(["ping", "-n", "1", ip_address], stdout=subprocess.PIPE)
	result = result.stdout
	return b"Impossible" not in result

print(ipExists("8.8.8.8"))
