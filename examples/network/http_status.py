import urequests


TARGET_URL = 'https://pentest-tools.com'


if __name__ == '__main__':
    res = urequests.get(TARGET_URL)
    print(f'[INFO] HTTP Status Code for {TARGET_URL} is {res.status_code}')
