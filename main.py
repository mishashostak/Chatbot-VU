#Unibot

SPORTS = [
    "Aikido",
    "Basketball",
    "Tennis",
    "Swimming",
    "Football",
    "Zumba",
    "Karate",
    "Yoga",
    "Waterpolo"
]

EVENTS = [
    "New Year's Party (13 Jan)",
    "Valentine's Dinner (14 Feb)",
    "Carnival Night (1 March)",
    "Karaoke Night (18 April)",
    "Kayaking Trip (5 May)",
    "Seaside Picnic (15 Sep)",
    "Halloween Party (31 Oct)",
    "Thanksgiving Jamboree (26 Nov)",
    "Christmas Dinner (18 Dec)"
]

ASSOCIATIONS = [
    "Poetry Pals",
    "Debate Club",
    "Science Society",
    "Painting and Pottery",
    "Language Club",
    "International Students Society",
    "Students for Sustainability",
    "Animal Shelter Volunteers",
    "Bunch of Backpackers"
]


def main():
    print("Hello, I am Unibot. \nWhat can I help you with?")
    user_input = input().lower()

    topic = check_topic(user_input)

    if topic is None:
        print("\nHmm, I couldn't quite tell. Are you interested in sports, events, or associations?")
        topic = input().lower()

    if topic == "sports" or "sport" in topic:
        sports_chat()
    elif topic == "events" or "event" in topic:
        events_chat()
    elif topic == "associations" or "association" in topic:
        association_chat()
    else:
        print("Sorry, I can only help with sports, events, or associations right now.")
    
    print("Thank you for using Unibot! Have a good day.")


def check_topic(user_input):    
    #FILL
    sports_words = [
        "sport", "sports", "gym", "training", "train", "weight", "health", "fitness", 
        "excercise", "workout", "tournament", "competition", "stretch", "cardio", 
        "active", "track", "field", "ball", "run", "league", "soccer", "match", "team",
        "coach", "court", "baseball", "sporty", "gymnasium", "athlete", "athletic", "recreation"
    ] + [s.lower() for s in SPORTS]
    
    events_words = [
        "event", "party", "dinner", "festival", "concert", "picnic", "night", "celebration", 
        "campus", "borrel", "drinking", "gathering", "trip", "halloween", "christmas", 
        "thanksgiving", "valentine", "valentines", "weekend", "mixer", "outing", "meet",
        "meetup", "hangout", "holiday", "fun", "music", "dance", "dancing", "people"
    ] + [word.lower() for e in EVENTS for word in e.split()]
    
    association_words = [
        "association", "club", "society", "societies", "group", "student", "students", "network",
        "organization", "join", "membership", "friends", "teamwork", "connect", "connections",
        "together", "community", "committee", "support", "interest", "union", "volunteer",
        "international", "creative", "career", "networking", "hobby", "research"
    ] + [word.lower() for a in ASSOCIATIONS for word in a.split()]

    sports_count = count_keywords(user_input, sports_words)
    events_count = count_keywords(user_input, events_words)
    association_count = count_keywords(user_input, association_words)

    scores = {"sports": sports_count, "events": events_count, "associations": association_count}
    best_topic = max(scores, key=scores.get)

    if scores[best_topic] == 0 or list(scores.values()).count(scores[best_topic]) > 1:
        return None
    
    return best_topic


def count_keywords(user_input, keywords):
    count = 0
    for word in keywords:
        count += user_input.count(word)
    return count


#FILL
#The print() functions are placeholders
def sports_chat():
    print("sports")


def events_chat():
    print("events")


def association_chat():
    print("association")


main()