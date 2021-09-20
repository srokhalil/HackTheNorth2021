from datetime import timedelta, date
from python.daily_schedule import *
from python.eventbrite_events import get_events

# hours = {'start-work : value, 'end-work' : value, 'wake': value, 'sleep': value, 'work-break-time' : value, 'work-break' : value, 'hours-before-work' : value, 'hours-after-work': value, 'days-worked': [value]}


def generate_schedule_week_csv(activity_category, hours):

    calendar = ""

    days = []
    today = date.today()
    days_delta = 6 - today.weekday()
    if days_delta <= 0:
        days_delta += 7
    sunday = date.today() + timedelta(days_delta)
    for i in range(0, 7):
        day = sunday + timedelta(days=i)
        days.append(day.strftime('%m/%d/%y'))

    # Set variables
    start_work_time = hours['start-work']
    end_work_time = hours['end-work']
    wake_time = hours['wake']
    sleep_time = hours['sleep']
    work_break_time = hours['work-break-time']
    work_break_hours = 1 # standard break is 1 hr
    leisure_hours_before_work = hours['hours-before-work']
    leisure_hours_after_work = hours['hours-after-work']
    days_worked = hours['days-worked']


    calendar += 'Subject, Start Date, Start Time, End Time, Description, Location\n'
    for day in days:
        if days.index(day) in days_worked:
            waking = generate_waking_time(wake_time)
            subject = waking['activity']
            start = waking['start']
            end = waking['end']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

            before_work = generate_activity_before_work(
                activity_category, wake_time, leisure_hours_before_work, start_work_time)
            subject = before_work['activity']
            start = before_work['start']
            end = before_work['end']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

            work_before_break = generate_work_before_break(
                start_work_time, work_break_time)
            subject = work_before_break['activity']
            start = work_before_break['start']
            end = work_before_break['end']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

            during_break = generate_during_break(
                activity_category, work_break_time, work_break_hours)
            subject = during_break['activity']
            start = during_break['start']
            end = during_break['end']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

            work_after_break = generate_work_after_break(
                work_break_time, work_break_hours, end_work_time)
            subject = work_after_break['activity']
            start = work_after_break['start']
            end = work_after_break['end']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

            after_work = generate_activity_after_work(
                activity_category, end_work_time, leisure_hours_after_work, sleep_time)
            subject = after_work['activity']
            start = after_work['start']
            end = after_work['end']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

            sleep = generate_sleeping_time(sleep_time)
            subject = sleep['activity']
            start = sleep['start']
            calendar += '{0}, {1}, {2}, {3}\n'.format(subject, day, start, end)

        else:
            events = get_events(day)
            for event in events:
                individual_event = events[event]
                subject = individual_event['event-name']
                location = individual_event['venue']
                start = individual_event['start-time']
                end = individual_event['end-time']
                description = 'Event link: {0} \nEvent category: {1} \nEvent description: {2}'.format(
                    individual_event['eventbrite-link'], individual_event['category'], individual_event['description'])
                calendar += '{0}, {1}, {2}, {3}, {4}, {5}'.format(
                    subject, day, start, end, description, location)

    return calendar
