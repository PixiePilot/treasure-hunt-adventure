#sing up, Certain questions asked to not waste time.

def welcome():
    print('Welcome to the Team sing up program\nCertain questions will be asked to ensure that you\'re a good fit.\nGoodluck!')
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
        case "investor":
            print()
        case "ranger":
            print()
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

signup()
