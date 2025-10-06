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
    
    print("\nThank you for using Unibot! Have a good day :)")


def check_topic(user_input):    
    sports_words = [
        "sport", "sports", "gym", "training", "train", "weight", "health", "fitness", 
        "excercise", "workout", "tournament", "competition", "stretch", "cardio", "play",
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


def sports_chat():
    print("\nAre you interested in a specific sport, or would you like to try something new?")
    print("You can type 'specific' for a certain sport you had in mind.")
    answer = input("(Type 'specific' or 'new'): ").strip().lower()

    if "specific" in answer:
        print("Which sport are you interested in?")
        sport = input().strip().lower()
        matches = [s for s in SPORTS if sport in s.lower()]
        if matches:
            print("\nThat sport is available at Sportcentrum VU!")
            print("You can sign up on the Sportcentrum VU website: https://sportcentrumvu.nl/")
        else:
            print("\nThat sport might not be available. Here's what we do offer though:")
            for s in SPORTS:
                print("-", s)
    else:
        print("\nHere are all the sports we have available:")
        for s in SPORTS:
            print("-", s)
        print("\nYou can sign up for any of them on the Sportcentrum VU website: https://sportcentrumvu.nl/")


def events_chat():
    print("We offer plenty of events at VU Amsterdam!")
    print("\nWould you like to look for a specific event? (yes/no)")
    answer = input("(yes/no): ").strip().lower()

    if "y" in answer:
        print("You can enter a keyword (e.g., party, dinner, Christmas) and I will look for that event")
        keyword = input("Enter a keyword: ").strip().lower()
        matches = [e for e in EVENTS if keyword in e.lower()]
        if matches:
            print("\nHere's what I found:")
            for e in matches:
                print("-", e)
        else:
            print("\nSorry, I couldn't find an event matching that keyword. So here are all the events we offer:")
            for e in EVENTS:
                print("-", e)
    else:
        print("\nNo problem! Here is the full list of events we offer:")
        for e in EVENTS:
                print("-", e)
    print("If youre interested, you can also check out other events that are happening at: https://vu.nl/en/events")


def association_chat():
    print("\nAre you interested in a specific type of association (e.g., debate, art, science)?")
    interest = input("Enter a keyword or press Enter to see all: ").strip().lower()

    if interest:
        matches = [a for a in ASSOCIATIONS if interest in a.lower()]
        if matches:
            print("\nBased on your interest, you might enjoy:")
            for a in matches:
                print("-", a)
        elif interest == "no":
            print("Oh, that's a shame, I suppose we can restart")
            main()
        else:
            print("\nI couldn't find any associations for that interest. Here are some others you could explore:")
            for a in ASSOCIATIONS[:5]:
                print("-", a)
    else:
        print("\nHere are all the associations you could join:")
        for a in ASSOCIATIONS:
            print("-", a)

    print("\nYou can learn more or sign up through the VU website: https://vu.nl/en/student/associations")


main()