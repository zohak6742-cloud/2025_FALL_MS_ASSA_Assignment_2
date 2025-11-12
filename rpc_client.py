import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Requesting remote method...")
name = input("Enter your name: ")
response = proxy.greet(name)
print("Response from Server:", response)
