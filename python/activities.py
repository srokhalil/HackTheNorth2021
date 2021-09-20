import random
activities = {
    'sports': {
        'basketball': 2,
        'jogging': 0,
        'tennis': 2,
        'volleyball': 1,
        'football': 2,
        'golf': 4,
        'swimming': 1,
        'badminton': 0,
        'cricket': 5,
        'yoga': 0,
        'cycling': 3,
        'go bowling': 1,
        'frisbee': 1,
        'marathon': 5,
        'gymnastics': 1,
        'mountain climbing': 3,
        'trekking': 3,
        'archery': 0,
        'skateboarding': 0,
        'snorkeling': 2,
        'fitness': 2
    },

    'others': {
        'baking a cake': 2,
        'try out a new recipe': 1,
        'take a course': 3,
        'have a quick bite': 1,
        'meditate': 0,
        'stretch': 0,
        'take a nap': 1,
        'hangout with friends or family': 1,
        'hangout with friends or family': 2,
        'hangout with friends or family': 3,
        'hangout with friends or family': 4,
        'hangout with friends or family': 5,
        'take a walk in the park': 0,
        'get a crazy new hairstyle': 1,
        'gardening': 2,
        'go camping': 5,
        'self care': 1
    },

    'creativity': {
        'writing': 5,
        'painting': 5,
        'sing': 0,
        'play an instrument': 1,
        'perform': 2,
        'dance': 1,
        'sculpting': 2,
        'woodworking': 4,
        'design your room': 3,
        'coloring': 0,
        'visit a museum': 4,
        'take photos': 1,
        'create a photo album': 0,
        'create a time capsule': 0,
        'write meaningful letters to your loved ones': 1,
        'knit': 2,
        'go for an art class': 3,
        'fold some origami': 0,
        'listen to some music': 0,
        'cosplay': 1,
        'DIY project': 3,
        'make jewelery': 0,
        'reading': 1
    },

    'entertainment': {
        'attend a play': 4,
        'attend a comedy show': 3,
        'watch a movie on netflix': 2,
        'watch a episode of your favorite tv show': 1,
        'watch youtube videos': 0,
        'listen to a podcast': 0,
        'play video games': 2,
        'play word or card games': 1,
        'binge on movies': 5,
        'explore the library': 3,
        'go to the amusement park': 5,
        'go to the arcade': 1,
        'sightseeing': 3,
        'fishing': 2,
        'browse social media': 0
    }
}


def get_activity(hours, categories):
    activity_list = []
    print("hours", hours)
    print("categories", categories)

    for category in categories:
        if category in activities:
            for activity, activity_hours in activities[category].items():
                if activity_hours == hours:
                    activity_list.append(activity)

    print('activity_list', activity_list)
    result = random.choice(activity_list)
    print("result", result)
    return result
