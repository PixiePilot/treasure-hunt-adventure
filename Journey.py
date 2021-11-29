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
        people = float(input('How many people are you with: '))
    except ValueError:
        print('Please enter a number.')
        costs()
    horse = 0.8 / 2
    tent = 8
    inn = 0.4
    innhorse = 0.18
    price = float(tent + inn + innhorse + horse)
    price = people * price + 4
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
