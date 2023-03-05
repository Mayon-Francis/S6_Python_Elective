x = 0xA0

for n in range(1,16):
    x>>1
    if(x & 0x01 == 1):
        print("1", end="")
    else:
        print("0", end="")
