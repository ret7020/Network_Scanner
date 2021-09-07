import socket

def check_port(host, port):
	sock = socket.socket()
	try:
		sock.connect((host, port))
		return True
	except:
		return False

host = input()
ports = {22 : "ssh", 80 : "http", 21 : "ftp", 20 : "ftp", 23 : "telnet",
		25 : "smtp", 53 : "dns", 79 : "finger", 110 : "pop3", 111 : "sun rpc",
		119 : "NNTP", 139 : "net bios", 443 : "secure http", 513 : "rlogin"}
for port in range(1, 1001):
	if check_port(host, port):
		print(port, "- Open - for", ports[port])
