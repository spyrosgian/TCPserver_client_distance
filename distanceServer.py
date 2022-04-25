# Importing necessary Python packages:
import socket
import pickle

# Taking integer values for start, end and increment
# and then returning a two-dimensional array:
def table(s, e, i):
    s1 = "*****************************"
    s2 = "*Speed (mph)*Distance (feet)*"
    table = s1 + "\n" + s2 + "\n" + s1 +"\n"
    for speed in range(s, e + i, i):
        distance = (speed ** 2) // 20 + speed
        row = ("*%5s      *%8s       *\n" % (str(speed), str(distance)))
        table += row
    table += s1
    return table

# Defining server constants:
SERVER = ""
PORT = 5000
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
HEADER = 8192


# TCP receiving and sending messages from and to the client:
print(f"[STARTING] Server with IP {SERVER} is starting (port {PORT})...")

# Creating TCP server socket:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding server socker to Local IP and selected port:
server.bind(ADDR)
print(f"[STARTED] Server with IP {SERVER} is running (port {PORT}).")

# TCP listening for client connections:
print(f"[LISTENING] Server with IP {SERVER} is waiting for connection (port {PORT})... ")
server.listen()
try:
    while True:
        dataclient, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        # Receiving data from client:
        s_e_i = dataclient.recv(HEADER).decode(FORMAT)
        print(f"[RECEIVING] Receiving from client: {addr} - Message received: {s_e_i}")
        
        # Splitting received data to create start, end and increment:
        l = s_e_i.split(" ")
        s = int (l[0])
        e = int (l[1])
        i = int (l[2])

        # Calling convert function (which returns a two dimensional array),
        # and from that creating 2 distinct lists for speed and distance:
        tab = table(s, e ,i)
        
        # Sending list to the client:
        print(f"[SENDING] Sending to client: {addr} - Table sent: {tab}")
        send_table = pickle.dumps(tab)
        dataclient.send(send_table)

        # Closing client socket:
        dataclient.close()
finally:
    # Closing server socket:
    server.close()


