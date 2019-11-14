import random
import requests
import conf

names = conf.names

def get_name(name, name_list):
    choice = random.choice(name_list)
    if (choice == name) or (choice == names[name]["so"]):
        choice = get_name(name, name_list)

    return choice

def assign_names(name_list):
    assignments = []
    giftees = list(name_list)
    try:
        for name in name_list:
            rand = get_name(name, giftees) 
            del giftees[giftees.index(rand)]
            assignments.append([name, rand])
    except:
        return assign_names(name_list)
    return assignments

def send_simple_message(email, gifter, giftee):
	return requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(conf.mailgun_domain),
        auth=("api", conf.api_key),
        data={"from": "{}Secret Santa <{}santa@mg.leblibrary.com>".format(conf.sender_name, conf.sender_email),
              "to": [email],
              "subject": "Hello",
              "text": "Hi {}, you will buy for {} this christmas.".format(gifter, giftee)})

assignments = assign_names(names.keys())

for pair in assignments: 
    send_simple_message(names[pair[0]]["email"], pair[0], pair[1]) 
