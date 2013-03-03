#! /usr/bin/env python

"""
A simple echo server for Red Team to connect to for scoring.
"""

import socket
import time

COMPETITION_CLOCK = time.time();
host = ''
port = 50000
backlog = 5
size = 1024
roundNumber = 0
redCallback = false
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(backlog)
while 1:
    client, address = serversocket.accept()
    data = client.recv(size)
    if data:
        client.send(data)
        if updateRound():
            scoreRed(true)
    else:
        if updateRound():
            scoreRed(false)
    client.close() 

def scoreRed(checkIfRedScored):{
    points = 0
    if checkIfRedScored:
       points = 1 
    
    f = open('redscore.txt', 'w')
    f.write("Red Team scored " + points + " point(s) for Round " + roundNumber)
    f.close()
}

def updateRound():{    
    isEndOfRound = false
    if (time.time() - COMPETITION_CLOCK) == 10:
        isEndOfRound = true
        COMPETITON_CLOCK = time.time()
        roundNumber++
    return isEndOfRound
}
