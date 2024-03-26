from socket import *

def socket_connect():
    HOST = "gaia.cs.umass.edu"
    PORT = 80
    
    encoded_credentials = 'd2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms='
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    sentence = f"GET /wireshark-labs/protected_pages/HTTP-wireshark-file5.html HTTP/1.1\r\n" + \
                      f"Host: {HOST}\r\n" + \
                      f"Authorization: Basic {encoded_credentials}\r\n" + \
                      "\r\n"
    
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("RESPONSE:\n\n", modifiedSentence.decode())
    clientSocket.close()
    
    if "200 OK" in modifiedSentence.decode():
        print("Attacker 로그인 성공!")
    else:
        print("Attacker 로그인 실패...")