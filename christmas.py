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

def getInterests(giftee):
    interests = names[giftee]["interests"]
    if len(interests) <= 0:
        return ""
    msg = "They wrote to Santa and said they were interested in "
    for interest in interests[:-1]:
        msg += " {},".format(interest)
    if len(interests) > 1:
        msg += " and"
    msg += " {}.\n".format(interests[-1])
    return msg

def send_simple_message(email, gifter, giftee):
	return requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(conf.mailgun_domain),
        auth=("api", conf.api_key),
        data={"from": "{} <{}>".format(conf.sender_name, conf.sender_email),
              "to": [email],
              "subject": "Secret Santa",
              "text": "Hi {},\nThis is your secret santa assignment! \nThis Christmas, you will buy a gift for {}.\n{}Remember this is a SECRET Santa so ssssshhhhhhh!\nMerry Christmas\nSanta Claus".format(gifter, giftee, getInterests(giftee))}) 
assignments = assign_names(names.keys())

for pair in assignments: 
    print("{} gives to {}".format(pair[0], pair[1]))
    print(send_simple_message(names[pair[0]]["email"], pair[0], pair[1]).text)
