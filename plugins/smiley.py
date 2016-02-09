import time
import numpy
crontable = []
outputs = []
smilies = []
first = True

def process_message(data):
    print(data['channel'])
    if "C0K2UNFB2" in data['channel']:

        if ('.reload' in data['text']) and first:
            reload_file()
            first = False

        elif '.smile' in data['text']:
            randomNumber = numpy.random.random_integers(len(smilies)-1)
            print('Sending smile number {}'.format(randomNumber))
            outputs.append([data['channel'],\
                    "{}".format(smilies[randomNumber])])


def reload_file():
    smilies = []
    smileFile = open('smileFile','r')
    for smile in smileFile:
        smilies.append(smile.strip())
    smileFile.close()
    print('smileFile has been reloaded')

