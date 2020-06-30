from game import Game1


class StringDatabase:

    """
    The class StringDatabase is responsible of all I/O operations and maintains the 4-letter words database.
    This class also has simple methods/functions which takes input from the player and returns it to the calling function.
    :param wordlist: Class variable which stores the list of 4-letter words
    """
    wordlist = []
    # final_data = []

    def generate_list():
        """
        Simple funtion which extracts 4-letter words from a .txt file and stores in a class variable wordlist
        :return:
        """
        f = open('four_letters.txt', 'r')
        # f = open('test.txt', 'r')
        StringDatabase.wordlist = f.read().split()

    def get_list():
        """
        Simply function which returns the list of 4-letter words
        :return: Returns wordlist. A list of 4-letter words.
        """
        return StringDatabase.wordlist

    def get_choice():
        """
        A function to get option/choice input from the player and return to the calling function.
        Info: If the player enters a capital letter(upper-case), it is converted to lower-case and processed.
        :return: Returns ch. Option/choice opted by the player.
        """
        ch = input('\ng = guess, t = tell me, l for a letter, and  q to quit\n')
        if ch.isupper():
            ch = ch.lower()
        if ch not in ['g', 'l', 't', 'q']:
            print('Invalid input')
            return None
        return ch

    def get_letter():
        """
        A function to let player guess a letter in the game and return it to the calling function.
        Info: If the player enters a capital letter(upper-case), it is converted to lower-case and processed.
        :return: Returns letter. Letter guessed by the player
        """
        letter = input('Enter a letter\n')
        if letter.isupper():
            letter = letter.lower()
        if len(letter) != 1:
            print('Invalid')
            return None
        return letter

    def get_word():
        """
        A function to let player guess a word in the game and return it to the calling function.
        Info: If the player enters an upper-case word, it is converted to lower-case and processed.
        :return: Returns word. Word guessed by the player
        """
        word = input('Guess the four letter word\n')
        if word.isupper():
            word = word.lower()
        return word

    def print_game_data():
        """
        A function which prints the information of all the games played when opted to 'quit' the game.
        :return:
        """
        print("{:8s} {:8s} {:11s} {:15s} {:18s} {:9s}".format('Game', 'Word', ' Status', 'Bad Guesses',
                                                               'Missed Letters', 'Score'))
        print("{:8s} {:8s} {:11s} {:15s} {:18s} {:9s}".format('-'*4, '-'*4, '-'*8, '-'*11, '-'*14, '-'*5))

        for data in Game1.game_data:
            print("{:8s} {:8s} {:11s} {:15s} {:18s} {:9s}".format(str(data[0]), data[1], data[2], str(data[3]),
                                                                   str(data[4]), str(data[5])))
            Game1.final_score += data[-1]

        print('Final Score: ', round(Game1.final_score, 2))
