stock = [400, 540, 120, 9, 550]
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "remaining":
        print(f'''The coffee machine has:
        {stock[0]} ml of water
        {stock[1]} ml of milk
        {stock[2]} g of coffee beans
        {stock[3]} disposable cups
        ${stock[4]} of money''')
    if action == "buy":
        buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if buy == "1":
            if stock[0] < 250:
                print("Sorry, not enough water!")
                continue
            else:
                stock[0] = stock[0] - 250
            if stock[2] < 16:
                print("Sorry, not enough coffee beans!")
                continue
            else:
                stock[2] = stock[2] - 16
            if stock[3] < 1:
                print("Sorry, not enough disposable cups!")
                continue
            else:
                stock[3] = stock[3] - 1
            stock[4] = stock[4] + 4
            print("I have enough resources, making you a coffee!")
        if buy == "2":
            if stock[0] < 350:
                print("Sorry, not enough water!")
                continue
            else:
                stock[0] = stock[0] - 350
            if stock[1] < 75:
                print("Sorry, not enough milk!")
                continue
            else:
                stock[1] = stock[1] - 75
            if stock[2] < 20:
                print("Sorry, not enough coffee beans!")
                continue
            else:
                stock[2] = stock[2] - 20
            if stock[3] < 1:
                print("Sorry, not enough disposable cups!")
                continue
            else:
                stock[3] = stock[3] - 1
            stock[4] = stock[4] + 7
            print("I have enough resources, making you a coffee!")
        if buy == "3":
            if stock[0] < 200:
                print("Sorry, not enough water!")
                continue
            else:
                stock[0] = stock[0] - 200
            if stock[1] < 100:
                print("Sorry, not enough milk!")
                continue
            else:
                stock[1] = stock[1] - 100
            if stock[2] < 12:
                print("Sorry, not enough coffee beans!")
                continue
            else:
                stock[2] = stock[2] - 12
            if stock[3] < 1:
                print("Sorry, not enough disposable cups!")
                continue
            else:
                stock[3] = stock[3] - 1
            stock[4] = stock[4] + 6
            print("I have enough resources, making you a coffee!")
        if buy == "back":
            continue
    if action == "fill":
        water = int(input("Write how many ml of water you want to add:\n"))
        milk = int(input("Write how many ml of milk you want to add:\n"))
        beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        cups = int(input("Write how many disposable cups you want to add:\n"))
        stock[0] = stock[0] + water
        stock[1] = stock[1] + milk
        stock[2] = stock[2] + beans
        stock[3] = stock[3] + cups
    if action == "take":
        print(f"I gave you ${stock[4]}")
        stock[4] = stock[4] * 0
    if action == "exit":
        break
