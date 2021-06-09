"""
Italian Present Tense Verb Conjugator

This program conjugates a given Italian verb in its infinite form into the various present tense forms. 
It also loads a csv that contains a list of some commonly used irregular verbs and their present tense forms.
It is fairly simplistic right now with a lot of room for improvement. 
I hope to continually improve it as I learn more Italian and Python.

Possible future directions:
* GUI using Tkinter and Tkinter-Designer
* Translation/dictionary (IT-EN, or EN-IT)
* Sentence handling
"""

import os
import csv

# ask user input for regular verb in infinite form
# program scan to see if it is in csv of irregular verbs. if so, take conjugations from there. 
# else
# program reads last three letters of input (are/ere/ire)
# program prints 1st - 3rd singular , 1st - 3rd plural options
# if there's already an i in the root end don't put another in 2nd singular and 1st plural


def main():
    
    """
    User is asked to input an Italian verb in its inifinite form.
    Program checks if the inputted verb is irregular or regular, and outputs corresponding present tense conjugations accordingly.
    User is then given the option to continue to conjugate another verb or to end the program.  
    """

    while True:
        user_verb = input("Please input a verb in its infinite form: ")

        if check_if_irregular(user_verb) == True:
            pass
        else:
            user_verb_class = get_verb_class(user_verb)
            user_verb_root = get_verb_root(user_verb)
            user_verb_conjugation = regular_conjugation(user_verb_class, user_verb_root, user_verb)
        
        check_again = input("If you would like to conjugate another verb, please type 'new verb'. Otherwise, type 'all done': ")

        if check_again == "new verb":
            print('\nVa bene! \n') # okay!
            continue
        elif check_again == "all done":
            print('\nArrivederci! \n') # see you!
            break

def check_if_irregular(user_verb):
    """
    Checks if the inputted verb is irregular by loading and checking against a given csv of commonly used irregular verbs.
    If it is an irregular verb, the conjugations accrording to the csv will be printed out.
    If it is not an irregular verb, it will return to the loop in main().
    """

    with open('italian_irregular_verbs.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        for row in csvreader:
            irregular_verb = row['verb']
            first_singular_irreg = row['1st_sing']
            second_singular_irreg = row['2nd_sing']
            third_singular_irreg = row['3rd_sing']
            first_plural_irreg = row['1st_pl']
            second_plural_irreg = row['2nd_pl']
            third_plural_irreg = row['3rd_pl']

            if user_verb == irregular_verb:
                print(f"""
            
                {user_verb} is an irregular verb!
                
                1st singular I / io: {first_singular_irreg}

                2nd singular you / tu: {second_singular_irreg}

                3rd singular he/she lui/lei: {third_singular_irreg}

                1st plural we / noi: {first_plural_irreg}

                2nd plural you / voi: {second_plural_irreg}

                3rd plural they / loro: {third_plural_irreg}
                """)
                
                return True



def get_verb_class(regular_verb):
    """
    Get the regular verb class (-are, -ire, or -ere) via indexing of the inputted verb
    """

    verb_class = regular_verb[-3:]

    return verb_class

def get_verb_root(regular_verb):
    """
    Get the regular verb root/stem via indexing of the inputted verb
    """
    
    verb_root = regular_verb[:-3]

    return verb_root

def regular_conjugation(verb_class, verb_root, regular_verb):
    """
    Conjugate the regular verb based on verb roots and verb classes
    Includes case of roots that end in 'i' (e.g., mangiare) where the 'i' should be omitted in 2nd singular and 1st plural present tense conjugation
    """
    
    if verb_root[-1] == 'i' and verb_class == 'are':
        print(f"""
        
        {regular_verb} is a regular verb!

        1st singular I / io: {verb_root}o

        2nd singular you / tu: {verb_root}
        
        3rd singular he/she lui/lei: {verb_root}a

        1st plural we / noi: {verb_root}amo

        2nd plural you / voi: {verb_root}ate 

        3rd plural they / loro: {verb_root}ano
        """)
    elif verb_root[-1] == 'i' and verb_class == 'ere':
        print(f"""
        
        {regular_verb} is a regular verb!

        1st singular I / io: {verb_root}o

        2nd singular you / tu: {verb_root}
        
        3rd singular he/she lui/lei: {verb_root}e

        1st plural we / noi: {verb_root}amo

        2nd plural you / voi: {verb_root}ete 

        3rd plural they / loro: {verb_root}ono
        """)
    elif verb_root[-1] == 'i' and verb_class == 'ire':
        print(f"""
        
        {regular_verb} is a regular verb!

        1st singular I / io: {verb_root}o

        2nd singular you / tu: {verb_root}
        
        3rd singular he/she lui/lei: {verb_root}e

        1st plural we / noi: {verb_root}amo

        2nd plural you / voi: {verb_root}te 

        3rd plural they / loro: {verb_root}ono
        """)
    elif verb_class == 'are':
        print(f"""
        
        {regular_verb} is a regular verb!

        1st singular I / io: {verb_root}o

        2nd singular you / tu: {verb_root}i
        
        3rd singular he/she lui/lei: {verb_root}a

        1st plural we / noi: {verb_root}iamo

        2nd plural you / voi: {verb_root}ate 

        3rd plural they / loro: {verb_root}ano
        """)
    elif verb_class == 'ere':
        print(f"""
        
        {regular_verb} is a regular verb!

        1st singular I / io: {verb_root}o

        2nd singular you / tu: {verb_root}i
        
        3rd singular he/she lui/lei: {verb_root}e

        1st plural we / noi: {verb_root}iamo

        2nd plural you / voi: {verb_root}ete 

        3rd plural they / loro: {verb_root}ono
        """)
    elif verb_class == 'ire':
        print(f"""
        
        {regular_verb} is a regular verb!

        1st singular I / io: {verb_root}o

        2nd singular you / tu: {verb_root}i
        
        3rd singular he/she lui/lei: {verb_root}e

        1st plural we / noi: {verb_root}iamo

        2nd plural you / voi: {verb_root}ite 

        3rd plural they / loro: {verb_root}ono
        """)

if __name__ == '__main__':
    main()
