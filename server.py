import socket
import pickle
from _thread import *

# Define the host and port for your server
HOST = '193.168.2.6'  # Listen on all available network interfaces
PORT = 49152

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

# A dictionary to hold player data
player_data = {}
first_player_data = {
    "player_id": 'id',
    "current_sprite": 'objects/animations/playerIdleSprites/3/playerIdle (1).png',
    "x" : 300,
    "y" : 300,
    "loc" : 'Aroyo_online'
}
player_data2 = {}
# Function to handle client connections
def handle_client(client_socket):
    try:
        player_data2[first_player_data["player_id"]] = first_player_data  # Store player data on the server

        players_and_client_data = {"player_data" : player_data2, "player_data_rec" : player_data2}
        pickle_data = pickle.dumps(players_and_client_data)

        print(pickle_data)
        
        client_socket.send(pickle_data)
        print('sended')
        print(f"client: {client_socket}")
        # Receive the JSON data from the client
        data = client_socket.recv(1024)
    
        # Deserialize the JSON data into a Python dictionary
        #messages = data.split("\n")
        #for message in messages:
            #try:
        player_data_received = pickle.loads(data)
        print(player_data_received)
                # Handle player_data_received
            #except json.decoder.JSONDecodeError:
        # Handle JSON decoding errors
                #print('json decoder error',str(messages))
        # Process the player's data
        player_id = player_data_received["player_id"]
        player_data[player_id] = player_data_received  # Store player data on the server
        print('player_data: ',str(player_data))
        players_and_client_data = {"player_data" : player_data, "player_data_rec" : player_data_received}
        pickle_data = pickle.dumps(players_and_client_data)

        # Broadcast the player's data to other connected clients
        #for client in client_sockets:
         #   if client != client_socket:
        print('sending')
                #client.send(data.encode())  # Send the player's data to other clients
        client_socket.send(pickle_data)
    except ConnectionResetError:
        print("connection reset error")
        client_socket.close()
        client_sockets.remove(client_socket)
def run():
    client, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    client_sockets.append(client)  # Add the new client socket to the list
    for socket in client_sockets:
        
        #handle_client(socket)
        handle_client(socket)
        #start_new_thread(handle_client(socket), (client,))
    

    start_new_thread(handle_client, (client,))
# List to store client sockets
client_sockets = []

# Accept client connections and handle them
while True:
    run()
    
    #client_handler = threading.Thread(target=handle_client, args=(client,))
    #client_handler.start()
