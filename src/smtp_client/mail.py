import socket
import sys

URL = "smtp.mail.com"
PORT = 25
SRC = "sender@mail.com"
DST = "recipient@mail.com"
DATA = "Subject: ...\r\nHello"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (URL, PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

def rall():
    r = ' '
    try:
        while r != b"\n":
            r = sock.recv(1)
            print(r.decode(), end = "")
    except Exception as e:
        print("unable to recv on host: " + str(e))

try:
    rall()

    # HELO test.example.com
    # MAIL FROM: Absenderadresse
    # RCPT TO: Empfaengeradresse
    # DATA
    # Subject: Testnachricht
    # newline
    # DATA
    # newline
    # .
    # QUIT
    msgs = ["HELO " + URL, "MAIL FROM: " + SRC, "RCPT TO: " + DST, "DATA", DATA + "\r\n.", "QUIT"]

    for msg in msgs:
        msg = msg + "\r\n"
        print("\n########################################")
        print("sending: " + msg)
        sock.sendall(str.encode(msg))
        print("receiving: ", end = "")
        rall()
        print("-----------------------------------------")
finally:
    print('closing socket')
    sock.close()
