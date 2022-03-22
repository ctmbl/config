#!/usr/bin/env python3

from pwn import * 

argv = ["pwntools.py","xx"]
print("SSH on challenge: "+argv[1])

host = ssh(user="app-systeme-ch"+argv[1],
           host="challenge02.root-me.org",
           port=2222,
           password="app-systeme-ch"+argv[1])
target = host.process(b"./ch"+bytes(argv[1],'utf-8'))

target.interactive()

buffer = b""
payload = p32(0xdeadbeef)
target.sendline(buffer + payload)

target.interactive()

close = False
while(not close):
    msg = input()
    if msg == 'exit\n' or msg == 'e\n':
        print("--> Order to exit challenge...")
        close = True
        host.close()
        break
    elif msg != "\n":
        print("--> Sending: "+msg)
        target.sendline(bytes(msg,'ascii'))
        print(target.recvline())
    else:
        print(target.recvline())

