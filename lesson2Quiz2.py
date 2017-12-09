x = 3.14159      

#ENTER CODE BELOW HERE

y = str(x)

decimal_pos = y.find(".")


z = y[decimal_pos+1]

 


print (z);
if (z>=str(5)):

   
  a=y[:decimal_pos]
  print (int(a)+1);
else:

    
  b=y[:decimal_pos]
  print(int(b));
  
    