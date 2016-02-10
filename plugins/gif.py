import time
import numpy
crontable = []
outputs = []
gifs = []
channel = 'C0L0FQHPZ'

def process_message(data):

    if channel in data['channel']:

        text = data['text']
        #channel = data['channel']
         
        if '.gif' in text:

            if 'reload' in text: 

                reload()
                print('smileFile has been reloaded')
            
            elif 'list' in text:

                outputText = gifs[0][0]

                for gif in gifs[1:]:
                    outputText += ', '+gif[0]

                outputs.append([channel,"{}".format(outputText)])

            else:

                for gif in gifs:
                    
                    if gif[0] in text:

                        print('Sending gif {} to {}'.format(gif[0],channel))
                        outputs.append([channel,"{}".format(gif[1])])
                    

def reload():

   del gifs[:]
   gifFile = open('plugins/gifFile','r')
   for gif in gifFile:
       gifs.append(gif.strip().split(','))
   gifFile.close()

reload()
