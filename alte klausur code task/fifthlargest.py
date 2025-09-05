
# task a, 4 points
# Es sei eine Liste L von 5 oder mehr paarweise verschiedenen ganzen Zahlen gegeben.
# Schreiben Sie eine Python-Funktion fifthlargest(L), die das fünftgrößte Element
# von L zurückgibt. Es darf dabei L nur einmal durchlaufen werden.

def fifthlargest(L):
    if len(L) < 5:
        raise ValueError("List must have at least 5 elements")
    
    top5 = []
    for x in L:
        # find insertion position
        pos = 0
        while pos < len(top5) and top5[pos] > x:
            pos += 1
        top5.insert(pos, x)   # insert keeps descending order
        if len(top5) > 5:
            top5.pop()        # remove smallest if > 5 elements
    
    return top5[-1]           # 5th largest is now at the end

print(fifthlargest([20, 15, 10, 8, 5, 3, 2]))
print(fifthlargest([1,2,3,4,5]))
print(fifthlargest([1,10,2,3,4,5]))