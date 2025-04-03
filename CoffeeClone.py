from Data import MENU
from logo import logo
print(logo)

#global variables
resources = {
            "water": 300,
            "milk" : 200,
            "coffee" : 75,
}
profit = 0.0


def report():
    print(f"Water = {resources['water']} ml")
    print(f"Milk = {resources['milk']} ml")
    print(f"Coffee = {resources['coffee']} ml")
    print(f"Money = ${profit:.2f}")

def resource_check(dict):
    for items in dict["ingredients"]:
        if dict["ingredients"][items] > resources.get(items,0):
            print("Sorry! We don't have enough resources to make your coffee!")
            return False
        else:
            return True

def transaction(dict):
    print("Enter the coins...")
    qtr = int(input("Quarters: "))
    dime = int(input("Dimes: "))
    nick = int(input("Nickles: "))
    penn = int(input("Pennies: "))

    Cust_given_money = 0.25*qtr + 0.1*dime + 0.05*nick + 0.01*penn
    if Cust_given_money >= dict["cost"]:
        return Cust_given_money - dict["cost"]
    else:
        return -1


def make_coffee(coffee_name , ingredients ):
    global profit
    for items in ingredients:
        resources[items] -= ingredients[items]
    profit += MENU[coffee_name]["cost"]
    print(f"Here is your {coffee_name} coffee...ENJOY!!")





def main():

    turn_ON = True

    while turn_ON:

        print("Welcome! to the coffee machine...make a following selection: ")
        selection = input(f"espresso / latte / cappuccino / report / off ").lower() #selection == latte
        if selection == 'report':
            report()
        elif selection == 'off':
            turn_ON = False
            print("Turning off machine...")
        elif selection in MENU :
            drink_dict = MENU[selection] #entire latte dict
            if resource_check(drink_dict):
                print(f"Price for a {selection} {drink_dict['cost']} USD")
                change = transaction(drink_dict)
                if change == -1:
                    print(f"You Don't have enough money!...Money refunded")

                else:
                    make_coffee(selection , drink_dict["ingredients"])
                    print(f"Here's your {change}")
        else:
            print("Invalid input!!")





main()