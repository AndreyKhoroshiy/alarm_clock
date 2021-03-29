from datetime import datetime
from playsound import playsound

alarm_time = input("Введите время для срабатывания будильника в 24-часовом формате 'HH.MM.SS'")


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Неверный формат времени, попробуйте снова ввести корректное время"
    else:
        if int(alarm_time[0:2]) > 23:
            return "Неверный ввод для формата часы, попробуйте ввести снова"
        elif int(alarm_time[3:5]) > 59:
            return "Неверный ввод для формата минуты, попробуйте ввести снова"
        elif int(alarm_time[6:8]) > 59:
            return "Неверный ввод для формата секунды, попробуйте снова"
        else:
            return "Ok"


validate = validate_time(alarm_time)
if validate != "Ok":
    print(validate)
else:
    print(f"Будильник установлен на {alarm_time}...")

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]


while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("Просыпайся")
                playsound('sound/2-mashi-bosaja.mp3')
                break
