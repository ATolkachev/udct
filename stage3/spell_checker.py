import urllib

def read_text():
    quotes = open("/Users/virtim/Documents/udct/stage3/curse_text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen(
                "http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print "Alarm!"
    elif "false" in output:
        print "All good"
    else:
         "Error!" 
    print (output)
    connection.close()

read_text()
