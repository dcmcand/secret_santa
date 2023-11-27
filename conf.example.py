names = {
    "Barney": {"email": "barney@bedrock.com", "so": "Betty", "interests": ["Bowling", "Jokes", "Movies"]},
    "Fred": {"email": "fred@bedrock.com", "so": "Wilma", "interests": ["Bowling", "Dinosaurs", "Golf"]},
    "Wilma": {"email": "wilma@bedrock.com", "so": "Fred", "interests": ["Cooking", "Gardening", "Shopping"]},
    "Betty": {"email": "betty@bedrock.com", "so": "Barney", "interests": ["Reading", "Music", "Crafts"]},
    "Pebbles": {"email": "pebbles@bedrock.com", "so": "", "interests": ["Exploring", "Drawing", "Sports"]},
    "BamBam": {"email": "bambam@bedrock.com", "so": "", "interests": ["Rock Music", "Cave Painting", "Athletics"]},
}

api_key = "supersecretstring"

mailgun_domain = "mg.bedrock.com"

sender_name = "Secret Santa"

sender_email = "santa@{}".format(mailgun_domain)
