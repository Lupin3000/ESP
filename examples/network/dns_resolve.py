from usocket import getaddrinfo


DNS_TARGET = 'root-me.org'


if __name__ == '__main__':
    info = getaddrinfo(DNS_TARGET, 23)
    print(f'[INFO] The IP of {DNS_TARGET} is {info[0][-1][0]}')
