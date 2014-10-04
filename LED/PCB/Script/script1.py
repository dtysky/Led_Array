import string

import struct

out=open('Led.scr','w');

w=204.5000
h=500.1500

for j in range(51):
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    w=w+2.0000
