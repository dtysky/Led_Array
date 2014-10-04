import string

import struct

out=open('Led.scr','w');

w_s=88.95
h_s=53.47

for k in range(2):
	w=w_s
	h=h_s
	
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'270'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+9.0000
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'90'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+16.07
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'270'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+9.0000
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'90'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+17
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'270'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+9.0000
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'90'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
    
	w=w+16
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'270'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+9.0000
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'90'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)

	w=w+17.05
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'270'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+9.0000
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'90'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)  

	w=w+16.43
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'270'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+9.0000
	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'90'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf) 	
	
	h_s=h_s-7.3


