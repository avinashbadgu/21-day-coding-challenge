import time
from plyer import notification

if __name__ == '__main__':
    stretch_interval = 15


    while True:
        notification.notify(
            title="Please Drink Water Now!!",
            message="It's important to stay hydrated! The recommended daily fluid intake is about 15.5 cups (3.7 liters) for men and 11.5 cups (2.7 liters) for women.",
            app_icon="D:\pythonProject\Iconarchive-Seaside-Tools-Water-Bottle.ico",
            timeout=12
        )
        time.sleep(6)


        notification.notify(
            title="Stretch Break Reminder",
            message="Take a break and stretch your muscles. Give your eyes and body some rest.",
            app_icon="D:\pythonProject\Icons8-Windows-8-Time-Sandglass.ico",
            timeout=12
        )

        time.sleep(stretch_interval)