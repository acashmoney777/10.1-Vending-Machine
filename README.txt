The assignment was to do a Class that was modeled after a real world object and so I chose to do my class after a vending machine. Vending machine was a good and easy idea because there’s a lot of options that came with it so it was very easy to decide the direction I wanted to go with it. The vending machine sells candy, chips, and soda and also keeps an inventory of how much chips, candy, soda, and money in the machine


* __init__ method: is the constructor method and I defined chips, soda, candy, and inventory(money) in it. All the important stuff is in it
   * self.chips variable: it is the chips variable
   * self.soda variable: soda variable
   * self.candy variable: candy variable
   * self.cashregister variable: lets me call it at any time, in any method
* start method: acts as a main menu and you get three options with it (buy, status, inventory). Buy is where you buy food, inventory is how much of each item defined in the constructor is left, and stock allows you to add items to it for the price of $50 so the vending machine inventory has to have at least $50 to refill it
* exit method: returns user to main menu by calling start function. More convenient and easy for me to use this than using a while loop
* supplies method: checks if there are enough supplies. Kind of just a placeholder method, can’t lie
* get_prices method: has the prices defined and returns them. To use it, you have to enter prices at the main menu
* purchase method: goes through the snacks and gives you options to choose from. Deducts one snack from inventory and adds the appropriate sum of money to inventory/cash register
   * self.choice variable: used self so I didn’t have to access the variable later and just write it once but here you input what snack you want. It asks you what snack you want and you just enter a number 1-4 depending on the options
   * secondchoice variable: is called 2nd choice because it's the second choice you make and you choose what specific drink you want. Also has input, you just enter the number and it dispenses what you chose
   * thirdchoice variable: depends on the secondchoice variable and what you chose but it's the same thing as the secondchoice concept-wise
* stock method: Allows user to refill the machine, does this with += and incrementation
* inventory method: just shows how much is in the machine and returns some print statements


In my main(), I just called the necessary functions so you can run it and experience the magic of my program for yourself