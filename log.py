import os
import datetime


def write_log(b_data: str, path: str, date=None) -> bool:
    if not date: date = datetime.datetime.now()
    if os.path.exists(path): log_path = os.path.relpath(path)
    else: return False
    #if os.path.isfile(log_path):
        #print("path not fould:\n", log_path)
        #return False

    date_log = f"{date.hour}:{date.minute}.{date.second} {date.day}/{date.month}/{date.year}"

    with open(log_path, 'a') as f:
        line = "{} => {}\n".format(date_log, b_data)
        f.write(line)

    return True


def print_log(output_file=None):
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            for line in f.readlines():
                print(line, end="")

def write_error(err: str, path: str, date=None):
    if not date: date = datetime.datetime.now()
    if os.path.exists(path): log_path = os.path.relpath(path)
    else: return False

    with open(path, "a") as f:
        f.write(f"{date.hour} {date.day}/{date.month}/{date.year} error: {err}\n")



if __name__ == "__main__":
    path = "logs/test_log.txt"
    write_log("testing... ", path)
    print_log(path)
