MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

request = ''
income = 0
while request != 'off':
    request = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if request == 'report':
        print(f'''
        Water: {resources['water']}
        Milk: {resources['milk']}
        Coffee: {resources['coffee']}
        Money: ${income}
        ''')
    elif request in MENU.keys():
        shortage = 0
        for i in MENU[request]['ingredients'].keys():
            if resources[i] < MENU[request]['ingredients'][i]:
                print(f'There is not enough {i}')
                shortage +=1
        if shortage == 0:
            print('Please insert the coins $$$')
            quarters = int(input('#Quarters: '))
            dimes = int(input('#Dimes: '))
            nickles = int(input('#nickles: '))
            pennies = int(input('#Pennies: '))
            total_coins = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
            if total_coins < MENU[request]['cost']:
                print('Sorry that\'s not enough money! :(')
            else:
                for i in MENU[request]['ingredients'].keys():
                    resources[i] -= MENU[request]['ingredients'][i]
                income += MENU[request]['cost']
                change = total_coins - MENU[request]['cost']
                print(f'Your change is ${change}')
                print(f'Here is your {request}. Enjoy!')

    else:
        print('Wrong, please re-enter the correct request! ')