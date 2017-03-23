# Lesson 3.2: Use Functions
# Mini-Project: Secret Message
import os
# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
#get file names and store them in a list
def get_file_names():
    list_of_files = os.listdir(
        "/Users/virtim/Documents/udct/ipnd-starter-code-master/ipnd-starter-code-master/stage_3/lesson_3.2_using_functions/secret_message/prank"
    )
    return list_of_files

saved_path = os.chdir(
"/Users/virtim/Documents/udct/ipnd-starter-code-master/ipnd-starter-code-master/stage_3/lesson_3.2_using_functions/secret_message/prank"
)
list_of_files = get_file_names()

def rename_files(saved_path):
    print "\n \n \n \n Current folder: "
    for file_name in list_of_files:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print os.listdir(saved_path)
    #QTA Why chdir at the end, not before?
    os.chdir("/Users/")

rename_files(saved_path)
