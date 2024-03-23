import socket
import base64

def user_login():
    # 서버 주소와 포트 설정
    HOST = 'gaia.cs.umass.edu'
    PORT = 80
    
    # 인증 정보 인코딩
    encoded_credentials = 'd2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms='  # wireshark-students:network 의 Base64 인코딩 결과
    
    # HTTP 요청 메시지 생성
    request_message = f"GET /wireshark-labs/protected_pages/HTTP-wireshark-file5.html HTTP/1.1\r\n" + \
                      f"Host: {HOST}\r\n" + \
                      f"Authorization: Basic {encoded_credentials}\r\n" + \
                      "\r\n"
    
    # 소켓 생성 및 서버에 연결
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # 요청 메시지 전송
        s.sendall(request_message.encode())
        
        # 서버로부터 응답 받기
        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data
    
    # 응답 출력
    if b"200 OK" in response:
        print("User 로그인 성공!")
    else:
        print("User 로그인 실패...")

if __name__ == "__main__":
    user_login()