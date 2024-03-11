import math

def outliers(num):
    mitjana = sum(num) / len(num)
    desviacio = math.sqrt(sum((x - mitjana) ** 2 for x in num) / len(num))
    z_scores = [(x - mitjana) / desviacio for x in num]
    return [num[i] for i, z in enumerate(z_scores) if z >= 1.5 or z <= -1.5]


numbers = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 100, 105, 110]
print(outliers(numbers))
