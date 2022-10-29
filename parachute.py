from pyparsing import line


class parachute():

    """responsibility:
    display lines in a form of parachute that represent the number of guesses
 behaviors:
    -display parachute
    -remove line
 state:
    -number of guesses
---------------------------------------
    (attributes)
    number_guesses
    validation

    (methods)
    _init_(self)
    display_parachutes()
    evaluate_guess()
    """

    def _init_(self):

        self.number_guesses = 5
        self.validation = True

    def display_paracute(self):

        grid = [
            "   _   ",
            " /   \ ",
            "   _   ",
            " \   / ",
            "  \ /  ",
            "   o   ",
            "  /|\  ",
            "  / \  "]

        for i in grid:
            print(i)

        validation = self.validation()
        while validation:
            user_choice = input("y or n ?")
            if user_choice == "y":
                for i in grid:
                    print(i)

            elif user_choice == "n":
                validation == False
                grid.pop(0)

                for i in grid:
                    print(i)
