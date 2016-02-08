# -*- coding utf-8 -*-
import time
import numpy
from slackclient import SlackClient

smilies = ['(^_^)','(T_T)','\(^_^)/','(^O^)','(*_*)','(<,<)','(?_?)']
smiley = 0

while True:
        sc = SlackClient(token)
        if sc.rtm_connect():

                #channel = sc.server.channels.find('general')
                #channel_id = 'C0K2UNFB2'

                channel = sc.server.channels.find('testing_ground')
                channel_id = 'C0L0FQHPZ'

                start = time.time()
                elapsed = 0
                while True:
                        message_list = []
                        message_list = sc.rtm_read()
                        for message in message_list:
                                try:
                                        id_check = message['channel']
                                        if channel_id == id_check:
                                                if message['type'] == 'message':
                                                        text = message['text']
                                                        print(text.encode('utf-8'))
                                                        print('before text check ',smiley)
                                                        if '.smile' in text:
                                                                #channel = sc.server.channels.find('testing_ground')
                                                                print('sending message')
                                                                print(smilies[smiley],smiley)
                                                               
                                                                #print(sc.server.channels.find('testing_ground').send_message(smilies[smiley]))
                                                                channel.send_message(smilies[smiley])
                                                                smiley = numpy.random.random_integers(len(smilies))
                                except:
                                        continue
                        
                        time.sleep(0.1)
                        
                        elapsed = time.time() - start
                        if elapsed > 3:
                                sc.server.ping()
                                start = time.time()
    
