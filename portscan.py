"""
TCP Connect Scan - Port Scanner
"""
import argparse
from socket import *
from threading import *

'''Below line prevents printing inconsitances with threaded connscans'''
ScreenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSoc = socket(AF_INET, SOCK_STREAM)
        connSoc.connect((tgtHost,tgtPort))
        connSoc.send(bytes('KnockKnock\r\n', 'UTF-8'))
        results = connSoc.recv(100)
        ScreenLock.acquire()
        print("[+]",tgtPort,"open")
        print("    [RESP]", str(results))
        connSoc.close()
    except:
        ScreenLock.acquire()
        print("[-]",tgtPort,"closed")
    finally:
        ScreenLock.release()
        connSoc.close()
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve", tgtHost,": Unknown host")
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for:', tgtName[0])
    except:
        print('\n[+] Scan Results for:', tgtIP)
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
def main():
    # Arg Parsing
    parser = argparse.ArgumentParser(description='Scan some ports for lulz.')
    parser.add_argument("-H","-host", help="Target Host IP or URL")
    parser.add_argument("-p","-port", help="Targeted Port(s), comma delimited")
    args = parser.parse_args()
    tgtHost = args.H
    tgtPorts = str(args.p).split(',')
    # Check args present and set variables
    if (tgtHost == None) | (tgtPorts[0] == None):
        parser.print_help()
        exit(0)
    portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
    main()

exit(0)
