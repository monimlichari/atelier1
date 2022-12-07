
X = int(input("Entrez le numéro X"))
n = int(input("Entrez la puissance n"))

def puissance(X,n):
    puissance = 1
    for i in range(1,X+1):
            puissance = puissance * X
    return puissance
            
print("X^n est égale à: %d"%puissance(X,n))         

    
    


    

