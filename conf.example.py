
names = {
    "Barney": {"email": "barney@bedrock.com", "so": "Betty"},
    "Fred": {"email": "fred@bedrock.com", "so": "Wilma"},
    "Wilma": {"email": "wilma@bedrock.com", "so": "Fred"},
    "Betty": {"email": "betty@bedrock.com", "so": "Barney"},
    "Pebbles": {"email": "pebbles@bedrock.com", "so": ""},
    "BamBam": {"email": "bambam@bedrock.com", "so": ""},
}


api_key = "supersecretstring"

mailgun_domain = "mg.bedrock.com"

sender_name = "Secret Santa"

sender_email = "santa@{}".format(mailgun_domain)
