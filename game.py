#----------------------------imports----------------------------------
import random
#----------------------------items------------------------------------
youritems = []
money=0
youritemcount=0
miss=0
item={
        "cactus":15,
        "bed":20,
        "nigger":10,
        "mug":5,
        "toy train":5
    }
#----------------------------name creation----------------------------
namecreated=0
print("what is your name peasant")
input()
print("1, I'm not a peasant")
print("2, What's your name")
print("3, My name is...")
choice=input()
if (choice=="1"):
    print("Okay then peasant boy")
    name="peasantboy"
elif (choice=="2"):
    print("You don't deserve to know my name")
elif (choice=="3"):
    while namecreated==0:
        print("Enter your name: ")
        name=input()
        print("so you are "+name+" is that correct?(y/n)")
        answer=input()
        if(answer=="y"):
            print("that name is kinda gay but okay")
            namecreated=1
        if(answer=="n"):
            print("BRUH")
else:
    print("then your name shall be stupid bitch who doesn't know how to answer")
    name="stupid bitch who doesn't know how to answer"
#--------------------------------------------------------------------
def story():
    global youritemcount
    global youritems
    print("Your first mission will be really important you have to sell this cactus")
    input()
    print("1, But where am I")
    print("2, Why?")
    print("3, Ok?")
    choice=input()
    if(choice=="2"):
        print("There is no time for questions hurry and sell that goddamm cactus")
    elif(choice=="1"):
        print("You are here")
    elif(choice=="3"):
        print("Then don't just stand there hurry")

    youritemcount=youritemcount+1
    youritems.append("cactus")
    input()
    print("you can buy or sell items in the market to go there you just have to type the word market")
    print("if you are done type in the word mission to continue the story")
    action()



#---------------------------------------------------------------------------------------------------------------
def action():
    while True:
        act=input()
        if (act=="market"):
            market()
            continue
        if(act=="stats"):
            stats()
            continue
        if(act=="mission"):
            mission()
            continue
        if(act=="sleep"):
            sleep()
        if(act=="help"):
            helps()
#--------------------------------
def helps():
    print("market")
    print("stats")
    print("mission")
    print("sleep")
    print("help")
#---------------------------
def market():
    global youritems
    print("do you want? (buy/sell)")
    choice=input()
    if (choice=="sell"):
        sell()
    elif (choice=="buy"):
        buy()
    else:
        print("Then we are done")
#-------------------------------------------
def sell():
    global youritems
    print("which item would you like to sell")
    for x in youritems:
        print(x)
    itemtosell=input()
    if(youritems.__contains__(itemtosell)==True):
        items(itemtosell)
    else:
        print("you dont have that item in your inventory")
#------------------------------------------------
def items(it):
    global item
    print("This item is worth "+str(item[it])+" iip")
    print("Do you want to sell it for this price(y/n)")
    inp=input()
    if(inp=="y"):
        sold(item[it],it)
    else:
        print("Bruh")
#-------------------------------------------------
def sold(a,b):
    global money
    global youritems
    money+=a
    youritems.remove(b)
#-------------------------------------------------
def stats():
    print("money: "+str(money)+" imaginary internet points")
    print("inventory")
    for x in youritems:
        print("    "+x)
#-------------------------------------------------
def buy():
    print("What would you like to buy")
    for x in item:
        print(x+":"+str(item[x])+" iip")
    inp=input()
    if(item.__contains__(inp)==True):
        bought(inp)
    else:
        print("sorry we dont have any in stock")
#--------------------------------------------------
def bought(a):
    global money
    global youritems
    if(money<item[a]):
        print("you don't have enough money to buy this")
    else:
        print("do you want to purchase "+a+"for "+str(item[a])+" iip (y/n)")
        inp=input()
        if(inp=="y"):
            money-=item[a]
            youritems.append(a)
        else:
            print("I am sorry to hear that")
#-------------------------------------------------
def sleep():
    for x in item:
        marketchange=random.randint(-5,5)
        item[x]+=marketchange
#-------------------------------------------------
def mission():
    global miss
    global money
    
    if(miss==2):
        if(money<100):
            print("what are you waiting for. Go MAKE SOME MONEY")
        else:
            print("Ok")
    if(miss==1):
        if(youritems.__contains__("nigger")):
            print("That's a nice one with him around I don't have to clean my house anymore")
            miss+=1
            print("For your next mission you'll have to have 100iip")
            print("to earn money you'll have to buy low sell high")
            print("the market changes evey day")
            print("to sleep type in sleep")

        else:
            print("Where is my nigger??")
    if(miss==0):
        if(youritems.__contains__("cactus")):
            print("sell the fucking cactus on the market")
        else:
            print("Nice job very well done")
            input()
            print("Here is 10 iip for your services")
            money+=10
            input()
            print("Your next mission will be to buy a nigger and deliver it to me")
            miss+=1
story()
