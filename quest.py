import math
def theamount()-> float:
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print('Only numbers are allowed, Please try again.')
        theamount()
    return amount

def conversion():
    currency = input('Please enter your desired currency choose from : Copper, silver, gold or platinum : ')
    currency.lower
    amount = theamount()
    match currency:
        case "copper":
            print("Your currency is copper, but the total amount in the end will be shown in gold.")
            amount = amount / 50

        case "silver":
            print('Your currency is silver, but the total amount in the end will be shown in gold.')
            amount = amount / 10
        
        case "gold":
            print('Your currency is gold, but the total amount in the end will be shown in gold.')

        case "platinum":
            print('Your currency is platinum, but the total amount in the end will be shown in gold.')
            amount = amount * 24

    return amount
def costs():
    try:
        global people
        people = int(input('How many people are you with: '))
    except ValueError:
        print('Please enter a number.')
        costs()
    _ = people / 2
    horse = 0.8
    horse = _ * horse
    tent = 8
    inn = 0.4
    innhorse = 0.18
    price = float(tent + inn + innhorse)
    price = people * price + horse
    price = float(round(price, 2))
    return price
    
#costs : 8 gold per tent; 2 person horse 8 silver per day; inn visit 4 silver per person, 9 copper per horse 
amount = conversion()
print(amount)
price = costs()
print(price, " Is your total bill in gold.")
check = (amount - price)


if check < 0:
    check = float(round(check, 2))
    print('You don\'t hav enough gold, you\'re missing :',check)
else:
    check = float(round(check, 2))
    print('This is what you\'ll have left after the bills : ',check)

#sing up, Certain questions asked to not waste time.

def welcome():
    print('Welcome to the Team sing up program\nCertain questions will be asked to ensure that you\'re a good fit.\nGoodluck!')
    print('(one investor is required)')
def question1():
    try:
        quest1 = int(input('How old are you: '))
    except ValueError:
        print('please use a number')
        question1()
    return quest1

def question2():
    quest2 = str(input('Have you adventured before: '))
    quest2.lower
    if quest2 == "yes":
        return quest2
    elif quest2 == "no":
        return quest2
    else:
        print('Please type either Yes or No.')
        question2()

def question3():
    answer = input('Are you evil: ')
    answer.lower
    if answer == "yes":
        print('Go away, You evil bastard.')
        return False
    elif answer == "no":
        return True
    else:
        print('Please type either Yes or No.')
        question3()

def question4():
    answer = input('Are you trustworthy: ')
    answer.lower
    if answer == "yes":
        
        return True
    elif answer == "no":
        return False
    else:
        print('Please type either Yes or No.')
        question3()

def question5():
    a = input ('Which roll do you have in society.\nChoose between:\nInvestor\nThief\nRanger\nHealer\nNone above\nAnswer:')
    a.lower
    if a == "investor":
        global job
        job = "investor"
        return True

    if a == "thief":
        
        job = "thief"
        return True
    if a == "ranger":
        
        job = "ranger"
        return True
    if a == "healer":
        
        job = "healer"
        return True
    elif a == "none above":
        return False

    else:
        print('Please choose from one of the roles listed')
        question5()




def questionthief():
    questthief = int(input('How many things have you stolen before: '))
    if questthief > 2:
        return True
    else: 
        return False

def questionthief2():
    questthief2 = int(input('How many times have you been caught before: '))
    if questthief2 > 1:
        return True
    else:
        return False   

def questionhealer():
    try:
        lives = int(input('How many lives have you saved :'))
    except ValueError:
        print('please enter a number.')
        questionhealer()
    if lives > 2:
        return True
    else:
        return False

def questionhealer2():
    try:
        lives = int(input('How many lives have you lost :'))
    except ValueError:
        print('please enter a number.')
        questionhealer2()
    if lives > 1:
        return True
    else:
        return False

