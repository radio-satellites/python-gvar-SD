import os
from PIL import Image
from bitstring import BitArray
f = open("goesn_sd.frm",'rb')
f_out = open("goesn_output.bin",'wb')

bytes_in_file = os.path.getsize('goesn_sd.frm')
ints_in_file = []
bits_list = []
#print(ints_in_file)

ch1 = Image.new('RGB',(20000,2000))

counter = 0

def read_bits():
    global bits_list #Allows for modification inside function
    #attempt to read 80 bits/10bytes because it is convinient
    bytes10 = f.read(10).hex() #10 bytes = 80 bits
    #print(bytes10)
    c = BitArray(hex=bytes10)
    bits_string80 = c.bin[2:] #I'm not sorry about the variable names. Sorry!
    for i in range(8): #8 because we are repacking into 10 bit frames
        #bits_list.append(bits_string80[i*10:(i+1)*10])
        ints_in_file.append(int(bits_string80[i*10:(i+1)*10],2))

    return 0
        
    
    
    

for i in range(2000000):
    #ints_in_file.append(int.from_bytes(current_byte, "big"))
    #f_out.write(int.from_bytes(current_byte, "big"))
    read_bits()
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


