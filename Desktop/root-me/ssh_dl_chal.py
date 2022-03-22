#!/usr/bin/env python3

from pwn import * 
import sys
import os
import argparse

def dl(user, password, port, server_name, files):
    #print("SSH to chal"+chal+" ...\n")
    
    host = ssh(user=user,
               host=server_name,
               port=port,
               password=password)
    
    for file in files:
        host.download_file(file)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("user")
    argparser.add_argument("file")
    argparser.add_argument("-s", "--server", required = False, default="root-me.org", help="the server")
    argparser.add_argument("-c", "--chalServ", type=int, required=False, help = "the challenge server on root-me")
    argparser.add_argument("-p", "--port", required = False, default = 2222, help="the port for the ssh")
    argparser.add_argument("-pass", "--password", required = False, help="password if needed")
    args = vars(argparser.parse_args())

    user = args['user']
    file = args['file']
    server = args['server']
    port = args['port']
    chall_serv = args['chalServ']
    password = args['password']
    
    try:
        assert(chall_serv or server)
    except:
        print("[-] Please enter a server with -s or --server, or at least a challenge-server number on root-me with -c")
        exit(1)

    if server == "root-me.org":
        server = "challenge0" + str(chall_serv) + "." + server
        password = user
    elif not password:
        password=""

    files = [file]
    dl(user,password,port,server,files)

    exit()


if __name__ == '__main__':
    main()
