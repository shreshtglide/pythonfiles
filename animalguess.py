def animal_guess_game():
    print("Welcome to the Animal Guessing Game!")
    print("Think of an animal (whale or dog) and answer the following questions with yes or no.")

    question1 = input("Does it live in the water? ")
    question2 = input("Is it a mammal? ")
    question3 = input("Is it known for its size? ")
    question4 = input("Is it commonly kept as a pet? ")

    if question1.lower() == "yes" and question2.lower() == "yes" and question3.lower() == "yes" and question4.lower() == "no":
        print("You're thinking of a whale!")
    elif question1.lower() == "no" and question2.lower() == "yes" and question3.lower() == "no" and question4.lower() == "yes":
        print("You're thinking of a dog!")
    else:
        print("Sorry, I couldn't guess the animal.")

animal_guess_game()