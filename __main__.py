import socket, sys
def main(site):
        try:
            ips = socket.gethostbyname_ex(site)
            # ips = socket.getprotobyname(site)
        except socket.gaierror:
            ips=[]
        return ips
try:
    site = sys.argv[1]
    ips = main(site)
    print(repr(''.join(ips[2][0])))
except IndexError:
    print("You Need To Specify The Website!")
