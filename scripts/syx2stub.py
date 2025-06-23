#!/usr/bin/env python3
import mido, sys, pathlib

if len(sys.argv) != 3:
    sys.exit("usage: syx2stub.py <infile.syx> <out.bin>")

src, dst = map(pathlib.Path, sys.argv[1:])
out = bytearray()

for msg in mido.read_syx_file(src):
    d = msg.data
    for i in range(0, len(d), 8):
        prefix = d[i]
        block  = d[i+1:i+8]
        for bit, b in enumerate(block):
            out.append(b | (((prefix >> bit) & 1) << 7))

dst.write_bytes(out)
print(f"✓ wrote {dst}  ({len(out):,} bytes)")