import sys
from pathlib import Path

try:
    input_file = Path(sys.argv[1])
    if not input_file.exists():
        raise FileNotFoundError
except Exception as e:
    print(f"Error: {e}")
    exit()
    
def RunlengthEncode(bytesin:bytes) -> bytes:
    lastbyte = None
    current_stack = 0 # Like minecraft..???
    out = []
    nullchar = u"\u0000"
    
    for byte in bytesin:
    
        if byte == lastbyte:
            current_stack += 1
            continue
        else:
            out.append(f"{byte}{nullchar}{current_stack}{nullchar}".encode("utf-8"))


            current_stack = 0
        
        
        lastbyte = byte
    
    b = b"".join(out)
    return b

print("Loading file into memory.")

data = input_file.read_bytes()

print(f"Before Size: {data.__sizeof__() /1024} KiB")

out = RunlengthEncode(data)

print("Done!")
print(f"Size afterwards: {out.__sizeof__() /1024} KiB")

c = input("Write to file? (Y/N)")

if c.lower() != "y":
    exit()
    
outfile = Path(input_file.name + ".runlength.bin")
outfile.write_bytes(out)

print(f"Wrote file to {outfile.absolute()}.")