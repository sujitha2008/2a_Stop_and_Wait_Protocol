import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)
print("Server waiting for connection...")
conn, addr = server.accept()
print("Connected to client\n")
expected_seq = 0
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    seq, frame = data.split(":")
    if int(seq) == expected_seq:
        print(f"Received: {frame} (Seq: {seq})")
        conn.send(f"ACK{seq}".encode())
        expected_seq = 1 - expected_seq
    else:
        print("Duplicate frame received")
        conn.send(f"ACK{1 - expected_seq}".encode())
conn.close()
server.close()