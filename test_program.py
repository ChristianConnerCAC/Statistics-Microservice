# Test program for the Statistics Analyzer microservice
#
# Sends one request through ZeroMQ and prints the reply.
#
# Start the microservice first, then run this
# in a 2nd terminal with: python3 test_program.py

import json
import zmq

context = zmq.Context()

# REQ socket: sends a request, then waits for the reply
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# ask for all six statistics of the numbers 2, 4, 4, 10
request = {
    "values": [2, 4, 4, 10],
    "stats": ["mean", "median", "mode", "min", "max", "unique"],
}

request_text = json.dumps(request)
socket.send_string(request_text)
print(f"Sent request: {request_text}")

# wait for the reply and turn the JSON text back into a dictionary
reply = json.loads(socket.recv().decode())
print(f"Received reply: {reply}")

# the test is done, so tell the microservice to stop
socket.send_string("Q")

# close ZeroMQ before the program ends
context.destroy()
