import schedule
import random
import time 
from msg_send import send_messages
from twilio.rest import Client 
from msg_auth import whatsapp_numbers,twilio_number,twilio_account_sid,twilio_auth_token 
import schedule
import random
import time  

message ="How is the weather"
schedule.every(2).minutes.do(send_messages(whatsapp_numbers, message))
#schedule.every().hour.do(job)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)