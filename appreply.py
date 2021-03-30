from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from datetime import datetime
from PIL import Image
import urllib.request
import sys, os
from datetime import datetime
#swagger documentation dependencies 
import flasgger
from flasgger import Swagger 
from flasgger.utils import swag_from
from dbfunctions import add_message_logs,add_user,update_number,display_number,display_logs,search_number,display_logs 
from helper_functions import switch_msg

dir_name =os.path.dirname(os.path.abspath(sys.argv[0]))
base_filename ="images"
pdf_dir ="pdfdoc"
download_dir =os.path.join(dir_name, pdf_dir)
DOWNLOAD_DIRECTORY =os.path.join(dir_name, base_filename)



def switch(msg):

    if(msg.lower() == ("hello") or msg.lower() ==("hi")):
        reply = "Hello! \n How can i help you?" 
    elif (msg.lower() == ("one") or msg.lower() ==("1")):
        reply = "What do you think is causing it ?"
    elif (msg.lower() == ("two") or msg.lower() ==("2")):
        reply = "What kind of rubbish is being burnt?"
    elif (msg.lower() == ("three") or msg.lower() ==("3")):
        reply = "Did you get the number plate? can you please share it?"
    elif (msg.lower() == ("four") or msg.lower() ==("4")):
        reply = "Can you please describe what you see"

    else:
        reply = "Thank you for your message, let's get back to you shortly"
    return reply


app = Flask(__name__)
Swagger(app) # initialize app

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/sms", methods=['POST',"GET"])
@swag_from('reply.yml')
def sms_reply():
    """Respond to incoming with a simple text message."""

    resp = MessagingResponse()
    sender = request.form.get('From')

    print(sender)
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y %H:%M")
    file_name = dt_string+sender 
    Media_Type = request.values.get("MediaContentType0")
    body = request.values.get("Body")
    address ="Kawempe"
        #name = name   
    n_dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
     
    date =n_dt_string
    from_no = request.values.get("From").split("whatsapp:")[1]
    to_no ='+14155238886'
    direction = "Incoming"
    media_url = request.values.get('MediaUrl0')
    media_number = request.values.get('NumMedia')
    status = request.values.get('SmsStatus') 
    add_message_logs(address,body,date,from_no,to_no,direction,status,media_number,media_url)

    if request.values['NumMedia'] != '0':
        if(Media_Type == 'image/jpeg'):
            From_Mobile = request.values.get("From").split("whatsapp:")[1]
            Media_Type = request.values.get("MediaContentType0")

            img_path = DOWNLOAD_DIRECTORY+'/{}.png'.format(file_name)


            filename = '{}.png'.format(file_name)
            with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
               image_url = request.values['MediaUrl0']
               f.write(requests.get(image_url).content)

     

            resp.message("Thanks for the image!")
        #Check for media type PDF
        elif(Media_Type == 'application/pdf'):
            file_path =download_dir+'/{}.pdf'.format(file_name)
            with open(file_path, 'wb') as f:
                image_url = request.values['MediaUrl0']
                f.write(requests.get(image_url).content)
            resp.message("Thanks for the Document!")  
        elif(Media_Type ==  "video/mp4"):
            resp.message("Thanks for the video!")
        elif(Media_Type =="audio/ogg"):
            resp.message("Thanks for the Document!")

    else:
        msg = request.form.get('Body')
        reply =switch(msg)

        resp.message(reply)



    return str(resp)


@app.route("/send_msg", methods=['POST',"GET"])
@swag_from('message.yml')
def send_airqo():
    message =request.args.get("message")
    switch_msg(message)
    return("message sent")

@app.route("/add_number", methods=['POST',"GET"])
@swag_from('add_no.yml')
def add_no():
    name =request.args.get("name")
    number =request.args.get("number")
    address =request.args.get("address")            
    gs =add_user(name,number,address)
    return gs

@app.route("/update_number", methods=['POST',"GET"])
@swag_from('update_no.yml')
def update_no():
    name =request.args.get("name")
    number =request.args.get("number")
    address =request.args.get("address")            
    gs =update_number(number,name,address)
    return gs
@app.route("/display_number", methods=['POST',"GET"])
@swag_from('display_no.yml')
def display_no():
    l = display_number()
    return str(l)
@app.route("/search_number", methods=['POST',"GET"])
@swag_from('search_no.yml')
def search_no():
    number =request.args.get("number")    
    l =search_number(number)
    return l
@app.route("/display_log", methods=['POST',"GET"])
@swag_from('display_log.yml')
def display_mlog():
    l =display_logs()
    return str(l)




if __name__ == "__main__":
    app.run(debug=True)