#!/usr/bin/python3

# TODO: 
# - Quest System
# - Story Proggression
# - Better Market Price Changes

#---------------------------Imports-----------------------------------

from sys import exit
import os
import random
import time
import readline

#----------------------Global Variables-------------------------------

# Static
currency        = " IIP"
currency_long   = " Imaginary Internet Points"
action_commands = [ "market", "stats", "mission", "sleep", "help", "exit", "clear" ]

# Simple 
money = 0     # Your Balance
miss  = 0     # ???
commands = [] # Auto complete options 

#-----------------------Utility Functions----------------------------

# Auto complete
def set_completer_options(options):
    global commands
    commands = options
    readline.set_completer(completer)

def completer(text, state):
    global commands
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

# Input with Prompt
def get_input(prompt = "> "):
    raw = input(prompt)
    return raw.strip()

# Choice select with ordered list answers
def multiple_choice_input(required, question, answers):
    while True:
        print(question)
        time.sleep(0.5)
        for i in range(len(answers)):
            print(str(i+1) + ". " + answers[i])
        
        answer = get_input()
        if answer.isdigit():
            answer = int(answer)
            if 0 < answer and answer <= len(answers):
                return str(answer)

        if not required:
            return -1;

        print()

# Choice select with two choice
def two_choice_input(required, question, answer1="y", answer2="n"):
    set_completer_options([answer1,answer2])
    while True:
        prompt = question + " (" + answer1 + "/"+ answer2 + ") "
        answer = get_input(prompt)
        if answer.lower() == answer1.lower():
            return answer1
        elif answer.lower() == answer2.lower():
            return answer2

        if not required:
            return -1;

        print()


#-----------------------Inventory Management-------------------------


def is_thing(item, name):
    return item.name == name

def is_nothing(item):
    return item.amount > 0

class Item:
    def __init__(self, name, unique, amount=1):
        self.name   = name
        self.amount = amount
        self.unique = unique
    
class Inventory:
    def __init__(self):
        self.items = [ ]
    
    def __contains__(self, name):
        return self.contains(name)

    def contains(self, name):
        for item in self.items:
            if item.name == name:
                return True
        return False

    def add(self, name, unique, amount=1):
        if self.contains(name):
            for item in self.items:
                if(item.name == name):
                    item.amount += amount
                    break
        else:
            self.items.append( Item(name,unique,amount) )
    
    def remove_all(self, name):
        self.items = filter(lambda x: x[0] not in name, self.items)

    def remove(self, name, amount=1):
        if self.contains(name):
            for item in self.items:
                if(item.name == name):
                    item.amount -= amount
                    break
        self.items = list(filter(is_nothing, self.items))
    
    def count(self):
        return len(self.items)

    def get_item(self, name):
        return list(filter(lambda x: x[0] in name, self.items))[0]

    def item_names(self):
        names = []
        for item in self.items:
            names.append(item.name)
        return names

    def show(self):
        for item in self.items:
            if item.unique:
                print(item.name)
            else:
                print(item.name + " " + str(item.amount) + "x" )
        print()

inventory = Inventory()

#-------------------------------Market--------------------------------

class Market:
    def __init__(self):
        self.price_table  = {
        # Name | Price
        "cactus"   :15,
        "bed"      :20,
        "nigger"   :10,
        "mug"      :5,
        "toy train":5
        }
    def check_price(self, name):
        if self.has(name):
            return self.price_table[name]
        return -1

    def has(self, name):
        if name in self.price_table:
            return True
        return False
    
    def item_names(self):
        return self.price_table.keys()

    def refresh(self):
        for name in self.price_table:
            change = random.randint(-5,5)
            self.price_table[name] += change

    def show(self):
        for name in self.price_table:
            price = self.price_table[name]
            print(name + " " + str(price) + currency)
        print()

    # Dialogs
    def dialog(self):
        global inventory
        choice = two_choice_input(False,"Do you want to?","buy","sell")
        if (choice == "sell"):
            self.sell_dialog()
        elif (choice == "buy"):
            self.buy_dialog()
        else:
            print("Then we are done")
        
    def sell_dialog(self):
        global inventory
        global money
        
        inventory.show()
        set_completer_options(inventory.item_names())

        item_to_sell = get_input("Which item would you like to sell? ")

        if item_to_sell in inventory:
            money += self.price_table[item_to_sell]
            inventory.remove(item_to_sell)
        else:
            print("You don't have '" + item_to_sell + "' in your inventory.")

    def buy_dialog(self):
        global money
        print("Market")
        self.show()
        set_completer_options(self.item_names())
        item = get_input("What would you like to buy?")
        if self.has(item):
            # TODO: Check if unique item
            price = self.price_table[item]
            if(money < price):
                print("You don't have enough money to buy this")
            else:
                answer = two_choice_input(False,"Do you want to purchase " + item + " for " + str(price) + currency + "?")
                if answer:
                    money -= price
                    inventory.add(item, False)
                else:
                    print("I am sorry to hear that")
        else:
            print("Sorry we dont have any in stock.")

