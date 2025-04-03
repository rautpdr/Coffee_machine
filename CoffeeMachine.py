


#user choice function for coffee

#report
## add to profit , resorces should also update

#resources
##coffe resources, resources should deduct if coffee is done

#resource_tracking
#transaction_check(boolean)
#transaction_calculation


from logo import logo
from Data import MENU

#constants
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0.0


def make_coffee(coffee_name , ingredients):
    global profit
    for items in ingredients :
        resources[items] -= ingredients[items]
    profit += MENU[coffee_name]["cost"]
    print(f"Here's your {coffee_name} coffee!Enjoy")
    return


def give_report():
    print(f"Milk = {resources['milk']} ml")
    print(f"Water = {resources['water']} ml")
    print(f"Coffee = {resources['coffee']} ml")
    print(f"Money = ${profit:.2f}")


def report_cal(drink):
    #print logic
    for items in drink["ingredients"]:
        if drink["ingredients"][items]  > resources.get(items , 0)  :
            print("not enough resources to complete the order!")
            return False
        else:
            return True


def transaction_calculation():
    #logic
    print("Please insert coins.")
    qtr = int(input("How many quarters "))
    dime = int(input("How many dimes "))
    nick = int(input("How many nickles "))
    penn = int(input("How many pennies "))

    user_money = 0.25*qtr + 0.1*dime + 0.05*nick + 0.01*penn
    return user_money


def transaction_aut(auth_money, user_money):
    if user_money >= auth_money:
        return True
    else:
        return False



#main func
def machine():
    isON = True

    while isON:
        print("Welcome!")
        choice = input("What coffee would you like today, We have cappuccino, latte, espresso : ").lower()
        #choice == latte

        if choice == 'off':
            isON = False
            print("Turning off machine...")
            break

        elif choice == 'report':
            give_report()

        elif choice in MENU:
            drink = MENU[choice] #drink == fetching latte content ..entire dict

            if report_cal(drink):
                User_money = transaction_calculation()
                if transaction_aut(drink["cost"],User_money):
                    make_coffee(choice , drink["ingredients"])
                    change = User_money - drink["cost"]
                    print(f"Here's your change! {change}")

                else:
                    print(f"Not enough Money! refunded {User_money}")
                    break

        else:
            print("Invalid Input!")


















machine()