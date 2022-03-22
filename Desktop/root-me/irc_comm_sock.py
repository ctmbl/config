#!/usr/bin/env python3

import sys
import socket
import time
from math import sqrt 


def loop(sock, channel, bot, nickname):

    def pwn_it():
        sock.send(bytes("PRIVMSG " + bot + " :!ep1\n","UTF-8"))
        printer(bot + " called")
        ans = sock.recv(70).decode("UTF-8")
        n1 = int( ans[ans[1:].find(":")+2 : ans.find(" / ")] )
        print(n1)
        n2 = int( ans[ans.find(" / ") + 3:])
        print(n2)
        res = round(sqrt(n1)*n2,2)
        sock.send(bytes("PRIVMSG " + bot + " :!ep1 -rep " + str(res) + "\n", "UTF-8"))
        ans = sock.recv(100).decode("UTF-8")
        print(ans)

    def cmd():
        cmd = str(input())
        if cmd == 'q' or cmd == 'e':
            sock.send(bytes("QUIT :None\n", "UTF-8"))
            printer("QUIT msg sent")
            printer("EXIT now")
            exit(1)
        elif cmd == 'j':
            sock.send(bytes("JOIN " + channel + "\n", "UTF-8"))
            printer("has joined " + channel)
        elif cmd == 'pm':
            sock.send(bytes("PRIVMSG " + bot + " :!ep1\n","UTF-8"))
            printer("candy PMed")
        elif cmd == 'pwn':
            pwn_it()
        elif cmd == 'i':
            cmd = str(input())
            sock.send(bytes(cmd + "\n","UTF-8"))
        else:
            printer("Unknown cmd: " + cmd)

    text = "" 
    while True:
        try:
            text = sock.recv(2040).decode("UTF-8")
        except UnicodeDecodeError:
            pass
        except KeyboardInterrupt:
            printer("Interrupt")
            print("List of cmds: 'e', 'q' - exit ; 'j' - join channel ; 'pm' - PM the bot ; 'i' - interactive ; 'pwn' - u know")
            cmd()

        sys.stdout.write(text)
    
        if "PING" in text:
            printer("PONG sent")
            sock.send(bytes("PONG " + nickname + "\n","UTF-8"))
        text = ""

def main():
    HOST = "irc.root-me.org"
    PORT = 6667
    CHANNEL = "#root-me_challenge"
    BOT = "candy"
    
    if len(sys.argv) < 2:
        printer("Missing arguments")
        print("use: " + sys.argv[0] + " <nickname>")
        printer("EXIT")
        exit(1) 
    NICK = sys.argv[1]
    sock = connect(HOST, PORT, NICK)
    loop(sock, CHANNEL, BOT, NICK)
    exit(0)    

def connect(host, port, nickname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    printer("socket created")
    
    try:
        conn = sock.connect((host, port))
    except:
        raise SystemExit(1)
        printer("EXIT")
        exit(1)
    printer("socket connected")
    sock.send(bytes("NICK " + nickname + "\n","UTF-8"))
    sock.send(bytes("USER " + nickname + " foo junk" + " :" + nickname + "\n", "UTF-8")) 
    printer(nickname + " registerd")
    return sock


def printer(text):
    print("[+] " + text)


if __name__ == "__main__":
    main()
