import socket, subprocess, os

logo = '''
 ____  _                     _   __       
/ ___|| |__   __ _ _ __ ___ (_) / _|_   _ 
\___ \| '_ \ / _` | '__/ _ \| || |_| | | |
 ___) | | | | (_| | | |  __/| ||  _| |_| |
|____/|_| |_|\__,_|_|  \___||_||_|  \__, |
                                    |___/ 
                                
                                -- Akash koiri
'''

print(logo)

def get_ip(opt):
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    if opt == 1 or opt == 'Upload' or opt == 'upload':
        print(f"\nIP Address: {ip}/upload\n")
    elif opt == 2 or opt == 'Download' or opt == 'download':
        print(f"\nIP Address: {ip}\n")
    elif opt == 3:
        exit()
    else:
        print('Please enter a correct option')

def runserver():
    cmd = 'python -m uploadserver 80'
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)


print('\n**Notice: Make sure your devices are connected in the same network')
print('\n1. Upload\n2. download\n3. Exit')
opt = int(input('\nWhat do you want to do:'))

get_ip(opt)
runserver()

