import random as rnd 
 
def generar2(n): 
     arr = [0]*n 
     for i in range(n): 
         arr[i] = (rnd.randint(1,100)) 
     return arr 
 
print(generar2(10))