def questioninvestor():
    try:
        pouch = int(input('How much gold do you have: '))
    except ValueError:
        ('Please enter an amount in numbers.')
        questioninvestor()
    if pouch > 300:
        global totalgroupgold
        totalgroupgold = pouch
        return True
    else:
        return False

def questioninvestor2():

        company = input('What is the name of your company: ')
        return company

def questionranger():
    guide = int(input('How many times have you been a guide so far: '))
    if guide < 2:
        return False
    elif guide > 1:
        return True

def questionranger2():
    certificate = input('Do you have a certificate for your job: ')
    certificate.lower
    if certificate == "yes":
        return True
    elif certificate == "no":
        return False
    else:
        print('Please type either Yes or No.')
        questionranger2()

def signup():
    welcome()
    quest1 = question1()
    if quest1 <= 15:
        print('you\'re not old enough, Sorry.') # open 1 
        return 0
    quest2 = question2() # closed 1
    if quest2 == "yes":
        print()
    else:
        print('Sorry, You\'re not experienced enough') # open 2 
        return 0
    quest3 = question3()#closed 3 
    if quest3 == True:
        print()
    else:
        return 0
    quest4 = question4()#closed 4 
    if quest4 == True:
        print()
    else:
        return 0
    quest5 = question5() #open 3

    if quest5 == True:
        print()
    else:
        return False
    
    match job:
            case "healer":
                healer = questionhealer()
                if healer == True:
                    print()
                else:
                    print("Sorry, you\'re not a good fit for us")
                    return 0
                healer2 = questionhealer2()
                if healer2 == True:
                    print()
                else:
                    print("Sorry, you\'re not a good fit for us")
                    return 0            
            case "investor":
                questinvestor = questioninvestor()
                if questinvestor == True:
                    print()
                else:
                    return 0
                questinvestor2 = questioninvestor2()
                print(questinvestor2, ",I know of that company, It has a very good reputation.\nYou\'re hired!")
            case "ranger":
                questranger = questionranger()
                
                if questranger == True:
                    print()
                else:
                    return 0
                questranger2 = questionranger2()
                if questranger2 == True:
                    print('You\'re hired!')
                else:
                    return 0
            case "thief":
                thief = questionthief()
                if thief == False:
                    print('Sorry, You\'re not a good fit for us')
                    return 0
                thief2 = questionthief2()
                if thief2 == False:
                    print('Sorry, You\'re not a good fit for us')
                    return 0
                Accept = True
                print('Congratulations, you\'ve been accepted!')
for _ in range(people):
    signup()
shovel,shovelamount = 0,0
climbing,climbingamount = 0,0
latern,amountlatern = 0,0
oil,oilamount = 0,0
rod,rodamount = 0,0
tinder,tinderamount = 0,0
backpack,backpackamount = 0,0
rope,ropeamount = 0,0
musk,muskamount = 0,0
torch,torchamount = 0,0
pouch,pouchamount = 0,0
def welcomer():
    print('You have',people,"with you.")
    print('It\'s time to shop, as your group enter the store, you hear a bell ring\nand the shop keeper walks over, your group engages in conversation with the shop keeper.')

