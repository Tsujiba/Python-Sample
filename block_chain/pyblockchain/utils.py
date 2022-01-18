from audioop import add
import collections
import re
import socket
import logging
from sys import prefix
from traceback import print_tb

RE_IP = re.compile('(?P<prefix_host>^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.)(?P<last_ip>\\d{1,3}$)')

logger = logging.getLogger(__name__)

def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(sorted(unsorted_dict.items(), key=lambda d:d[0]))

def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25}Chain{i}{"="*25}')
        for k, v in chain.items():
            if k == 'transaction':
                print(k)
                for d in v:
                    print(f'{"-"*40}')
                    for kk, vv in d.items():
                        print(f'{kk:30}{vv}')
            else:
                print(f'{k:15}{v}')
    print(f'{"*"*25}')
    
def is_found_host(targer_ip, targer_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        try:
            sock.connect((targer_ip, targer_port))
            return True
        except Exception as ex:
            logger.error({
                'action': 'is_found_host',
                'target_ip': targer_ip,
                'target_port': targer_port,
                'ex': ex
            })
            return False

def find_neighbours(my_host, my_port, start_ip_range, end_ip_range, start_port, end_port):
    address = f'{my_host}:{my_port}'
    m = RE_IP.search(my_host)
    if not m:
        return None
    
    prefix_host = m.group('prefix_host')
    last_ip = m.group('last_ip')
    
    neighbours = []
    for guess_port in range(start_port, end_port):
        for ip_range in range(start_ip_range, end_ip_range):
            guess_host = f'{prefix_host}{int(last_ip)+int(ip_range)}'
            guess_address = f'{guess_host}:{guess_port}'
            if is_found_host(guess_host, guess_port) and not guess_address == address:
                neighbours.append(guess_address)
    return neighbours

def get_host():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as ex:
        logger.error({
            'action': 'get_host',
            'ex': ex
        })

if __name__ == '__main__':
    
    # print(is_found_host('127.0.0.1', 5000))
    # print(find_neighbours('127.0.0.1', 5000, 0, 3, 5000, 5002))
    # print(get_host())
    print(find_neighbours(get_host(), 5000, 0, 3, 5000, 5002))

    
    
    # dict1 = {'a': 1, 'b': 2}
    # dict2 = {'b': 2, 'a': 1}
    
    # print(sorted_dict_by_key(dict1))
    # print(sorted_dict_by_key(dict2))
    
    # if dict1 == dict2:
    #     print('true')
    # else:
    #     print('False')
    
    # print(collections.OrderedDict(dict1))
    # print(collections.OrderedDict(dict2))
    
    # if collections.OrderedDict(dict1) == collections.OrderedDict(dict2):
    #     print('true')
    # else:
    #     print('False')
        
    # print(dict2)
    # print(dict2.items())
    # print(sorted(dict2.items()))



