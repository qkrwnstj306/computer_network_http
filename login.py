import requests
import base64

login_url = 'http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html'

def user_login():
    encoded_credentials = 'd2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms='  # wireshark-students:network 의 Base64 인코딩 결과

    headers = {'Authorization': f'Basic {encoded_credentials}'}

    response = requests.get(login_url, headers=headers)

    if response.status_code == 200:
        print('User 로그인 성공!')
    else:
        print('User 로그인 실패...')

if __name__=="__main__":
    user_login()

