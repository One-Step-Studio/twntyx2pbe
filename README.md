# twntyx2pbe
The backend


This server will manage api requests from client devices running unity and spread relevant api requests to flask servers on the same vpc.
it will wait for all async responses and finally resturn the user results for each request.

most resquests will be light api requests that will return quickly, yet still proccess some information after the user got its reply.
Django will just continue an asyncfunction after return- to manage database and process extra info from the flask infrastructure.
