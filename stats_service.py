# Statistics Analyzer microservice
#
# Waits for requests through ZeroMQ, calculates the stats each request
# asks for, and sends the answer back as JSON.
#
# Run it with:  python3 stats_service.py

import json
import zmq

import MinMax
import ThreeMs
import UniqueValues

context = zmq.Context()

# REP socket: waits for a request, then sends back one reply
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")
print("Statistics Analyzer is waiting for requests on port 5556.")

while True:
    # wait for the next request
    message = socket.recv().decode()
    print(f"Received request: {message}")

    # a "Q" message stops the microservice
    if message == "Q":
        break

    request = json.loads(message)

    # the stat functions take a table (a list of rows), so the values go in as one row
    table = [request["values"]]

    # add one answer to the reply for each stat the request asks for
    reply = {}
    for stat in request["stats"]:
        if stat == "min":
            maxValue, minValue = MinMax.minMax(table)
            reply["min"] = minValue
        elif stat == "max":
            maxValue, minValue = MinMax.minMax(table)
            reply["max"] = maxValue
        elif stat == "mean":
            meanAverage, medianMiddle, modeRepeat = ThreeMs.threeMs(table)
            reply["mean"] = meanAverage
        elif stat == "median":
            meanAverage, medianMiddle, modeRepeat = ThreeMs.threeMs(table)
            reply["median"] = medianMiddle
        elif stat == "mode":
            meanAverage, medianMiddle, modeRepeat = ThreeMs.threeMs(table)
            reply["mode"] = modeRepeat
        elif stat == "unique":
            reply["unique"] = UniqueValues.uniqueValues(table)

    # send the reply back as JSON text
    reply_text = json.dumps(reply)
    socket.send_string(reply_text)
    print(f"Sent reply: {reply_text}")

# close ZeroMQ before the program ends
context.destroy()
