from urllib import request, parse

ENDPOINT = 'https://harshasrikara.api.stdlib.com/acm-dev@dev/challenge'

def send_response():
    params = parse.urlencode({
        'value': 'Willie Chalmers III',
    })
    response = request.urlopen(f'{ENDPOINT}?{params}')
    return response.read().decode('utf-8')

if __name__ == '__main__':
    print(send_response())

