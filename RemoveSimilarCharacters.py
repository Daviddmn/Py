def duplicate_count(text):
    b=''

    for z in text:
    	if z not in b:
    		b+=z
    	else:
    	    continue
    return b	
    	
	
       
            
    


print(duplicate_count("abcabcaaaaaabcbcccaaaaattttp"))

