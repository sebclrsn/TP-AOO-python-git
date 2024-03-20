def calculate_moving_average(data: list[float], interval: int):
    resultat = []
    longueur_liste = len(data)
    for i in range(longueur_liste-n):
        x = 0
        for j in range(n):
            x = x + (1/n)*data[n-j+i-1]
        resultat.append(x)
    print(resultat)

data = [0,1,2,3,4,5,6,7,8,9]
n=4

calculate_moving_average(data,n)
