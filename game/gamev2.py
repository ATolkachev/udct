#Correct answer to verify if user is not dumb
final_answer = "If you multiply 2 by 2 correct answer is going to be: 4. If you then multiply it by 3 it became 12. And if you add 9 it'll became 21."

#questions
question1 = 'If you multiply 2 by 2 correct answer is going to be: __1__.'
question2 = 'If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__.'
question3 = "If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__. And if you add 9 it'll became __3__."

#list with all answers that user have to type
answers = ['4', '12', '21']

#how many tries user have before we realise he is not good enough
tries = 5

#Array to search through question
list_of_blanks = ['__1__', '__2__', '__3__']


#function to ask user about level of dificulty
def level_of_dif():
    level = raw_input(
        "How dificult is this quiz supposed to be? \n 1. Super ease \n 2. Harder \n 3. Very hard \n"
    )
    if level == '1':
        return question1, answers[0].split()
    elif level == '2':
        return question2, answers[:2]
    elif level == '3':
        return question3, answers
    else:
        print 'Sorry, but you can only choose between 1 to 3 here. PLease use numbers only'
        return level_of_dif()


#assign question and correct answers based on level of dificulty
question, answers = level_of_dif()


# Looking for blanks in list_of_blanks
def task_in_lob(blanks, lob):
    for element in lob:
        if element in blanks:
            return element
    return None


#Game
def play_game(question_string, lob):
    global tries
    replaced = []
    exact_questions = [
        'What the answer for the first blank? ',
        'What the answer for the second blank? ',
        'What the answer for the third blank? '
    ]
    exact_questions_index = 0
    print "Here is the question: ", question, "Please feel the blanks"
    question_string = question_string.split()
    for word in question_string:
        replacement = task_in_lob(word, lob)
        if replacement != None:
            word = word.replace(
                replacement, raw_input(exact_questions[exact_questions_index]))
            replaced.append(word)
            exact_questions_index += 1
        else:
            replaced.append(word)
    replaced = ' '.join(replaced)
    if replaced in final_answer:
        print "You win!"
    elif tries > 0:
        tries -= 1
        print "You made a mistake. Try to use calculator. You have only tries", tries, "left"
        question_string = ' '.join(question_string)
        play_game(question_string, lob)
    else:
        print "Too many mistakes. Goodbye"

#start game here
play_game(question, list_of_blanks)
