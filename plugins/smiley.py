import time
import numpy
crontable = []
outputs = []
smilies = []

smileFile = open('plugins/smileFile','r')
for smile in smileFile:
    smilies.append(smile.strip())
smileFile.close()

def process_message(data):
    if "C0K2UNFB2" in data['channel']:

        if '.reload' in data['text']:
            smileFile = open('plugins/smileFile','r')
            for smile in smileFile:
                smilies.append(smile.strip())
            smileFile.close()
            print('smileFile has been reloaded')

        elif '.smile' in data['text']:
            randomNumber = numpy.random.random_integers(len(smilies)-1)
            print('Sending smile number {i}'.format(randomNumber))
            outputs.append([data['channel'],\
                    "{}".format(smilies[randomNumber])])



