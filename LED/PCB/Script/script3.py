import string

import struct

out=open('Led.scr','w');

w_s=199.3
h=801.65

for i in range(114):
    
    w=w_s
    
    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    w=w+2
    h=h+0.2
    
    for j in range(120):

        wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)
        wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)

        w=w+2

    h=h-2.2



