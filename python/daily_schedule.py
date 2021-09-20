from python.activities import get_activity
# Usage: get_activity(hours, category)
from datetime import datetime

# Generate waking time


def generate_waking_time(wake_time):
    start = datetime.strptime(str(wake_time), "%H")
    end = datetime.strptime(str(wake_time) + ':10', "%H:%M")
    return {'activity': 'wakeup', 'start': start.strftime("%I:%M %p"), 'end': end.strftime("%I:%M %p")}

# Generate activity and time before work


def generate_activity_before_work(activity_category, wake_time, leisure_hours_before_work, start_work_time):

    hours_before_work = start_work_time - wake_time

    if leisure_hours_before_work is None:
        leisure_hours_before_work = hours_before_work
    if leisure_hours_before_work > hours_before_work:
        leisure_hours_before_work = hours_before_work
    if leisure_hours_before_work > 5:
        leisure_hours_before_work = 5

    before_work_activity = get_activity(leisure_hours_before_work, activity_category)
    start = datetime.strptime(str(start_work_time - leisure_hours_before_work), "%H")
    end = datetime.strptime(str(start_work_time), "%H")
    return {'activity': before_work_activity, 'start': start.strftime("%I:%M %p"), 'end': end.strftime("%I:%M %p")}

# Generate working time (before break)


def generate_work_before_break(start_work_time, work_break_time):
    start = datetime.strptime(str(start_work_time), "%H")
    end = datetime.strptime(str(work_break_time), "%H")
    return {'activity': 'work', 'start': start.strftime("%I:%M %p"), 'end': end.strftime("%I:%M %p")}

# Generate work break time and activity


def generate_during_break(activity_category, work_break_time, work_break_hours):
    break_activity = get_activity(work_break_hours, activity_category)
    start = datetime.strptime(str(work_break_time), "%H")
    end = datetime.strptime(str(work_break_hours + work_break_hours), "%H")
    return {'activity': break_activity, 'start': start.strftime("%I:%M %p"), 'end': end.strftime("%I:%M %p")}

# Generate working time (after break)


def generate_work_after_break(work_break_time, work_break_hours, end_work_time):
    start = datetime.strptime(str(work_break_time+work_break_hours), "%H")
    end = datetime.strptime(str(end_work_time), "%H")
    return {'activity': 'work', 'start': start.strftime("%I:%M %p"), 'end': end.strftime("%I:%M %p")}

# Generate activity and time after work


def generate_activity_after_work(activity_category, end_work_time, leisure_hours_after_work, sleep_time):

    hours_after_work = sleep_time - end_work_time

    if leisure_hours_after_work is None:
        leisure_hours_after_work = hours_after_work
    if leisure_hours_after_work > hours_after_work:
        leisure_hours_after_work = hours_after_work
    if leisure_hours_after_work > 5:
        leisure_hours_after_work = 5

    before_work_activity = get_activity(
        leisure_hours_after_work, activity_category)
    start = datetime.strptime(str(sleep_time - leisure_hours_after_work), "%H")
    end = datetime.strptime(str(sleep_time), "%H")
    return {'activity': before_work_activity, 'start': start.strftime("%I:%M %p"), 'end': end.strftime("%I:%M %p")}

# Generate sleeping time


def generate_sleeping_time(sleep_time):
    start = datetime.strptime(str(sleep_time), "%H")
    return {'activity': 'goodnight', 'start': start.strftime("%I:%M %p")}
