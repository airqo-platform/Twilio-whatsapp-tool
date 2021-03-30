from mongo_conect import mydb 
from flask import jsonify
contacts = mydb.contactdetails
logs = mydb.message_log



#@app.route('/add_user', methods=['POST'])
#Add user
def add_user(name,number,address):

    name = name
    number =number
    address = address

    try:

        doc = contacts.find_one({"number": number})
        if doc is None:
            contacts.insert_one({ "name": name, "number":number,"address": address })
            return("Number added")
        else:
        	return("number already exists" )


    except Exception:
        return jsonify("Failed")




#add logs
def add_message_logs(address,body,date,from_no,to_no,direction,status,media_number="0",media_url=None):

    #name = name
    address = address
    message = body
    date =date
    from_no = from_no
    to_no =to_no
    direction = direction 
    media_url = media_url
    media_number = media_number
    status = status
    log_col = {"DATE":date,"DIRECTION":direction,"FROM":from_no,"TO":to_no,"STATUS":status,"MEDIA":media_number,"MEDIA_URL":media_url,"MESSAGE":message}
    #TODO assume phone exists but once twilio is in add a number verification check


    try:
    	logs.insert_one(log_col)


    except Exception:
        return jsonify("Failed")


def delete_number():
	contacts.remove({"number":number})


def delete_message():
	pass


def update_number(number,name,address):

	contacts.update_one({"number":number}, {'$set':{ "name": name, "address": address }})
	return("number updated") 


def update_message():
	pass

def display_number():
	con =contacts.find()
	return(list(con))



def display_logs():
	all_logs =logs.find()
	return(list(all_logs))
	#for cant in all_logs:
		#print(cant)
	


def with_images():
	media =logs.find({"MEDIA":"1"})
def no_media():
	media =logs.find({"MEDIA":"0"})

def search_number(number):
	number_l = contacts.find_one({"number":number})
	s = 'Name: {0} number: {1}'.format(number_l['name'], 
		number_l['number'])
	return s

def message_number():
	msg_n = logs.find({"number":number})

#add_user("Divine","+25678huhdijd","Kampala")
#update_number("+256780303876","pro_napro","Central")
#display_number()
#search_number("+256780303876")

#output = {'name' : new_star['name'], 'distance' : new_star['distance']}
#return jsonify({'result' : output})

#add_message_logs("Kampala","HEllo","any","Divine","Napro","Reply","delivered","1","url")
#print(display_logs())

    
