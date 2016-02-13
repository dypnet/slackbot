import time
import numpy
crontable = []
outputs = []
gifs = []
random = []

def process_message(data):

    text = data['text']
    channel = data['channel']

    if '.gif' in text:
        text = text[5:]
        print(text)
        if 'reload' in text:
            reload()
            print('smileFile has been reloaded')

        elif 'list' in text:
            outputText = gifs[0][0]
            for gif in gifs[1:]:
                outputText += ', '+gif[0]
            outputs.append([channel,"{}".format(outputText)])

        elif 'random' in text:
            randomNumber = numpy.random.random_integers(len(random)-1)
            print('Sending random gif number {}'.format(randomNumber))
            outputs.append([channel,"{}".format(random[randomNumber])])

        else:
            for gif in gifs:
                if gif[0] == text:
                    print('Sending gif {} to {}'.format(gif[0],channel))
                    outputs.append([channel,"{}".format(gif[1])])



def reload():

   del gifs[:]
   gifFile = open('plugins/reactionGifFile','r')
   gifRandFile = open('plugins/randomGifFile','r')

   for gif,rand in zip(gifFile,gifRandFile):
       gifs.append(gif.strip().split(','))
       random.append(rand.strip())
   gifFile.close()

reload()
