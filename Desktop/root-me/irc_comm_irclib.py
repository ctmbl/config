#! /usr/bin/env python
#
# Example program using irc.client.
#
# This program is free without restrictions; do anything you like with
# it.
#
# Joel Rosdahl <joel@rosdahl.net>

import sys
import argparse
import itertools
import subprocess

import time

import irc.client
import jaraco.logging


class RootMeIRC2(irc.client.SimpleIRCClient):
    
    def __init__(self, host, port, nick, channel, target, pwn):
        irc.client.SimpleIRCClient.__init__(self)
        try:
            self.conn = self.connection.connect(host, port, nick)
            print("[+] client created")
        except irc.client.ServerConnectionError:
            print(sys.exc_info()[1])
            raise SystemExit(1)

        self.host = host
        self.port = port
        self.nick = nick
        self.channel = channel
        self.target = target
        self.pwn = self.pwn_it if pwn == None else pwn

    def on_welcome(self, conn, event):
        print("[+] on_welcome")
        print("[+] do you want to pwn_it ? : 'pwn' or 'p' - pwn_it")
        cmd = input()
        if cmd == 'pwn' or cmd == 'p':
            self.pwn()
    
    def on_privmsg(self, conn, event):
        print("[+] " + self.target + "responded")
        print(event.source + " said " + event.arguments[0] + " of type "  + str(type(event.arguments[0])))
        print(event.arguments)
        #print([type(event.arguments[i]) for i in range(len(event.arguments))])

        print("[+] CMD, what do you want to do : r - respond ; e - exit")
        cmd = input()
        if cmd == 'r':
            self.respond(conn,event)
        elif cmd == 'e' or cmd == 'q':
            conn.quit()
        else:
            print("[+] Unknown command, nothing to do")

    def on_join(self, conn, event):
        print("[+] on_join")
    
    def pwn_it(self):
        self.conn.join(self.channel)
        self.conn.privmsg(self.target, "!ep3")
    
    def respond(self, conn, event):
        ans = rot13(event.arguments[0])
        print("[+] trying to decode in rot13: " + ans)
        conn.privmsg(self.target,"!ep3 -rep " + ans)
    
    def on_disconnect(self, conn, event):
        print("[+] disconnected")
        raise SystemExit()

def rot13(msg):
    ans = ""
    for i in msg:
        if i < 'A':
            ans += i
            continue
        c = bytes(i,'utf-8')
        offset = 0x41 if i < 'a' else 0x61
        c13_int =  (int.from_bytes(c,'little') - offset + 13)%26 + offset
        ans += str(c13_int.to_bytes(1,"little"))[2:-1] 
    return ans

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('server')
    parser.add_argument('nickname')
    parser.add_argument('channel')
    parser.add_argument('target', help="the bot to communicate with")
    parser.add_argument('-p', '--port', default=6667, type=int)
    jaraco.logging.add_arguments(parser)
    print("[+] args parsed")
    return parser.parse_args()


def main():
    args = get_args()
    jaraco.logging.setup(args)
    print(args)
    exploit =  RootMeIRC2(args.server, args.port, args.nickname, args.channel, args.target, None)
    try:
        exploit.start()
    except KeyboardInterrupt:
        print("[+] what do you want to do ? : e or q - exit")
        cmd = input()
        if cmd =='e' or cmd == 'q':
            exploit.conn.quit("Force quit")
        else:
            print("[+] Unknown command")


if __name__ == '__main__':
    main()
