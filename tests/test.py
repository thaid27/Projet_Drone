import threading 
import socket
import sys
import time

TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889
LOCAL_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", LOCAL_PORT))

# ------------------------------------------------------------------------ Load faces and detector/predictor ------------------------ #

# known_faces = load_known_faces(directory="Camera")
authorized_user = "Alexandre"  # Simulating an authorized user for testing

# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks(1).dat")
# detector = dlib.get_frontal_face_detector()

# ------------------------------------------------------------------------ Definition send and receive ------------------------ #

def send(cmd):
    print(f"Sending: {cmd}")
    sock.sendto(cmd.encode(), (TELLO_IP, TELLO_PORT))


def receive():
    try:
        response, _ = sock.recvfrom(1024)
        print(f"Response: {response.decode()}")
    except Exception as e:
        print(f"Error: {e}")


send("command")
receive()