init = float(input("Initial Amount: "))
halflife = float(input("Half-life: "))
time = float(input("Elapsed-time: "))
residual = init*0.5**(time/halflife)
print("Residual amount remaining = ",residual)
