import string

import struct

out=open('Led.scr','w');

w=241.9
h=119

for j in range(40):

##    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
##    out.write(wtf)
##    
##    h=h-2
##    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
##    out.write(wtf)
##    wtf='pick'+'  '+'dbl'+'  '+str(w)+'  '+str(h)+';'+'\n'
##    out.write(wtf)
##
##    h=h+2
##    w=w+1.27
##    wtf='done'+';'+'\n'
##    out.write(wtf)

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    
    w=w+2
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='pick'+'  '+'dbl'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    w=w-2
    h=h-1.27
    wtf='done'+';'+'\n'
    out.write(wtf)
