#Unibot: Project Computational Thinking

#Hard code the data from unilife.csv
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

#Main conversational flow function
def main():
    print("What can I help you with?")
    user_input = input("(type 'stop' to terminate or 'r' to restart): ").lower()
    
    #Checks if user wants to terminate the program
    if user_input == "stop":
        topic = "Quit"
    else:
        topic = check_topic(user_input)
    
    #Ask user to specify if no keywords or if tie in keywords
    if topic is None:
        print("\nHmm, I couldn't quite tell. Are you interested in sports, events, associations or studying?")
        topic = input().lower()

    #Send user to relative topic conversation flow function
    if topic == "sports" or "sport" in topic:
        sports_chat()
    elif topic == "events" or "event" in topic:
        events_chat()
    elif topic == "associations" or "association" in topic:
        association_chat()
    elif topic == "study" or "study" in topic:
        study_chat()
    elif topic == "Quit":
        print("Talk to you soon!")
    else:
        print("Sorry, I can only help with sports, events, associations, or studying right now.")
        main()
    
    print("\nThank you for using Unibot! Have a good day :)")

#Used to identify topic of conversation from an input
def check_topic(user_input):    
    #Lists of most probable keywords for each topic
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
        "meetup", "hangout", "holiday", "fun", "music", "dance", "dancing", "people", "events"
    ] + [word.lower() for e in EVENTS for word in e.split()]
    
    association_words = [
        "association", "club", "society", "societies", "group", "student", "students", "network",
        "organization", "join", "membership", "friends", "teamwork", "connect", "connections",
        "together", "community", "committee", "support", "interest", "union", "volunteer",
        "international", "creative", "career", "networking", "hobby", "research", "associations"
    ] + [word.lower() for a in ASSOCIATIONS for word in a.split()]

    study_words = [
        "exams", "exam", "tests", "test", "quiz", "homework", "struggle", "struggling", "difficult", 
        "assignment", "assignments", "challenge", "help", "subject", "learn", "learning", "tips", 
        "advice", "practice", "desk", "professor", "class", "classes", "course", "courses", "lecture",
        "understand", "teacher", "study", "studying"
    ]

    sports_count = count_keywords(user_input, sports_words)
    events_count = count_keywords(user_input, events_words)
    association_count = count_keywords(user_input, association_words)
    study_count = count_keywords(user_input, study_words)

    scores = {
        "sports": sports_count, 
        "events": events_count, 
        "associations": association_count,
        "study": study_count
    }
    best_topic = max(scores, key=scores.get)

    #Check if there are no keywords OR if there is an equal score between two topics
    if scores[best_topic] == 0 or list(scores.values()).count(scores[best_topic]) > 1:
        return None
    
    return best_topic

#Used to linearly count the number of keywords for each list of keywords
def count_keywords(user_input, keywords):
    count = 0
    for word in keywords:
        count += user_input.count(word)
    return count


#Conversational flow for the sports topic
def sports_chat():
    print("\nWe offer plenty of sports at VU!")
    print("Were you looking for a specific sport? (yes/no)")
    answer = input("(yes/no): ").strip().lower()
    if answer == "r": main()

    if "y" in answer:
        print("Which sport are you interested in?")
        sport = input().strip().lower()
        if sport == "r": main()

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


#Conversational flow for the events topic
def events_chat():
    print("We offer plenty of events at VU Amsterdam!")
    print("\nWould you like to look for a specific event? (yes/no)")
    answer = input("(yes/no): ").strip().lower()
    if answer == "r": main()

    if "y" in answer:
        print("You can enter a keyword (e.g., party, dinner, Christmas) and I will look for that event")
        keyword = input("Enter a keyword: ").strip().lower()
        if keyword == "r": main()

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


#Conversational flow for the associations topic
def association_chat():
    print("\nAre you interested in a specific type of association (e.g., debate, art, science)?")
    interest = input("Enter a keyword or press Enter to see all: ").strip().lower()
    if interest == "r": main()

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
            print("\nI couldn't find any associations for that interest. Here are all the others you could explore:")
            for a in ASSOCIATIONS:
                print("-", a)
    else:
        print("\nHere are all the associations you could join:")
        for a in ASSOCIATIONS:
            print("-", a)

    print("\nYou can learn more or sign up through the VU website: https://vu.nl/en/student/associations")


#Conversational flow for the study topic
def study_chat():
    print("\nAre you struggling with something in your studies, or are you just looking for practical information?")
    answer = input("(Type 'struggling' or 'practical'): ").strip().lower()
    if answer == "r": main()

    if "strug" in answer:
        print("\nWould you like to share what you're struggling with other students or keep it private?")
        share = input("(Type 'share' or 'private'): ").strip().lower()
        if share == "r": main()

        if "share" in share:
            print("\nThat's great! You could look for a study group to discuss and work through it together.")
            print("You can find study groups by asking one of the large Whatsapp groupchats specific to your program.")
            print("The most popular one belongs to Athena Studies so you can easily find it with a Google search! :)")
        else:
            print("\nThat's completely fine, not everyone feels comfortable sharing.")
            print("You might want to reach out to your student advisor for personal guidance.")
            print("You can contact them via: https://vu.nl/en/student/contact-student-guidance-and-support/academic-advisor")
    else:
        print("\nGot it! If you're only looking for practical study information, the Student Desk can help.")
        print("You find contact info here: https://vu.nl/en/education/more-about/student-desk-vrije-universiteit-amsterdam")

#Call the main() function and start the process
print("Hello, I am Unibot!")
main()