from PIL import Image

im=Image.open('test.bmp').getdata()
fout1=open('../ROM/IMG1.mif','w')
fout2=open('../ROM/IMG2.mif','w')
fout3=open('../ROM/IMG3.mif','w')

bs=''

for ip in im:
    bs+=str(ip)

fout1.write('WIDTH=40;\nDEPTH=128;\nADDRESS_RADIX=UNS;\nDATA_RADIX=BIN;\nCONTENT BEGIN\n')
fout2.write('WIDTH=40;\nDEPTH=128;\nADDRESS_RADIX=UNS;\nDATA_RADIX=BIN;\nCONTENT BEGIN\n')
fout3.write('WIDTH=40;\nDEPTH=128;\nADDRESS_RADIX=UNS;\nDATA_RADIX=BIN;\nCONTENT BEGIN\n')

s1=bs[0:4560]
s2=bs[4560:9120]
s3=bs[9120:13680]

for i in range(len(s1)/40):
    fout1.write('\t'+str(i)+' '+':'+' '+s1[(i*40):((i+1)*40-1)]+';'+'\n')
    fout2.write('\t'+str(i)+' '+':'+' '+s2[(i*40):((i+1)*40-1)]+';'+'\n')
    fout3.write('\t'+str(i)+' '+':'+' '+s3[(i*40):((i+1)*40-1)]+';'+'\n')

fout1.write('\t[114..127]  :   0;\nEND;')
fout2.write('\t[114..127]  :   0;\nEND;')
fout3.write('\t[114..127]  :   0;\nEND;')

fout1.close()
fout2.close()
fout3.close()
