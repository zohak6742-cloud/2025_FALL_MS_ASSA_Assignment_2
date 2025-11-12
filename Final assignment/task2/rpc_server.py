from xmlrpc.server import SimpleXMLRPCServer


def greet(name):
    return f"Hello {name}, this is the server!"


server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")
server.register_function(greet, "greet")
server.serve_forever()
