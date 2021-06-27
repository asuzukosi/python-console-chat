## Python cosole chat application

This is a console chat application built with just python.

It uses the socket library and the threading library to achieve this


The server.py is the the server application, there is a single server and you can spin up multiple client

The clients send chats to the application either as a broadcast to everyone or to a particular user. 

Clients register with a username they would like to be associated with while they use the application, and this information is persisted as long as the server is active
