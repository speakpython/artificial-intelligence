#http://127.0.0.1:4000/artificial-intelligence/2023/03/06/water-jug-problem.html#required-libraries

from math import gcd
from collections import defaultdict

#https://speakpython.codes/artificial-intelligence/2023/03/06/water-jug-problem.html#problem-defination

jug1 = int(input("Capacity of Jug1: "))
jug2 = int(input("Capacity of Jug2: "))
aim = int(input("Your Goal: "))


#https://speakpython.codes/artificial-intelligence/2023/03/06/water-jug-problem.html#water-jug-solver---driver-code

visited = defaultdict(lambda: False)
print("Jug1 \t Jug2")
def waterJugSolver(amt1, amt2): 
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0): #No. 1.
        print("-"*25)
        print(amt1,'\t',amt2,' -> Goal State')
        print("-"*25)
        return True
    if visited[(amt1,amt2)] == False: # No. 2.
        print(amt1,'\t',amt2)
        visited[(amt1, amt2)] = True

        return (waterJugSolver(0, amt2) or # No. 3
                waterJugSolver(amt1, 0) or
                waterJugSolver(jug1, amt2) or
                waterJugSolver(amt1, jug2) or
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
                amt2 - min(amt2, (jug1-amt1))) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
                amt2 + min(amt1, (jug2-amt2))))    
    else:
        return False

#https://speakpython.codes/artificial-intelligence/2023/03/06/water-jug-problem.html#possibility-check

if (aim == 0 or jug1 + jug2 > aim) and aim % gcd(jug1, jug2) == 0:
    waterJugSolver(0, 0) #defined in the next module
else:
    print("Not possible!")

