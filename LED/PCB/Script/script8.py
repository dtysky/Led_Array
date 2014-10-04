import string

import struct

out=open('Led.scr','w');

w=201.3
h=573.8

for j in range(120):

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    
    h=h-33
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
        
    h=h+33
    wtf='done'+';'+'\n'
    out.write(wtf)


    w=w+2



