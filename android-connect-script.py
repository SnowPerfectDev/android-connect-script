import subprocess
import time
import sys

while True:
    try:
        output = subprocess.check_output(['adb', 'connect', f'{sys.argv[1]}:5555'], stderr=subprocess.STDOUT, text=True)
        if "connected" in output:
            print("[!] SUCESSO!! Conectado a", f"{sys.argv[1]}:5555")
            print("[+] pegando shell")
            time.sleep(1)
            subprocess.call(['adb', 'shell'], stderr=subprocess.DEVNULL)
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        pass
    
    print("[*] Conectando...")
    time.sleep(0.20)
