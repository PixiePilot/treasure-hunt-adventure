# list Schep = 4 ( 2 gold per)
# climbing equipment 14 gold per ( not needed )
#lantern 4 gold per tent ( x people)
#lamp oil 11 copper per (x people + 1 )
#fishing rod 2 gold per ( x 2)
#tinderbox 4silver per ( x3 )
#backpack 3gold per (  x people)
#rope 7 copper per M ( x12)
#muskeeto net 6 copper per m2 ( none)
#torch 3 silver per ( x people)
#water pouch 4 gold per ( x people + 1 )
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
    print('It\'s time to shop, as your group enter the store, you hear a bell ring\nand the shop keeper walks over, your group engages in conversation with the shop keeper.')

def sale():
    print('In my shop I will list all items which I sell\n and ask for the amount of them you want')
    global shovelamount
    shovelamount = int(input("How many shovels would you like to buy\n they're 2 gold each: "))
    for x in range(shovelamount):
        global shovel
        shovel = shovel+2
    print('Great that will be,',(shovel)," gold")

    global climbing
    climbingamount = int(input("How many climbing packs would you like to buy\n they're 14 gold each: "))
    for x in range(climbingamount):
        global climbing
        climbing = climbing+14
    print('Great that will be,',(climbing)," gold")

    global amountlatern
    amountlatern = int(input("How many lanterns would you like to buy\n they're 4 gold each: "))
    for x in range(amountlatern):
        global latern
        latern = latern+4 
    print('Great that will be,',(latern)," gold")

    global oilamount
    oilamount = int(input("How much oil would you like to buy\n they're 4 gold each: "))
    for x in range(oilamount):
        global oil
        oil = oil+0.22
    print('Great that will be,',(oil)," gold")    

    global rodamount
    rodamount = int(input("How many fishing rods would you like to buy\n they're 4 gold each: "))
    for x in range(rodamount):
        global rod
        rod = rod+2
    print('Great that will be,',(rod)," gold")

    global tinderamount
    tinderamount = int(input("How many tinder boxes would you like to buy\n they're 4 gold each: "))
    for x in range(tinderamount):
        global tinder
        tinder = tinder+0.4
    print('Great that will be,',(tinder)," gold") 

    global backpackamount
    backpackamount = int(input("How many backpacks would you like to buy\n they're 4 gold each: "))
    for x in range(backpackamount):
        global backpack
        backpack = backpack+3
    print('Great that will be,',(backpack)," gold")

    global ropeamount
    ropeamount = int(input("How many meters of rope would you like to buy\n they're 4 gold each: "))
    for x in range(ropeamount):
        global rope
        rope = rope+3
    print('Great that will be,',(rope)," gold")

    global backpackamount
    backpackamount = int(input("How many tinder boxes would you like to buy\n they're 4 gold each: "))
    for x in range(backpackamount):
        global backpack
        backpack = backpack+3
    print('Great that will be,',(backpack)," gold")

sale()
