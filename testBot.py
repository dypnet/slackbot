import time
from slackclient import SlackClient

sc = SlackClient(token)

if sc.rtm_connect():
    channel = sc.server.channels.find('testing_ground')
    channel_id = 'C0L0FQHPZ'
    while True:
        message_list = sc.rtm_read()
        print(message_list)
        if len(message_list) > 0:
            print('accepted')
            try:
                id_check = message_list[0]['channel']
                print(id_check,type(id_check),channel_id)
                if channel_id == id_check:
                    print("id check")
                    if message_list[0]['type'] == 'user_typing':
                        channel.send_message('Stop typing!')
                    
                    elif message_list[0]['type'] == 'message':
                        text = message_list[0]['text']
                        print(text)
                        if 'rompe' in text:
                            print('sending message')
                            
                            channel.send_message('Husk prostata!')
            except:
                continue
                
        time.sleep(0.1)
        #channel.send_message('I am the creator of all things unholy, worship me!')

    
