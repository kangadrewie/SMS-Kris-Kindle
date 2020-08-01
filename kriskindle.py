import random
import re
from copy import copy
from twilio.rest import Client

twilio_sid = 'ACdd5f742b193e8499d45cab30e79939b5'
auth_token = 'b3af2a7cf439c507b2a77bbd47a272f8'

client = Client(twilio_sid, auth_token)

def smsMessage(toGet, toReceive):
    toGet, toGetNum = toGet.split('+')
    toReceiveName, toReceiveNum = toReceive.split('+')
    whatsApp_Message_1 = toGet + '\nThis is a random Kris Kindle Generator. You have been matched with ' + toReceiveName + '\nYou have a maximum of €150 to spend. No one knows who is matched, do not tell anyone. Happy Christmas!\n'

    # Blank below code out before running
    print(toGet, 'is toGet and,', toGetNum, 'is where sms will be sent')
    print(whatsApp_Message_1)

    #######

# THIS WILL SEND SMS, DONT RUN WITH ACTIVE CODE
    # message = client.messages \
    # .create(
    #     body=whatsApp_Message_1,
    #     from_='+12563776587',
    #     to='+'+toGetNum
    #     )

    # print(message.sid)
    return

def krisKindle(names, draw):
    matches= []
    while names:
        toGet = names.pop()
        toReceive = random.choice(draw)
        if toGet != toReceive:
            matches.append([toGet, toReceive])
            draw.remove(toReceive)
            smsMessage(toGet, toReceive)
    else:
        names.append(toGet)
    return matches
    smsMessage(toGet, toReceive)

names = [ 'Andrew +353857776581', 'Jonathan +353879015665', 'Robert +353851509909', 'Patrick +353838330479', 'Pat +353872891555', 'Breda +353851276484']

krisKindle(names,copy(names))
