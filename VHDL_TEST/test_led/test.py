import binascii
from PIL import Image

im=Image.open('test.bmp').tobytes()
fout1=open('test1.txt','w')
fout2=open('test2.txt','w')
fout3=open('test3.txt','w')

bs=''


for i in range(len(im)):
    b=binascii.b2a_hex(im[i])
    bs+=bin(int(b,16))[2:];
##    if len(b)==7:
##        bs+='0'+bin(int(b,16))[2:]
##    elif len(b)==6:
##        bs+='00'+bin(int(b,16))[2:]
##    elif len(b)==5:
##        bs+='000'+bin(int(b,16))[2:]
##    elif len(b)==4:
##        bs+='0000'+bin(int(b,16))[2:]
##    elif len(b)==3:
##        bs+='00000'+bin(int(b,16))[2:]
##    elif len(b)==2:
##        bs+='000000'+bin(int(b,16))[2:]
##    elif len(b)==1:
##        bs+='0000000'+bin(int(b,16))[2:]
##    elif len(b)==0:
##        bs+='00000000'+bin(int(b,16))[2:]
##    else:
##        bs+=bin(int(b,16))[2:]

##for i in range(len(bs)/120):
##    print bs[(i*120):((i+1)*120-1)]+'\n'

s1=bs[0:4560]
s2=bs[4560:9120]
s3=bs[9120:13680]

for i in range(len(s1)/40):
    fout1.write(str(i)+' '+':'+' '+s1[(i*40):((i+1)*40-1)]+';'+'\n')
    fout2.write(str(i)+' '+':'+' '+s2[(i*40):((i+1)*40-1)]+';'+'\n')
    fout3.write(str(i)+' '+':'+' '+s3[(i*40):((i+1)*40-1)]+';'+'\n')

fout1.close()
fout2.close()
fout3.close()
