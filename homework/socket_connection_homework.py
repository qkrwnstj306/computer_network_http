import socket 

def socket_connect():
    HOST = ""
    PORT = ""
    
    encoded_credentials = ""
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        
        request_message = f"GET ...\r\n" + \
                      f"Host: ...\r\n" + \
                      f"Authorization: ...\r\n" + \
                      "\r\n"
        
        s.sendall(request_message.encode())
        
        response = b'' # don't change
        
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data
    
    print("RESPONSE:\n") 
    print(response.decode())
    
    if b"200 OK" in response:
        print("Attacker 로그인 성공!")
    else:
        print("Attacker 로그인 실패...")
