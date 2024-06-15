print('This program illustrates the number of years taken to reach the final population.')
initPop = int(input("Enter the initial population: "))
finPop = int(input("Enter the final population: "))

if initPop < finPop:
    c = 0
    currentpop = initPop
    while currentpop < finPop:
        newBorn = int(currentpop / 3)
        Dead = int(currentpop / 4)
        total = currentpop + newBorn - Dead
        c += 1
        currentpop = total 
        if currentpop >= finPop: 
            break

    print(f"It took {c} years to reach or exceed the final population.")

elif initPop < 9:
    print("Enter an initial population greater than 9.")
else:
    print("Enter a final population greater than the initial population.")
