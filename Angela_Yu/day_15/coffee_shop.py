from first import resources
from first import MENU
profit = 0
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return is_enough
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received- drink_cost,2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money Refunded")
        return False

def make(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    typeof = input("What would You like? (expresso/cappuccino/latte)")
    if typeof == "off":
        is_on = False

    elif typeof == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:{profit}")

    else:
        drink = MENU[typeof]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make(typeof, drink["ingredients"])
