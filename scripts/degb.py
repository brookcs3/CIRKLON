#!/usr/bin/env python3
import mido, sys, pathlib

if len(sys.argv) != 2:
    sys.exit("usage: unpack_ck2os.py <CK2OS.SYX>")
    
syx_path = pathlib.Path(sys.argv[1])
out_path = syx_path.with_suffix('.bin')

data_out = bytearray()

for msg in mido.read_syx_file(syx_path):
    d = msg.data
    for i in range(0, len(d), 8):
        prefix = d[i]
        block  = d[i+1:i+8]
        for bit, b in enumerate(block):
            data_out.append(b | (((prefix >> bit) & 1) << 7))

out_path.write_bytes(data_out)
print(f"✓ Wrote {out_path}  ({len(data_out):,} bytes)")