------------------------------WVU ACDC Gold Team Scorebots-------------------------------------

The Gold Team will be handling the scoring for both the Red Team and the Blue Team. For the current network setup, Gold Team will have a machine living within its own VLAN, and have the ability to reach out and probe both the Red and Blue team VLANs. As with other CCDC'esque inherit and defend competitions, Blue Team will be scored on availability of services, and asset consistency. Red Team will be scored primarily on their ability to call back to machines from within the Blue Team network. As Red Team gains access to Blue Team's computers, they will send their call backs to the Gold Team's server, thus scoring them a point. Alternatively, Blue Team will do their best to keep services running and exposed to the world. This will allow the Gold Team to view and track the availability of their services.

Tools we are using:
------------------
1. Apache - To monitor the Blue Team network via the Nagios webview
2. Nagios - For monitoring Blue Team. Also, we will make use of the pre-built scripts Nagios uses to check services (HTTP, SSH, etc.)
3. PHP - To run a voting script (See Voting section)
4. MySQL - For diffing the database of votes on our server and the one from Blue Team's database
5. FTP - For Red Team to send tokens (stolen ssh keys, dump of Blue's database, stolen passwords, etc.)

Gold Server Setup:
-----------------
Ubuntu 12.04, running LOUD meta distro

Package List:
* php5
* php5-mysql - for voting script
* nagios3
* apache2
* mysql-server-5.5
* ftp
* emacs
* python 2.7.3
* git (^_^)


Voting:
--------------
For WVU's ACDC Competition 2, we are holding a "primary for the upcoming elections" and need a voting populus. Since Blue Team will be busy keeping out the Red Team, Gold Team has taken the liberty of filling the Blue Team's database with votes. This script will run in PHP, and was developed by a college of mine, Barry Martin. The script will write to the Blue Team's voting database randomly, and will vote for candidates at random too. Part of the Blue Team scoring will be to check if their database of votes has been compromised. To do this, we will write the randomized votes to a database living on our own server as well. When it comes time to check Blue's database, we will diff it against our own. If they are the same, then we know for a fact that the Red Team didn't affect the outcome of the votes. If they are different, then it is ensured that the Red Team stuffed (or removed votes from) the ballot box, which will in turn penalize the Blue Team.


Scoring Rounds:
-------------------------
Each team will follow a set of rounds that they can score points in. Each round will last 10 minutes, so if the event starts at 6PM and goes until 8PM, we have a total of 12 rounds. The scorebot for the Blue Team will check the Blue Team's network every 10 minutes and score according. 

For the Blue Team, scoring works like golf: the lower the score, the better. If our scorebot goes in and sees that SSH is open to the world, Blue Team will receive 0 points for that service. If it sees that SSH is down or closed, it will receive a score of 10 for the round.

The exact opposite works for Red Team. Red Team wants to callback to our server during each round. If Blue has 4 machines in their network, and Red Team calls back from each machine for Round 1, then at the end of Round 1, Red Team will receive 4 points. 

A perfect score for Red Team in this case would be 48 points. This would mean that Red Team was able to gain access to every machine within the first 10 minutes, and keep access for the entire 2 hours. Blue Team will be rendered incompetent if Red Team scores a full 48 points.


Scorebot for Red Team:
-------------------------
The scorebot for Red Team is a simple echo server for the Red Team callback scripts to hit. The server will keep track of where the callback came from, and at the end of each Round, will log to a file each location of the callback, the round number, how many points were scored for that round, and the total points Red Team has scored so far.

If Red Team does not successfully callback within a round, it will write to the scoring file accordingly.

At the end of the competiton, the file "redscore.txt" will contain each rounds scores and the total score for the Red Team.

Finally, the Red Team will attempt to grab various tokens for show and tell after the competiton completes. These tokens are not currently scored, but only to demonstrate the abilities of the Red Team. The Gold Team will setup an FTP server for Red Team to send these tokens to.


Scorebot for Blue Team:
------------------------
The scorebot for Blue Team will be run automatically every 10 minutes to check the following state of services within their network:

Tier 1 - Is the service running?
Tier 2 - Is the port open to the world?å
Tier 3 - Is the content from the service valid?

Each tier has a point value associated with it. As we stated earlier, Blue Team will be scored like golf. If our scorebot doesn't see that SSH is running, then they will be given 10 points. The tiers are as follows:

Tier 1 - 10 points
Tier 2 - 5 points
Tier 3 - 2 points

Another example: If the service is running, but the port is closed, then Blue Team will recieve 5 points. For a service such as Apache, if Blue passes tier 1 and 2, we will wget their index.html page. Our server will have a copy of Blue Team's index.html, so we will diff it against our copy. If there isn't a difference in the html pages, then Blue will pass the third tier of checks and recieve no penalty for that round. However, if Red Team defaces the homepage of the Blue Team's webserver, then our diff will come back positive. Blue Team will then be given 2 points for that service for the corresponding round.

The following are the services that we will be checking for Blue Team's network:

* Apache - 80
* MySQL - 3306
* Windows Sharing - 445
* SSH - 22

The following are the assets that we will be collecting from the blue team for our tier 3 checks:

* Wordpress homepage
* Voting application written in PHP (Different from the voting application running on our Gold server)
* Database of votes
* Can we SSH in?

Nagios will come in handy for Blue Team's scorebot, as it already has scripts in place to check popular services. We will simply implement the scripts Nagios already has in place and parse out the information that it returns for scoring tier 1 and 2.

Final Notes
-------------------------------------------
Contributors to Gold Team score bots and scripts:  
Adam Minter, Naveen Kumar, Barry Martin, and David Krovich

Version 0.7  
03/4/2013

^_^ Fin. ^_^
