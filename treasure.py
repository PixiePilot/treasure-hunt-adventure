import random
def treasurechest():
    coppercoins = random.randint(1,169420)
    silvercoins = random.randint(1,10000)
    silvercoins = silvercoins / 10
    platinumcoins = random.randint(1,1000)
    platinumcoins = platinumcoins * 24
    goldcoins = random.randint(1,1000)
    goldtotal = goldcoins + platinumcoins + silvercoins
    goldtotal = float(round(goldtotal, 3))
    return goldtotal

chest = treasurechest()
print(chest,"Gold coins is in the chest!!")