market = Market()

#----------------------------Name Creation----------------------------

choice = multiple_choice_input(False,
    "What is your name peasant?",
    [ "I'm not a peasant",
      "What's your name",
      "My name is..." ])

if (choice == "1"):
    name = "peasant boy"
    print("Okay then " + name)
elif (choice == "2"):
    print("You don't deserve to know my name")
elif (choice=="3"):
    while True:
        name = get_input("Enter your name: ")
        answer = two_choice_input(False,"So you are " + name + " is that correct?","y","n")
        if answer:
            print("That name is kinda gay but okay...")
            break
        else:
            print("BRUH")
else:
    name = "stupid bitch who doesn't know how to answer"
    print("Then your name shall be " + name + "!")

#--------------------------------------------------------------------

#TODO: Can be renamed to prolouge...
def story():
    global inventory
    choice = multiple_choice_input( False,
            "Your first mission will be really important you have to sell this cactus",
            [ "But where am I",
              "Why?",
              "Ok?"])

    if(choice == "1"):
        print("You are here")
    elif(choice == "2"):
        print("There is no time for questions hurry and sell that goddamm cactus")
    elif(choice == "3"):
        print("Then don't just stand there hurry")

    inventory.add("cactus",False,1)

    time.sleep(0.5)

    print()
    print("You can buy or sell items in the market to go there you just have to type the word 'market'")
    print( "If you are done type in the word 'mission' to continue the story.")

    action()


#---------------------------------------------------------------------------------------------------------------

def action():
    global market
    while True:
        set_completer_options(action_commands)
        act = get_input()
        match act:
            case "market":
                market.dialog()
            case "stats":
                stats()
            case "mission":
                mission()
            case "sleep":
                sleep()
            case "help":
                helps()
            case "clear":
                print(chr(27) + "[2J")
            case "exit":
                exit(0)           

#--------------------------------

def helps():
    # TODO: Details about the commands
    global commands
    print(f"{'Help' :=^10}")
    for cmd in commands:
        print(cmd)

#-------------------------------------------------

#TODO: Style
def stats():
    global inventory
    print("Balance: " + str(money) + currency_long)
    print("Inventory")
    inventory.show()

#-------------------------------------------------

def sleep():
    market.refresh()

#-------------------------------------------------

def mission():
    global miss
    global money
    
    if(miss == 2):
        if(money<100):
            print("What are you waiting for?! GO MAKE SOME MONEY!!!!")
        else:
            print("Ok")
    if(miss == 1):
        if("nigger" in inventory ):
            print("That's a nice one with him around I don't have to clean my house anymore")
            miss+=1
            print("For your next mission you'll have to have 100iip")
            print("to earn money you'll have to buy low sell high")
            print("the market changes evey day")
            print("to sleep type in sleep")

        else:
            print("Where is my nigger??")
    if(miss == 0):
        if("cactus" in inventory):
            print("Sell the fucking cactus on the market")
        else:
            print("Nice job very well done")
            time.sleep(0.5)
            print("Here is 10 iip for your services")
            money+=10
            time.sleep(0.5)
            print("Your next mission will be to buy a nigger and deliver it to me")
            miss+=1














story()
