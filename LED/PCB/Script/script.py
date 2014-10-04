import string

import struct

out=open('Led.scr','w');

w_s=200.0000
h_s=800.0000

for n in range(3):
    w_s=200.0000
    for k in range(4):
        w=w_s
        h=h_s
        for i in range(38):
            for j in range(30):
                wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
                out.write(wtf)
                w=w+2.0000
            w=w_s
            h=h-2.0000
        w_s=w_s+60
    h_s=h
        


