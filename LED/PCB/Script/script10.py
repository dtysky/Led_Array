import string

import struct

out=open('Led.scr','w');

w=202
h=540.8

for j in range(120):

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    
    h=h-4
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
        
    h=h+4
    wtf='done'+';'+'\n'
    out.write(wtf)


    w=w+2



