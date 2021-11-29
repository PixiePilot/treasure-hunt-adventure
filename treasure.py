import random
def treasurechest():
    platinumcoins = 27
    platinumcoins = platinumcoins *24
    kroon = 93
    robijn = 8.1
    ring = 46.5
    armband = 2426.4
    question1 = 63.3
    question2 = 17.6
    question3 = 1.5

    total = kroon + platinumcoins + robijn + ring + armband + question1 + question2 + question3
    return total

chest = treasurechest()
print(chest,"Gold coins is in the chest!!")

chest = chest / 5

