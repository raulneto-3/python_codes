import time
from datetime import datetime
from player import notification
import winsound

def set_alarm(hour, minute):
    now = datetime.now()
    alarm_time = datetime(now.year, now.month, now.day, hour, minute)
    time_diff = alarm_time - now
    time.sleep(time_diff.total_seconds())

    notification.notify(
        title="Alarm",
        message="Alarm is ringing",
        app_name="Alarm Clock",
        timeout=10
    )

    winsound.Beep(1000, 1000)

if __name__ == '__main__':
    hour = int(input("Enter the hour: "))
    minute = int(input("Enter the minute: "))
    set_alarm(hour, minute)