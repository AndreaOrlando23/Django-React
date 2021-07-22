Stateless protocol = it means that every cycle (HTTP Request >> << Retrieve Data) it’s completely independent from the previous requests and dosen’t store previous information. So every time the client send a Request, it has to authenticate with tokens.
Every time we send a request, the server create a session == state
