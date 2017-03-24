# Every element of array represents string with blanks. They're gonna be used to
# figure what exactly we should ask user later

question = [("If you multiply 2 by 2 correct answer is going to be: __1__. "
             "If you then multiply it by 3 it'll be: __2__. And if you add 9 "
             "it'll be: __3__. Final question: divide it by 7: __4__."),
            ("If you multiply 2 by 3 correct answer is going to be: __1__. "
             "If you then multiply it by 3 it became __2__. And if you add 9 "
             "it'll became __3__. Final question: divide it by 3 __4__."),
            ("If you multiply 2 by 4 correct answer is going to be: __1__. "
             "If you then multiply it by 3 it became __2__. And if you add 9 "
             "it'll became __3__. Final question: divide it by 11 __4__")]

# List with all answers that user have to type
answers = [['4', '12', '21', '3'], ['6', '18', '27', '9'],
           ['8', '24', '33', '3']]

# Array to search where blanks in questions are
list_of_blanks = ['__1__', '__2__', '__3__', '__4__']

# When users is losing in game. Basically minimum amount of lives
minAmountOfLives = 0

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
    """Question_string - string with blanks.
    lob - list with blanks to search through string with blanks"""
    questionNumber = 0 # To know exactly what we asking
    tries = 3 # How many tries user have before we realise he is not good enough
    noneTypeErrorHandling = 0 # Number to use instead of returning NoneType
    replaced = []
    print "Here is the question: ", question, "Please feel the blanks"
    question_string = question_string.split()
    for word in question_string:
        replacement = task_in_lob(word, lob)
        if replacement != None and tries >= minAmountOfLives:
            replaceWithThis, questionNumber, tries = check_answer(replaced, questionNumber, tries)
            if replaceWithThis != noneTypeErrorHandling and questionNumber != noneTypeErrorHandling and tries != noneTypeErrorHandling:
                word = word.replace(replacement, replaceWithThis)
                replaced.append(word)
            else:
                return "Game over"
        else:
            replaced.append(word)
    return "You win"

# Function to check if user answered right or wrong. Returns True or False
def check_answer(current_array, questionNumber, triesleft):
    """
    current_array - taking continuos result of play_game to print before asking
    questionNumber - taking index of array with answers to verify user input
    triesleft - taking amount of tries user have before he lose in game
    """
    tries = triesleft
    answerindex = questionNumber
    user_input = raw_input(' '.join(current_array))
    handlingError = 0 # To handle NoneType error and avoid magic number
    if user_input ==  answers[questionNumber]:
        print "That's correct!"
        answerindex += 1
        return user_input, answerindex, tries
    elif tries > minAmountOfLives:
        tries -= 1
        print "Try again. You have ", tries, 'tries left'
        return check_answer(current_array, questionNumber, tries)
    else:
        return handlingError, handlingError, handlingError

# Start game here
print play_game(question, list_of_blanks)
