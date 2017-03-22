#How can you store your data (your questions) to reduce redundancy?
# make a list of strings and use indexes. level 1 use question[0], level 3 use question[0..2]
# question = ['If you multiply 2 by 2 correct answer is going to be: __1__.', 'If you then multiply it by 3 it became __2__.', 'And if you add 9 it'll became __3__.']

#questions
question1 = 'If you multiply 2 by 2 correct answer is going to be: __1__.'
question2 = 'If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__.'
question3 = "If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__. And if you add 9 it'll became __3__."

#list with answers
answers = ['4', '12', '21']

#Array to search through question
list_of_questions = ['__1__', '__2__', '__3__']

#variable with level
level = 0

#empty variable with final answer
final_answer = []


# Select a level
#Why it's not working with the first try and doesn't return errors from else? --fixed
#Try and Except statements are unnecessary here. -- fixed with accepting string and comparing input with strings
def level_of_dif():
    level = raw_input(
        "How dificult is this quiz supposed to be? \n 1. Super ease \n 2. Harder \n 3. Very hard \n"
    )
    if level == '1' or level == '2' or level == '3':
        return level
    else:
        print 'Sorry, but you can only choose between 1 to 3 here. PLease use numbers only'
        return level_of_dif()


#looking for task in list_of_questions


def task_in_loq(task, loq):
    for element in loq:
        if element in task:
            return element
    return None


#Returns string based on level of dificulty
def assign_lod_to_quest(lod):
    if level_of_dif() == 1:
        return question1
    elif level_of_dif() == 2:
        return question2
    else:
        return question3


def check_answers(level):
    answer_index = 0
    print "Current answer_index is ", answer_index
    while answer_index < level:
        if answer_index < len(answers):
            print "Answer index is: ", answer_index, "Which is <= ", level
            user_input = raw_input("Type in an answer: ")
            if user_input == answers[answer_index]:
                answer_index += 1
                print "new answer index is: ", answer_index
                print 'Correct!'
            else:
                print 'Try to use calculator and type an answer again: '
                check_answers(level)
    return "All answers are correct!"


def play_game(question_string, loq):
    replaced = []
    question_string = question_string.split()
    for word in question_string:
        replacement = task_in_loq(word, loq)
        if replacement != None:
            word = word.replace(replacement, check_answers(level_of_dif))
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = ' '.join(replaced)
    return replaced


#print check_answers(level_of_dif())
#print play_game(assign_lod_to_quest(level_of_dif), list_of_questions)
