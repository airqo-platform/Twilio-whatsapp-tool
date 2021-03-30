from twilio.rest import Client 
from authentication_info import whatsapp_numbers,twilio_number,twilio_account_sid,twilio_auth_token 
import schedule
import random
import time
#morning_message =["Good Morning. How would you describe the air today?", "Good Moring team. How is the weather and airquality today?"]
#midday_message =["How is your son’s asthma today?","How many people do you have signed up for the event?","Has your neighbour followed the advice about cooking?"]
test_message = ["Good Morning team, please look out the window. How would you rate the air quality today from 0: terrible, very unheathy to 10: it is a beautiful clear healthy day?"]
def send_message(message_list =test_message):
 
	account_sid = twilio_account_sid
	auth_token = twilio_auth_token
	client = Client(account_sid, auth_token) 
	#airqo_message= message_list[random.randint(0, len(message_list)-1)]
	airqo_message = test_message


	for whatsapp_number in whatsapp_numbers:
	 
		message = client.messages.create( 
		                              from_=twilio_number,  
		                              body=airqo_message,      
		                              to= whatsapp_number 
		                          ) 
	# to send media you should have the media url
	#media_url ="https://airqo.net
 	#print(message.sid)

 # send a message in the morning
#schedule.every().day.at("9:00").do(send_message, morning_message)

# send a message in the afternoon
#schedule.every().day.at("13:00").do(send_message, midday_message)

#testing with minute
schedule.every(2).minutes.do(send_message, test_message)
#schedule.every().hour.do(job)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
