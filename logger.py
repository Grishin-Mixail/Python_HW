from datetime import datetime as dt

def logger_del(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}; deleted data;{}\n"
                        .format(time, data))

def logger_insert(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}; insert data;{}\n"
                        .format(time, data))

def logger_mod(data):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}; modified data;{}\n"
                        .format(time, data))


