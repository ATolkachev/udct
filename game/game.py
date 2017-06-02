#!/bin/python

#How can you store your data (your questions) to reduce redundancy?
# make a list of strings and use indexes. level 1 use question[0], level 3 use question[0..2]
final_answer = "If you multiply 2 by 2 correct answer is going to be: 4. If you then multiply it by 3 it became 12. And if you add 9 it'll became 21. And if you add 1 it'll became 22."

#questions
question1 = 'If you multiply 2 by 2 correct answer is going to be: __1__.'
question2 = 'If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__.'
question3 = "If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__. And if you add 9 it'll became __3__."
question4 = "If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__. And if you add 9 it'll became __3__. And if you add 1 it'll became __4__."

questions = ["If you multiply 2 by 2 correct answer is going to be: __1__.","If you then multiply it by 3 it became __2__.","And if you add 9 it'll became __3__.","And if you add 1 it'll became __4__."]

#list with answers
answers = [4, 12, 21, 22]

#how many tries user have before we realise he is not good enough
tries = 6

#Array to search through question
list_of_blanks = ['__1__', '__2__', '__3__','__4__']  #Find list_of_blanks

# docstrings <----
# Select a level
# Why it's not working with the first try and doesn't return errors from else? --fixed
# Try and Except statements are unnecessary here. -- fixed with accepting string and comparing input with strings
def level_of_dif():
    level = eval(raw_input(
        "How dificult is this quiz supposed to be? \n 1. Super ease \n 2. Harder \n 3. Very hard \n 4. Hardcore \n"
    ))
    if level <= 4:
        return questions[:level], answers[:level]
    else:
        print 'Sorry, but you can only choose between 1 to 4 here. PLease use numbers only'
        return level_of_dif()


question, answers = level_of_dif()

# Looking for blanks in list_of_blanks
def task_in_lob(blanks, lob):
    for element in lob:
        if element in blanks:
            return element
    return None


def play_game(question_string, lob):
    global tries
    replaced = []
    exact_questions = [
        'What the answer for the first blank? ',
        'What the answer for the second blank? ',
        'What the answer for the third blank? ',
        'What the answer for the fourth blank? '
    ]
    exact_questions_index = 0
    print "Here is the question: ", question, "Please feel the blanks"
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
        print "You won!"
    elif tries > 0:
        tries -= 1
        print "You made a mistake. Try to use calculator. You have only tries", tries, "left"
        play_game(question_string, lob)
    else:
        print "Too many mistakes. Goodbye"


play_game(question, list_of_blanks)
