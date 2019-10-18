f = open("data.bin","wb")
byte_arr = bytes([255,0,17]) #3
f.wrtite(byte_arr)
f.close()