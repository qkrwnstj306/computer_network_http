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
        self.packet_captured = False
    
    def sniff_http_traffic(self):
        def packet_callback(packet):
            if not self.packet_captured and packet.haslayer(Raw):
                pass

        print("HTTP 요청 캡처를 시작합니다...")
        pass
        
    def attack(self):
        print("Attack Start...!")
        
        pass
           
        # 로그인 요청 보내기
        response = pass

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
    