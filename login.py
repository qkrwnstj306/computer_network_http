import requests
import base64

login_url = 'http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html'

def user_login():

    # Base64로 인코딩된 사용자 인증 정보
    encoded_credentials = 'd2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms='  # wireshark-students:network 의 Base64 인코딩 결과

    # Base64 디코딩하여 사용자 인증 정보 추출
    decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
    username, password = decoded_credentials.split(':')

    # HTTP 요청 헤더 설정
    headers = {'Authorization': f'Basic {encoded_credentials}'}

    # 로그인 요청 보내기
    response = requests.get(login_url, headers=headers)

    # 응답 확인
    if response.status_code == 200:
        print('User 로그인 성공!')
    else:
        print('User 로그인 실패...')