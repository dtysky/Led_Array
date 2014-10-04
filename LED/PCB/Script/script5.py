import string

import struct

out=open('Led.scr','w');

w=202
h_s=648.8
for i in range(120):
    
    h=h_s
    
    
    for j in range(37):

        wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)

        h=h-2
        wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)

        wtf='done'+';'+'\n'
        out.write(wtf)


    w=w+2



