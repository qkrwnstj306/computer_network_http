from socket import *

def socket_connect():
    HOST = ""
    PORT = ""
    
    encoded_credentials = ""
    
    
    
    clientSocket = ""
    
    
    
    modifiedSentence = clientSocket.recv(1024)
    print("RESPONSE:\n\n", modifiedSentence.decode())
    clientSocket.close()
    
    if "200 OK" in modifiedSentence.decode():
        print("Attacker 로그인 성공!")
    else:
        print("Attacker 로그인 실패...")