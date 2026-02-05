# 2a_Stop_and_Wait_Protocol
## AIM 
To write a python program to perform stop and wait protocol
## ALGORITHM
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM
# Server.py:
```
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
```
# Client.py:
```
import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
frames = ["Frame 1", "Frame 2", "Frame 3", "Frame 4"]
seq = 0
for frame in frames:
    print(f"Sending: {frame} (Seq: {seq})")
    client.send(f"{seq}:{frame}".encode())
    ack = client.recv(1024).decode()
    print(f"Received {ack}\n")
    if ack == f"ACK{seq}":
        seq = 1 - seq  
        time.sleep(1)
    else:
        print("ACK not correct. Retransmitting...\n")
client.close()
```
## OUTPUT
# Server
![alt text](<Screenshot 2026-02-05 110806 copy.png>)
# client
![alt text](<Screenshot 2026-02-05 110858.png>)

## RESULT
Thus, python program to perform stop and wait protocol was successfully executed.
