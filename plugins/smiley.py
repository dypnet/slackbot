import time
import numpy
crontable = []
outputs = []
smilies = []

def process_message(data):
#    if "C0K2UNFB2" in data['channel']:
    text = data['text']
    channel = data['channel']
     
    if '.reload' in text or '.smile' in text or '..' in text:
        if '.reload' in text: 
            reload()
            print('smileFile has been reloaded')
    
        elif ('.smile' in text or '..' in text) and not '...' in text:
            randomNumber = numpy.random.random_integers(len(smilies)-1)
            print('Sending smile {} to {}'.format(smilies[randomNumber],channel))
            outputs.append([channel,"{}".format(smilies[randomNumber])])

def reload():
   del smilies[:]
   smileFile = open('plugins/smileFile','r')
   for smile in smileFile:
       smilies.append(smile.strip())
   smileFile.close()

reload()
