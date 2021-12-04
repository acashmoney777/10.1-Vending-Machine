#Akash Srinivasan
#CSE20
#12/3/2021
#10.1 making our own project, mine is a vending machine, like a really advanced one


class VendingMachine():

    def __init__(self, chips, soda, candy, inventory):
        self.chips = chips
        self.soda = soda
        self.candy = candy
        self.cashregister = inventory
        #constructor class
    

    def start(self): #starts and acts as the main menu
        self.options = input("buy, stock, inventory, prices: ")
        #buy is where u purchase food
        #stock is where a person would refill the machine
        #Status shows how much is left
        if self.options == "buy":
            self.purchase()
            #if buy is typed in, this function is called
        elif self.options == "stock":
            self.stock()
            #if stock is entered, this function is called
        elif self.options == "inventory":
            self.inventory()
            #if inventory is entered, this function is called
        elif self.options == "prices":
            self.get_prices()
            #shows prices

    def exit(self): #returns to the main menu (self.start())
        self.start()

    def supplies(self): # checks if there are enough supplies
        self.inventory()

    def get_prices(self):
        chip_prices = {'Cheetos': 1.50, 'Potato Chips': 1.50, 'Doritos': 1.50}
        soda_prices = {'Coke': 2, 'Dr Pepper': 2, 'Pepsi': 2, 'Sprite': 2}
        candy_prices = {'Skittles': 0.50, 'M&Ms': 0.50, 'Snickers': 0.50}
        return chip_prices, soda_prices, candy_prices


    def purchase(self): #purchase method
        self.choice = input("What would you like to buy? \n  1: Soda, 2: Chips or 3: Candy? ")
        #input what type of snack u want
        if self.choice == '1':
            secondchoice = input("1: Coke, 2: Pepsi, 3: Dr Pepper, or 4: Sprite ")
            #if soda inputted, you get choice between 4 drinks
            if secondchoice == '1':
                #Coke has different flavors so you get to choose again in the thirdchoice variable
                thirdchoice = input("1: Diet, 2: Normal, or 3: Zero Sugar ")
                if thirdchoice == "1":
                    if self.soda <= 0:
                        #checks the 
                        print("Sorry we don't have this anymore")
                    else:
                        print("Diet Coke ($2) has been dispensed!")
                    self.cashregister += float(2)
                    self.soda -= float(1)
                    self.exit()
                elif thirdchoice == "2":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Normal Coke ($2) has been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "3":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Coke Zero ($2) has been dispensed")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()

            elif secondchoice == '2':
                thirdchoice = input("1: Diet, 2: Normal, or 3: Zero Sugar")
                if thirdchoice == "1":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Diet Pepsi ($2) has been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "2":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Normal Pepsi ($2) has been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "3":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Pepsi Zero Sugar ($2) has been dispensed")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()

            elif secondchoice == '3':
                thirdchoice = input("1: Diet, 2: Normal, or 3: Zero Sugar")
                if thirdchoice == "1":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Diet Dr Pepper ($2) has been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "2":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Normal Dr Pepper ($2) has been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "3":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Dr Pepper Zero Sugar ($2) has been dispensed")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()

            elif secondchoice == '4':
                thirdchoice = input("1: Diet, 2: Normal, or 3: Zero Sugar")
                if thirdchoice == "1":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Diet Coke has ($2) been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "2":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Normal Sprite ($2) has been dispensed!")
                    self.soda -= float(1)
                    self.cashregister += float(2)
                    self.exit()
                elif thirdchoice == "3":
                    if self.soda <= 0:
                        print("Sorry we don't have this anymore")
                    else:
                        print("Cranberry Sprite ($45) has been dispensed")
                    self.soda -= float(1)
                    self.cashregister += float(45)
                    #maybe an audio file of lebron saying "Want a sprite cranberry" should play
                    self.exit()

        elif self.choice == "2":
            secondchoice = input("1: Cheetos, 2: Potato Chips, or 3: Doritos")
  
            if secondchoice == '1':
                if self.chips <= 0:
                    print("Sorry we don't have this anymore")
                else:
                    print("Your cheetos ($1.50) have been dispensed!")
                self.chips -= float(1)
                self.cashregister += float(1.50)
                self.exit()

            if secondchoice == "2":
                if self.chips <= 0:
                    print("Sorry we don't have this anymore")
                else:
                    print('Your chips ($1.50) have been dispensed!')
                self.chips -= float(1)
                self.cashregister += float(1.50)
                self.exit()

            if secondchoice == "3":
                if self.chips <= 0:
                    print("Sorry we don't have this anymore")
                else:
                    print("Your Doritos ($1.50) have been dispensed!")
                self.chips -= float(1)
                self.cashregister += float(1.50)
                #write something to make the inventory go down between each cycle
                self.exit()

        elif self.choice == "3":
            secondchoice = input("1: Snickers, 2: Skittles, or 3: M&Ms")

            if secondchoice == '1':
                if self.candy <= 0:
                    print("Sorry we don't have this anymore")
                else:
                    print("Your candy ($0.50) has been dispensed!")
                self.candy -= float(1)
                self.cashregister += float(.50)
                self.exit()

            if secondchoice == '2':
                self.candy -= float(1)
                self.cashregister += float(.50)
                if self.candy <= 0:
                    print("Sorry we don't have this anymore")
                else:
                    print("Your candy ($.50) has been dispensed!")
                self.exit()
        
            if secondchoice == '3':
                print("Your candy ($.50) has been dispensed!")
                self.candy -= float(1)
                self.cashregister += float(.50)
                self.exit()

    def stock(self): #Allows you to refill machine
        print(f"it costs $50 to stock the machine. We have ${self.cashregister} left")
        #Costs $50 to refill
        if self.cashregister < int(50):
            print("you cannot refill it now")
        self.candy += int(input("Enter how many units of candy you want to stock: "))
        self.soda += int(input("Enter how many units of soda you want to stock: "))
        self.chips += int(input("Enter how many units of chips you want to stock: "))
        self.cashregister -= 50
        self.inventory()
        self.exit()

    def inventory(self):
        print("The vending machine has: ")
        print(f"{self.chips} bags of chips left")
        print(f"{self.soda} cans of soda left")
        print(f"{self.candy} candy bars left")
        print(f"${self.cashregister:.2f} dollars left")
        self.exit() 

    def main():
        vend = VendingMachine(1,2,3,4)
        print(vend.start())
    if __name__ == '__init__':
        print(main())
    #if this don't work, try this:
    ###
    #vend = VendingMachine(1,2,3,4)
    #print(vend.start())

