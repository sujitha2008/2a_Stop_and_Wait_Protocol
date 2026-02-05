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