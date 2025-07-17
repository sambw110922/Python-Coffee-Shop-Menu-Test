
#   17 July 2025
#   This program simulates a coffee shop.

#	This is the main menu.
def Main_Menu():

    print("Welcome to the fake shop")
    print("Here are your options.")
    
    print("")
    
    #   Print the menu.
    print("1. Say 'Hello'.")
    print("2. Coffee")
    print("3. Tea")
    print("4. Specials")
    print("5. Goodbye")
    
    print("")
    
    #   The user gives their option.
    menu_choice = input("Please enter your choice 1-5: ")
   
    #   First, check to see if the option given is a number.
    
    if menu_choice.isnumeric():
    
        #   Convert the input into an int.
        menu_choice_convert = int(menu_choice)
        
        #   Next, check to see if the number is greater than 0 (not a negative) and less than 
        #   the total number of options.
        if menu_choice_convert > 0 and menu_choice_convert < 6:
    
            if menu_choice_convert == 1:  
                Say_Hello()
            elif menu_choice_convert == 2:
                Coffee_Menu()
            elif menu_choice_convert == 3:
                Tea_Menu()
            elif menu_choice_convert == 4:
                Specials_Menu()
            elif menu_choice_convert == 5:
                Goodbye()
                
        else:
            Main_Menu()
            
    else:
       Main_Menu()

#   This says hello.
def Say_Hello():

    print("You have entered option #1: Say Hello.")

    print("")
    
    print("Not many people come into a coffee shop just to say 'hello'.")
    print("But here it is.")
    print("Hello. :)")
    
    print("")
    
    #   Go back to the main menu.
    Main_Menu()

#   This is the tea menu.   
def Tea_Menu():

    print("You have entered option #3: Tea.")
    
    print("Here is your choice of tea.")
    
    print("")
    
    print("1. Regular")
    print("2. Decaff")
    print("3. Mint")
    print("4. Ginger and Lemon")
    print("5. Iced")
    print("6. Main Menu")
    
    print("")
    
    #   The user gives their option.
    tea_menu_choice = input("Please enter your choice 1-6: ")
    
    if tea_menu_choice.isnumeric():
    
        tea_menu_choice_convert = int(tea_menu_choice)
        
        if tea_menu_choice_convert > 0 and tea_menu_choice_convert < 7:
        
            if tea_menu_choice_convert == 1:
                print("Here is your REGULAR tea. Enjoy. :) ")
                Main_Menu()
            elif tea_menu_choice_convert == 2:
                print("Here is your DECAFF tea. Enjoy. :) ")
                Main_Menu()
            elif tea_menu_choice_convert == 3:
                print("Here is your MINT tea. Enjoy. :) ")
                Main_Menu()
            elif tea_menu_choice_convert == 4:
                print("Here is your GINGER AND LEMON tea. Enjoy. :) ")
                Main_Menu()
            elif tea_menu_choice_convert == 5:
                print("Here is your ICED tea. Enjoy. :) ")
                Main_Menu()
            elif tea_menu_choice_convert == 6:
                print("You want to go back to the MAIN MENU? OK.")
                Main_Menu()
        
        else:
            Tea_Menu()
    
    else:
        Tea_Menu()
    

#   This is the coffee menu.
def Coffee_Menu():

    print("You have entered option #2: Coffee.")
    
    print("Here is your choice of coffee.")
    
    print("")
    
    print("1. Regular")
    print("2. Decaff")
    print("3. Late")
    print("4. Americano")
    print("5. Cortado")
    print("6. Espresso")
    print("7. Cappacino")
    print("8. Iced")
    print("9. Main menu")
    
    print("")
    
    #   The user gives their option
    coffee_menu_choice = input("Please enter your choice 1-8: ")
    
    if coffee_menu_choice.isnumeric():
    
        coffee_menu_choice_convert = int(coffee_menu_choice)
        
        if coffee_menu_choice_convert > 0 and coffee_menu_choice_convert < 10:
        
            if coffee_menu_choice_convert == 1:
                print("Here is your REGULAR coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 2:
                print("Here is your DECAFF coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 3:
                print("Here is your LATE coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 4:
                print("Here is your AMERICANO coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 5:
                print("Here is your CORTADO coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 6:
                print("Here is your ESPRESSO coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 7:
                print("Here is your CAPPACINO coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 8:
                print("Here is your ICED coffee. Enjoy. :) ")
                Main_Menu()
            elif coffee_menu_choice_convert == 9:
                print("You want to go back to the MAIN MENU? OK. ")
                Main_Menu()
        else:
            Coffee_Menu()
    
    else:
       Coffee_Menu()


#   This is the specials menu.
def Specials_Menu():
    
    print("You have selected option #4: Specials.")
    print("Here is our special menu.")
    
    print("")
    
    print("1. Hot Chocolate")
    print("2. Chili chocolate")
    print("3. Frothy milk")
    print("4. Water and lemon")
    print("5. Main menu")
    
    print("")
    
    #   The user gives their option.
    specials_menu_choice = input("Please enter your choice 1-5: ")
    
    if specials_menu_choice.isnumeric():
    
        specials_menu_choice_convert = int(specials_menu_choice)
        
        if specials_menu_choice_convert > 0 and specials_menu_choice_convert < 6:
        
            if specials_menu_choice_convert == 1:
                print("Here is your HOT CHOCOLATE special. Enjoy. :) ")
                Main_Menu()
            elif specials_menu_choice_convert == 2:
                print("Here is your CHILI CHOCOLATE special. Enjoy. :) ")
                Main_Menu()
            elif specials_menu_choice_convert == 3:
                print("Here is your FROTHY MILK special. Enjoy. :) ")
                Main_Menu()
            elif specials_menu_choice_convert == 4:
                print("Here is your WATER AND LEMON special. Enjoy. :) ")
                Main_Menu()
            elif specials_menu_choice_convert == 5:
                print("You want to go back to the MAIN MENU? OK. ")
                Main_Menu()
        else:
        
            Specials_Menu()
    
    else:
        Specials_Menu()

#   This is goodbye.
def Goodbye():
    
    print("You have selected option #5: Goodbye.")
    
    print("")
    
    print("Goodbye.")

#	The main function.
def game_start():
	Main_Menu()

#	The main function.
game_start()
