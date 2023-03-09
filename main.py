import os
from PIL import Image
f = open("goesn_sd.frm",'rb')
f_out = open("goesn_output.bin",'wb')

bytes_in_file = os.path.getsize('goesn_sd.frm')
ints_in_file = []
#print(ints_in_file)

ch1 = Image.new('RGB',(20000,2000))

counter = 0

for i in range(2000000):
    current_byte = f.read(1) #read exactly one byte
    ints_in_file.append(int.from_bytes(current_byte, "big"))
    #f_out.write(int.from_bytes(current_byte, "big"))
    if counter == 1000000:
        print("Done "+str(round((i/bytes_in_file)*100))+"%!")
        counter = 0
    counter = counter + 1

print("Write image!")
px, py = 0, 0
w = 20000
for p in range(100*w):
    if px == w:
        py = py+1
        #print(py)
        px = 0
    else:
        ch1.putpixel((px, py), (int(round(ints_in_file[py*w + px])),int(round(ints_in_file[py*w + px])),int(round(ints_in_file[py*w + px]))))
        px = px+1
ch1.save("ch1.png")


