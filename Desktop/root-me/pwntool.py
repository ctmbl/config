#!/usr/bin/env python3

from pwn import * 
import sys

def pwn_it(guessed_address = 0x0):
    pass

if len(sys.argv) != 2:
    print("remote, local or plz_pwn ?")
    exit(1)

target = None
if sys.argv[1] == "remote":
    target = ???? 

    pwn_it()
    target.interactive()
elif sys.argv[1] == "local":
    target = process( ???? )
    gdb.attach(target, gdbscript='')
    pwn_it()
    target.interactive()
elif sys.argv[1] == "plz_pwn":
    print("Doesn't defined")
    for i in range( ???? , ???? , ??? ): 
        target = ????
        pwn_it(i)
        try: 
            target.recvline()
        except EOFError:
            pass
        except:
            target.interactive()
        else:
            target.interactive()
        target.kill()
else:
    print("remote, local or plz_pwn ?")
    exit(1)


