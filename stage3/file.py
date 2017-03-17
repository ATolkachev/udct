import time
import webbrowser

breaknumber = 0

print 'this program started at ' + time.ctime()

while breaknumber < 3:
    time.sleep(10)
    webbrowser.open('google.com')
    breaknumber += 1
