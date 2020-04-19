#!/usr/bin/env sh
from urllib import request, parse


ENDPOINT = 'https://harshasrikara.api.stdlib.com/acm-dev@dev/challenge'


def send_response(value: str):
    """Return a response to the challenge server.""" 
    params = parse.urlencode({
        'value': value,
    })
    response = request.urlopen(f'{ENDPOINT}?{params}')
    return response.read().decode('utf-8')


if __name__ == '__main__':
    print(send_response('Willie Chalmers III'))

