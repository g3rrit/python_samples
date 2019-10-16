import socket
import sys

URL = b"send.htwk-leipzig.de"
PORT = 25
SRC = "christoph.siegert@stud.htwk-leipzig.de"
DST = "christoph.siegert@stud.htwk-leipzig.de"
SUB = "test"
DATA = "hi"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (URL, PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

def rall():
    r = ' '
    while r != '\n':
        r = sock.recv(1)
        print(r)

try:
    rall()

    # EHLO test.example.com
    # MAIL FROM: Absenderadresse
    # RCPT TO: Empfaengeradresse
    # DATA
    # Subject: Testnachricht
    # newline
    # DATA
    # newline
    # .
    # QUIT
    msgs = [b"HELO " + URL, "MAIL FROM: " + SRC, "RCTP TO: " + DST, "DATA", "Subject: " + SUB, "\r\n", DATA, "\r\n", ".", "QUIT"]

    for msg in msgs:
        print("sending: " + msg + b"\r\n")
        sock.sendall(msg)
        rall()
finally:
    print('closing socket')
    sock.close()
