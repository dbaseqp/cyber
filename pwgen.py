#!/bin/python3
import argparse
import random
import string
import socket

def id_generator(size, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
    parser = argparse.ArgumentParser(description='Generate random passwords in comma-separated format.')
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('-c', dest='count', type=int, default=1, help='Number of passwords to print')
    mode_group.add_argument('-u', dest='user_list', action='store', help='list of users to set passwords of', default='')
    parser.add_argument('-n', dest='number', type=int, action='store', default=3, help='number of password groups (default: 3)')
    parser.add_argument('-s', dest='service', action='store', default='', help='name of service for password')
    args = parser.parse_args()
    print(args)
    if not getattr(args, 'user_list') == '':
        with open( getattr(args, 'user_list'), 'r') as file:
            count = len(file.readlines())
    else:
        count = getattr(args,'count')
    length = getattr(args, 'number')
    for password in range(count):
        generated_password = ''
        for i in range(length):
            generated_password += id_generator(5)
            generated_password += '-'
        generated_password = generated_password.strip('-')
        if not getattr(args, 'user_list') == '':
            with open(getattr(args, 'user_list'), 'r') as file:
                print(get_ip() + ','+ file.readlines()[password].rstrip() + ',' + generated_password + ',' + getattr(args, 'service'))
        else:
            if  getattr(args, 'service') == '':
                print(generated_password)
            else:
                print(generated_password + ',' + getattr(args,'service'))


if __name__=='__main__':
    main()

