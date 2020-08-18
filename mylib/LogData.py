import sys
import datetime
from mylib.TesseractPython import tesseract_class
from textblob import TextBlob

# class to log output data
class logger_class(object):

    def save_log(filename):
        orig_stdout = sys.stdout
        ## NOTE: a+ is append which auto opens text file and continues the output; w+ is auto re-write
        f = open('data/Log.txt', 'a+')
        sys.stdout = f
        ##To autowrite file
        #f.write(str(filename))
        ##To append file along with date and time (doesn't auto write)
        f.write(str('\n' + filename + '\n' + '\n' + 'Logged at' + " " + str(datetime.datetime.now())))
        sys.stdout = orig_stdout
        f.close()

    def save_log_trans(filename):
        orig_stdout = sys.stdout
        f = open('data/Log.txt', 'a+')
        sys.stdout = f
        final = ' '.join(filename)
        f.write(str('\n' + '\n' + final + '\n' + '\n' + 'Logged at' + " " + str(datetime.datetime.now())))
        sys.stdout = orig_stdout
        f.close()
