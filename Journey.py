def theamount():
    try:
        amount = int(input("Enter the amount: "))
    except ValueError:
        print('Only numbers are allowed, Please try again.')
        theamount()
    return amount

def conversion():
    currency = input('Please enter your desired currency choose from : Copper, silver, gold or platinum : ')
    currency.lower
    match currency:
        case "copper":
            print("Your currency is copper, but the total amount in the end will be shown in gold.")
            currency = currency / 50
        case "silver":
            print('Your currency is silver, but the total amount in the end will be shown in gold.')
            currency = currency / 10
        
        case "gold":
            print('Your currency is gold, but the total amount in the end will be shown in gold.')

        case "platinum":
            print('Your currency is platinum, but the total amount in the end will be shown in gold.')
            currency = currency * 24

    return currency
