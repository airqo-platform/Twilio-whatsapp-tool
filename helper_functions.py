from twilio.rest import Client 
from msg_auth import whatsapp_numbers,twilio_number,twilio_account_sid,twilio_auth_token,Bwaise_II, Kyebando,Mulago_II
import schedule
import random
import time   
from dbfunctions import add_message_logs 


account_sid = twilio_account_sid
auth_token = twilio_auth_token
client = Client(account_sid, auth_token) 
#airqo_message= message_list[random.randint(0, len(message_list)-1)]
def in_location():
	locations = [Bwaise_II,Kyebando,Mulago_II]
	dict_dict = {'Bwaise II':Bwaise_II, 'Kyebando':Kyebando, 'Mulago II':Mulago_II}
	for name,locations in dict_dict.items():
		for key, value in locations.items():
			inquire(key,value,name)

	return"message Sent"


def send_message(name,number, msg):
    message = client.messages.create(
        body='Hello {} ! {}'.format(name,msg),
        from_='whatsapp:+14155238886',
        to='whatsapp:' + number,

    )

    body = message.body
    address ="Kawempe"
    date =message.date_created
    from_no = '+14155238886'
    to_no =message.to
    direction = "Reply" 
    media_url = "None"
    media_number = message.num_media
    status = message.status
    add_message_logs(address,body,date,from_no,to_no,direction,status,media_number,media_url)

    return "Success"



def send_messages(numbers, message):
	for key, value in numbers.items():
		send_message(key,value, message)

def inquire(name,number,location):
    message = client.messages.create(
        body="Hi {} !  \n We see a spike in pollution levels within {},What can you observe \n 1. Commercial burning of bones \n 2. Rubbish burning \n 3.Fumes from old cars \n 4. Others".format(name,location),
        from_='whatsapp:+14155238886',
        to='whatsapp:' + number,

    )
    body = message.body    
    address ="Kawempe"
    date =message.date_created
    from_no = '+14155238886'
    to_no =message.to
    direction = "Reply" 
    media_url = "None"
    media_number = message.num_media
    status = message.status
    add_message_logs(address,body,date,from_no,to_no,direction,status,media_number,media_url)    
    return "Success"


def sendimg(media_url=None, number =None):
    message = client.messages.create(
             media_url=url,
             from_='whatsapp:+14155238886',
             body="Enjoy the Picture",
             to='whatsapp:' + number
         )


message ="Hello,Welcome and thank you for taking a step to improve air quality in your community. Together we can do More!"

#inquiry = " \n We see a spike in pollution levels within {},What can you observe \n 1. Commercial burning of bones \n 2. Rubbish burning \n 3.Fumes from old cars \n 4. Others".

#send_messages(whatsapp_numbers, message)
#send_messages(whatsapp_numbers, inquiry)
#in_location()
#send = request.form.get("msg")
def switch_msg(msg):
	if msg =="1":
		message ="Hello,Welcome and thank you for taking a step to improve air quality in your community. Together we can do More!"
		send_messages(whatsapp_numbers, message)
	elif msg =="2":
		in_location()
	else:
		send_messages(whatsapp_numbers, msg)

#switch_msg("Airqo")

#message propertie