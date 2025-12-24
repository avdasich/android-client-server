import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.REP)

sock.bind("tcp://*:2222")
print("[SERVER] ZMQ server started on port 2222")

counter = 0

while True:
    msg = sock.recv_string()
    counter += 1
    print(f"[SERVER] #{counter} got: {msg}")

    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"{counter}: {msg}\n")

    sock.send_string("Hello from Server!")
