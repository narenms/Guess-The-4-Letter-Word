import sys
import stringDatabase
from game import Game1


class Guess1:
    """
    The Guess represents the game itself(including the menu)
    This is the class which is called first to start the game.
    It has functions/methods which processes the choice/option of the player and
    communicate with other classes to get input, to calculate score, etc,.
    """

    def guess_word(ga, word, ch):
        """
        This is the key method/function which takes a choice input by the player
        and processes it in 4 different options depending on the input g = guess,
        t = tell me, l for a letter, and  q to quit.
        Option 1: Process it as user is guessing a letter.
        Option 2: Process it as user is guessing the word.
        option 3: User is Giving Up the current game.
        Option 4: Player is quitting the game. When the player quits the game,
        information of all the games is presented to the player.
        While the option/choice is not 'q'(i.e., quit) the player continues playing
        the guessing game until he opts to quit
        :param word: It is the current game random word which is to be guessed by the player.
        :param ch: It is the choice input by the player.
        :return: flag. Which is used to end the current game once the word is guessed and
                       start a new game by generating a new random game word.
        """
        flag = 0
        sd = stringDatabase
        gameword = list(word)
        gamewordlen = len(gameword)

        # Checks if the option/choice is 'l'
        if ch == 'l':
            gl = sd.StringDatabase.get_letter()
            if not gl:
                return
            # print('here')
            if gl in gameword:
                if gl in ga.guess_list:
                    print('Already flipped the letter, Guess another letter')
                    return
                n = gameword.count(gl)
                print('You found', n, 'letter/s')
                for i in range(gamewordlen):
                    if gameword[i] == gl:
                        ga.guess_list[i] = gl
                if ga.guess_list == gameword:
                    flag = 1
                    ga.status = 'Success'
                    print('Correct Guess!!')
                ga.calculate_score()
            else:
                print('You found 0 new letter/s, Try Again')
                ga.missed_letter += 1
                if ga.score == 0:
                    ga.score -= 1
                else:
                    ga.score -= (ga.score/4)
                    per = (ga.score*10)/100
                    ga.score -= per

        # Checks if the option/choice is 'g'
        if ch == 'g':
            gl = list(sd.StringDatabase.get_word())
            # print('\n')
            if gl == gameword:
                count = 0
                for i in range(gamewordlen):
                    if gameword[i] != ga.guess_list:
                        count += 1
                if count >= 1:
                    ga.calculate_score()
                ga.score += 10
                ga.status = 'Success'
                print('Correct guess!!')
                flag = 1
            else:
                ga.bad_guess += 1
                print('Wrong guess, Try Again')
                per = (ga.score * 30) / 100
                ga.score -= per

        # Checks if the option/choice is 't'
        if ch == 't':
            ga.score = ga.score/2
            ga.calculate_minus_score()
            ga.status = 'Gave up'
            print('Correct word is: ' + word)
            flag = 1

        return flag

    if __name__ == '__main__':

        """ Creating a object of type stringDatabase """
        sd = stringDatabase

        print("** The great guessing game **")

        # This calls the function generate_list()
        sd.StringDatabase.generate_list()

        #
        list = sd.StringDatabase.get_list()
        game_no = 1
        ga = Game1(list, game_no)
        word = ga.get_word()

        # print(word)
        print('Current guess: ', end='')
        for a in ga.guess_list:
            print(a, end='')

        while True:
            ch = sd.StringDatabase.get_choice()
            if ch:
                break

        """
        While the option/choice is not 'q'(i.e., quit) the player continues playing 
        the guessing game until he opts to quit
        """
        while ch != 'q':

            flag = guess_word(ga, word, ch)

            if flag == 1:
                ga.add_data()
                game_no += 1
                ga = Game1(list, game_no)
                word = ga.get_word()
                flag = 0
                print('\n-----NEW GAME-----\n')

            # print(word)
            print('Current guess: ', end='')
            for a in ga.guess_list:
                print(a, end='')

            while True:
                ch = sd.StringDatabase.get_choice()
                if ch:
                    break

        # pydoc sys

        """
        When the player quits the game, information of all the games is presented to the player. 
        """
        if ch == 'q':
            print('\nYou have quit the game\n')
            sd.StringDatabase.print_game_data()

            sys.exit()
