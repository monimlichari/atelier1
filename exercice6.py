n = int(input("Entrez le nomre choisi: "))

def compter(n):
    sum = 0
    while n!=0:
        n = n//10 # on va diviser le nombre choisi sur 10 jusqu'à le quotient devient 0
        sum += 1
    return sum

print("Le nombre des chiffres du nombre choisi est: %d"%compter(n))