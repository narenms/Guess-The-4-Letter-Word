import random


class Game1:
    """
    The class Game maintains information about a specific game which includes Game number, Current game word,
    game status, number of bad guesses, number of missed letters, score and a final data structure which stores the
    information about all the games.
    :param game_data: Class variable which maintains the information of current specific game
    :param final_score: Class variable which stores the final score of all the games played
    :param calculate_table: Stores the frequency values of all the English alphabets
    """

    # Static variables
    game_data = []
    final_score = 0
    calculate_table = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25,
                       'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09,
                       'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03,
                       'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93,
                       'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
                       'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
                       'y': 1.97, 'z': 0.07}

    def __init__(self, wordList, game_no):
        """

        :param wordList: Contains the list of 4-letter words
        :param game_no: Game number
        :param game_no: Instance variable which stores game number
        :param word: Instance variable which stores the current game word
        :param status: Instance variable which stores the game status
        :param bad_guess: Instance variable which stores number of bad guess of word
        :param missed_letter: Instance variable which stores number of missed/bad guess of letter/s
        :param score: Instance variable which stores the score of current specific game
        :param guess_list: Instance variable which stores the guessed letter
        """
        self.game_no = game_no
        self.word = random.choice(wordList)
        self.status = ''
        self.bad_guess = 0
        self.missed_letter = 0
        self.score = 0
        self.guess_list = ['-'] * 4

    def get_word(self):
        """
        Simple function which returns the current game word
        :return: Return current game word
        """
        return self.word

    def calculate_score(self):
        """
        Calculates the score of the current game when correctly guessed and updates the game score
        :return:
        """
        for i in range(len(self.word)):
            if self.word[i] != self.guess_list[i]:
                if self.guess_list[i] == '-':
                    self.score += Game1.get_calc_score(self.word[i])

    def calculate_minus_score(self):
        """
        Calculates the score of the current game when wrongly guesses and updates the game score
        :return:
        """
        for i in range(len(self.word)):
            if self.word[i] != self.guess_list[i]:
                if self.guess_list[i] == '-':
                    self.score -= Game1.get_calc_score(self.word[i])

    def add_data(self):
        """
        Adds all the current game information and store it in a python data structure
        :return:
        """
        data = []
        data.append(self.game_no)
        data.append(self.word)
        data.append(self.status)
        data.append(self.bad_guess)
        data.append(self.missed_letter)
        data.append(round(self.score, 2))
        Game1.game_data.append(data)

    def get_calc_score(char):
        """
        Simply function which returns the frequency value of an alphabet
        :return: Returns frequency value of an alphabet
        """
        return Game1.calculate_table.get(char)
