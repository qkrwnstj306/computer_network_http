import socket 

def socket_connect():
    HOST = "gaia.cs.umass.edu"
    PORT = 80
    
    encoded_credentials = 'd2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms='
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        
        request_message = f"GET /wireshark-labs/protected_pages/HTTP-wireshark-file5.html HTTP/1.1\r\n" + \
                      f"Host: {HOST}\r\n" + \
                      f"Authorization: Basic {encoded_credentials}\r\n" + \
                      "\r\n"
        
        s.sendall(request_message.encode())
        
        response = b''
        
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data
    
    print("RESPONSE:\n") 
    print(response.decode())
    
    # 응답 출력
    if b"200 OK" in response:
        print("Attacker 로그인 성공!")
    else:
        print("Attacker 로그인 실패...")
