# TCPserver_client_distance
This is a Git repository that contains the Python script for Assignment 4 - Part 2 of the _Advanced Python Programming Part-Time Course_ of Cardiff University.

This python TCP client/server applicationproduce a table of stopping distances for a range of speeds. Python socket programming and GUI were used.

The client application, distanceClient.py, connects to the server, distanceServer.py, using the TCP protocol and sends the values for the initial speed, final 
speed and increment in speed to the server.  The server application calculates the required stopping distances and sends back a table to the client 
as shown below.   

![image](https://user-images.githubusercontent.com/40058400/165054911-de815be3-5ba6-4f2d-88b2-e1ccd5ecb755.png)

The client application presents the user with a graphical interface as shown below and the above table is displayed in the blank scrollable 
Text widget.

![image](https://user-images.githubusercontent.com/40058400/165055072-41b75f38-f93b-49ae-bfd9-7e955272d869.png)
