from slacker import Slacker
import time


slack = Slacker(token)
sent_message = slack.chat.post_message('#testing_ground','fuck off',as_user=True)
print(sent_message)

print(slack.rtm.start())
		

