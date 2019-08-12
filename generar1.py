import random as rnd 
 
def generar(n): 
     arr = [] 
     for i in range(n): 
         arr.append(rnd.randint(1,100)) 
     return arr 
 
print(generar(10))