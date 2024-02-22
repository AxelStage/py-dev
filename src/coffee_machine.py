MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

COINS = {
    "quarter": 25,
    "dime": 10,
    "nickle": 5,
    "penny": 1,
}

FUNCTIONS = ("off", "report", "espresso", "latte", "cappuccino")
INGREDIENTS = ("water", "milk", "coffee")

paid = {
    "quarter": 0,
    "dime": 0,
    "nickle": 0,
    "penny": 0,
}
resources = {"water": 300, "milk": 200, "coffee": 100}
money = {"total": 0}
operating = True


def is_valid(user_input):
    if user_input in FUNCTIONS:
        return True
    return False


def print_report():
    report = f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money["total"]}'
    print(report)


def has_enough_resources(coffee_choice, ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < MENU[coffee_choice]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def valid_payment(coffee_choice):
    print("Please insert coins.")
    total_payment = 0
    for coin in COINS.keys():
        user_input = input(f"How many {coin}s?: ")
        total_payment += int(user_input) * COINS[coin]

    if total_payment > (MENU[coffee_choice]["cost"] * 100):
        payback = (total_payment - MENU[coffee_choice]["cost"] * 100) / 100
        print(f"Here is ${payback} in change")

    if total_payment >= (MENU[coffee_choice]["cost"] * 100):
        money["total"] += MENU[coffee_choice]["cost"]
        return True

    missing = (MENU[coffee_choice]["cost"] * 100 - total_payment) / 100
    print(f"You paid not enough! ${missing} missing!")
    return False


def make_coffee(coffee):
    for ingredient in INGREDIENTS:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]

    print(f"Here is your {coffee}. Enjoy!")


if __name__ == "__main__":
    while operating:
        raw_user_input = input("What would you like? (espresso/latte/cappuccino):")

        if is_valid(raw_user_input) is False:
            print(f"Wrong input: {raw_user_input}")
        elif raw_user_input == "off":
            operating = False
        elif raw_user_input == "report":
            print_report()
        else:
            if has_enough_resources(raw_user_input, INGREDIENTS):
                if valid_payment(raw_user_input):
                    make_coffee(raw_user_input)