def sale():
    print('In my shop I will list all items which I sell\n and ask for the amount of them you want')
    global shovelamount
    shovelamount = int(input("How many shovels would you like to buy\n they're 2 gold each: "))
    for x in range(shovelamount):
        global shovel
        shovel = shovel+2
        shovel = float(round(shovel, 2))

    print('Great that will be,',(shovel)," gold")

    global climbing
    climbingamount = int(input("How many climbing packs would you like to buy\n they're 14 gold each: "))
    for x in range(climbingamount):
        global climbing
        climbing = climbing+14
        climbing = float(round(climbing, 2))

    print('Great that will be,',(climbing)," gold")

    global amountlatern
    amountlatern = int(input("How many lanterns would you like to buy\n they're 4 gold each: "))
    for x in range(amountlatern):
        global latern
        latern = latern+4 
        latern = float(round(latern, 2))

    print('Great that will be,',(latern)," gold")

    global oilamount
    oilamount = int(input("How much oil would you like to buy\n they're 4 gold each: "))
    for x in range(oilamount):
        global oil
        oil = oil+0.22
        oil = float(round(oil, 2))

    print('Great that will be,',(oil)," gold")    

    global rodamount
    rodamount = int(input("How many fishing rods would you like to buy\n they're 4 gold each: "))
    for x in range(rodamount):
        global rod
        rod = rod+2
        rod = float(round(rod, 2))

    print('Great that will be,',(rod)," gold")

    global tinderamount
    tinderamount = int(input("How many tinder boxes would you like to buy\n they're 4 gold each: "))
    for x in range(tinderamount):
        global tinder
        tinder = tinder+0.4
        tinder = float(round(tinder, 2))

    print('Great that will be,',(tinder)," gold") 

    global backpackamount
    backpackamount = int(input("How many backpacks would you like to buy\n they're 4 gold each: "))
    for x in range(backpackamount):
        global backpack
        backpack = backpack+3
        backpack = float(round(backpack, 2))

    print('Great that will be,',(backpack)," gold")

    global ropeamount
    ropeamount = int(input("How many meters of rope would you like to buy\n they're 4 gold each: "))
    for x in range(ropeamount):
        global rope
        rope = rope+0.14
        rope = float(round(rope, 2))

    print('Great that will be,',(rope)," gold")

    global muskamount
    muskamount = int(input("How many muskeeto nets would you like to buy\n they're 4 gold each: "))
    for x in range(muskamount):
        global musk
        musk = musk+0.12
        musk = float(round(musk, 2))
    print('Great that will be,',(musk)," gold")

    global torchamount
    torchamount = int(input("How many torches would you like to buy\n they're 4 gold each: "))
    for x in range(torchamount):
        global torch
        torch = torch+0.3
        torch = float(round(torch, 2))
    print('Great that will be,',(torch)," gold")

    global pouchamount
    pouchamount = int(input("How many water pouches would you like to buy\n they're 4 gold each: "))
    for x in range(pouchamount):
        global pouch
        pouch = pouch+4
        pouch = pouch = float(round(pouch, 2))
    print('Great that will be,',(pouch)," gold")
    return(shovel + climbing + latern + oil + rod + tinder + backpack + rope + musk + torch + pouch)
a = sale()


totalgroupgold = totalgroupgold - a
a = float(round(a, 2))
totalgroupgold = float(round(totalgroupgold,2))
print(a,"This will be your total bill.")
print(totalgroupgold,"this is the amount of gold you've left.")


import time
def dialog():
    print('group: Hey guys, does something about this bridge seem off to you too?\nIt definitely looks like someone\n lives under this bridge, I wonder who?')
    time.sleep(3)
    print('The troll: It is I, The troll of the bridge\n You wont be able to enter unless you solve my riddles\n but be wary, They\'re not easy\n and if you fail them, It will cost you money!')
    time.sleep(3)
    print('The troll: Het gemiddelde van 3 getallen is 21. Een getal is 15, de andere 2 zijn het zelfde, wat getal is dat?')
    time.sleep(5)
    print('group: 12.66?')
    time.sleep(3)
    print('Als 2 kip 8 eieren leggen in 3 dagen. Hoeveel eieren leggen 3 kippen in een week?')
    time.sleep(3)
    print('16 eieren')
    time.sleep(3)
    print('Hoe vaak komt het cijfer 6 voor tussen 7 en 111?')
    time.sleep(3)
    print('Five times.')
    time.sleep(3)
    print('Correct!\nI suppose, I\'ll have to let you guys pass now.')
dialog()

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
chest = chest + totalgroupgold
chest = chest -55
print("group: Since we're so rich now we don\'t have to do any riddles, We can just pay the 55 gold fine")
chest2 = chest * 0.20
chest = chest - chest2
print(chest,"Gold coins is in the chest!!")

chest = chest / people
print('everyone ends up getting: ', chest)
