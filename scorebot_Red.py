#! /usr/bin/env python

"""
A simple echo server for Red Team to connect to for scoring.
"""

import socket
import time

class RedServer:
    def _init_(self):
        self.HOST = socket.AF_INET
        self.PORT = 50000
        self.BUFFERSIZE = 1024
        self.ADDRESS = (self.HOST,self.PORT)
        self.blueClientComputers = []
        self.COMPETITION_CLOCK = time.time();
        self.roundNumber = 0
        self.running = True
        self.serversocket = socket.socket()
        self.serverSock.bind(self.ADDRESS)
        self.serverSock.listen(5)
        self.clientThread.start()
        print("Waiting for callbacks...")
        while self.running:
            clientInfo = self.serverSock.accept()
            data = clientInfo[0].recv(size)
            print("Callback connected from {}.".format(clientInfo[1]))
            #If at the end of a round; Rounds last 10 minutes.
            if (time.time() - self.COMPETITION_CLOCK) == 10:
                #Reset the competition clock to the current time and update the round.
                self.COMPETITION_CLOCK = time.time();
                self.roundNumber++
                #Check to see if data was recieved by a red team call back. If so, send their
                #data right back at them, and give them a score.
                if data:
                    clientInfo[0].send(data)
                    scoreRed(true, clientInfo)
                else:
                    scoreRed(false, clientInfo)
            
        self.serverSock.close()
        print("- end -")

    def scoreRed(checkIfRedScored, clientInfo):
        points = 0
        if checkIfRedScored:
            points = 1
        
        f = open('redscore.txt', 'w')
        f.write("Red Team scored " + points + " point(s) for Round " + roundNumber + "from the following address: \n")
        f.write(clientInfo[0] + " " clientInfo[1] + "\n")
        f.close()


srvr = redServer()
