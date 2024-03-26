import pyshark
import requests
import base64
from socket_connection import socket_connect

class Attacker():
    
    def __init__(self):
        
        self.encoded_info = 'd2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms='
        self.decoded_info = base64.b64decode(self.encoded_info).decode('utf-8')
        self.http_version = '1.1'
        self.login_url = 'http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html'
        self.host_name = 'gaia.cs.umass.edu'
        
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
        print("="*20)
        print(f"Decoded user info: {self.decoded_info}")
        print(f"HTTP version: {self.http_version}")
        print(f"Host name: {self.host_name}")
        print("="*20)

            
if __name__ == '__main__':       

    attacker = Attacker()
   
    attacker.setting()
 
