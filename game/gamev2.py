# Every element of array represents string with blanks. They're gonna be used to
# figure what exactly we should ask user later

question = [("If you multiply 2 by 2 correct answer is going to be: __1__ ."
             "If you then multiply it by 3 it became __2__ . And if you add 9"
             "it'll became __3__ . Final question: divide it by 7 __4__ "),
            ("If you multiply 2 by 3 correct answer is going to be: __1__ ."
             "If you then multiply it by 3 it became __2__ . And if you add 9"
             "it'll became __3__ . Final question: divide it by 3 __4__"),
            ("If you multiply 2 by 4 correct answer is going to be: __1__ ."
             "If you then multiply it by 3 it became __2__ . And if you add 9"
             "it'll became __3__ . Final question: divide it by 11 __4__")]

# List with all answers that user have to type
answers = [['4', '12', '21', '3'], ['6', '18', '27', '9'],
           ['8', '24', '33', '3']]

# Array to search where blanks in questions are
list_of_blanks = ['__1__', '__2__', '__3__', '__4__']


# Function to ask user about level of dificulty
def level_of_dif():
    level = raw_input(
        "How dificult is this quiz supposed to be? \n 1. Super ease \n"
        " 2. Harder \n 3. Very hard \n")
    if level == '1':
        return question[0], answers[0]
    elif level == '2':
        return question[1], answers[1]
    elif level == '3':
        return question[2], answers[2]
    else:
        print 'Sorry, but you can only choose between 1 to 3 here. Please use \
        numbers only'
        return level_of_dif()


# Assign question and correct answers based on level of dificulty
question, answers = level_of_dif()


# Looking for blanks in list_of_blanks
def task_in_lob(blanks, lob):
    for element in lob:
        if element in blanks:
            return element
    return None


# Function that runs game
def play_game(question_string, lob):
    """Function which runs game.
    question_string is a string with blanks.
    lob represents list with blanks to search through string"""
    questionNumber = 0 # To know exactly what we asking
    minAmountOfLives = 0 # When users is losing in game. Basically minimum amount of lives
    tries = 3     # How many tries user have before we realise he is not good enough
    replaced = []
    print "Here is the question: ", question, "Please feel the blanks"
    question_string = question_string.split()
    for word in question_string:
        replacement = task_in_lob(word, lob)
        if replacement != None:
            word = word.replace(replacement, raw_input(' '.join(replaced)))
            if word == answers[questionNumber]:
                replaced.append(word)
            else:
                tries -= 1
                if tries <= minAmountOfLives:
                    print 'Game over!'
                else:
                    print "Try again"
                    word = word.replace(replacement, raw_input(' '.join(replaced)))
        else:
            replaced.append(word)

# Function to check if user answered right or wrong. Returns True or False
def check_answer(user_input, correct_answers, question_number):
    """This function accepts user_input from play_game, correctAnswers are list
    from global variable and questionNumber from play_game"""
    if user_input == correct_answers[question_number]:
        print "That's Correct! \n"
        return True
    else:
        print "You entered ", user_input, "Correct answer should be ", correct_answers[question_number]
        return False


# Start game here
play_game(question, list_of_blanks)
