from data import MENU, resources


def exchange(key):
    drink_cost = MENU[key]["cost"]
    quarters = 0.25 * int(input("how many quarters?: "))
    dimes = 0.10 * int(input("how many dimes?: "))
    nickles = 0.05 * int(input("how many nickles?: "))
    pennies = 0.01 * int(input("how many pennies?: "))
    user_total = quarters + dimes + nickles + pennies

    if user_total >= drink_cost:
        resources["cost"] += drink_cost
        print(f"Here is ${format(user_total-drink_cost, '.1f')} in change.")
        print(f"Here is your {key} ☕️. Enjoy!")

    else:
        print("Sorry that's not enough money. Money refunded.")


def check_resources(key):
    machine_water = int(resources['water'])
    machine_milk = int(resources['milk'])
    machine_coffee = int(resources['coffee'])
    drink_water = int(MENU[key]["ingredients"]["water"])
    drink_milk = int(MENU[key]["ingredients"]["milk"])
    drink_coffee = int(MENU[key]["ingredients"]["coffee"])

    if machine_water >= drink_water:
        if machine_milk >= drink_milk:
            if machine_coffee >= drink_coffee:
                resources['water'] -= drink_water
                resources['milk'] -= drink_milk
                resources['coffee'] -= drink_coffee
            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough milk")
            return False
    else:
        print("Sorry there is not enough water")
        return False

    return True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['cost']}")


off = False
while not off:
    enough_money = False
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        off = True
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        enough_resources = check_resources(user_choice)
        if enough_resources:
            exchange(user_choice)
    elif user_choice == "report":
        report()
    else:
        print("Please enter a valid keyword")