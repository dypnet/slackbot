import time
import numpy
crontable = []
outputs = []

smilies = ['(^_^)','(T_T)','\(^_^)/','(^O^)','(*_*)','(<,<)','(?_?)']

def process_message(data):
    print(data['channel'])
    if "C0L0FQHPZ" in data['channel']:
        if '.smile' in data['text']:
            randomNumber = numpy.random.random_integers(len(smilies)-1)
            outputs.append([data['channel'],\
                    "{}".format(smilies[randomNumber])])
        print(data)
