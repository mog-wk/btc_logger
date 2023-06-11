import os
import datetime


def write_log(b_data: str, path: str, date=None) -> bool:
    # writes log to "path" file return True if sucesseful
    if not date: date = datetime.datetime.now()
    if os.path.exists(path): log_path = os.path.relpath(path)
    else: return False

    date_log = f"{date.day}/{date.month}/{date.year} {date.hour:02d}:{date.minute:02d}.{date.second:02d}"

    with open(log_path, 'a') as f:
        line = "{} => {}\n".format(date_log, b_data)
        f.write(line)
    return True


def print_log(log=None, label=None):
    # prints log file to stdout
    #TODO add label delimiter
    log_file = os.path.relpath("logs/coin_market_cap_log.txt") if not log else os.path.abspath(log)
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            for line in f.readlines():
                print(line)
    else:
        print(f"log output: \"{log_file}\" does not exists")


def write_error(err: str, path: str, date=None) -> bool:
    # writes error message to "path" file return True if sucesseful
    if not date: date = datetime.datetime.now()
    if os.path.exists(path): log_path = os.path.relpath(path)
    else: return False

    with open(path, "a") as f:
        f.write(f"{date.hour} {date.day}/{date.month}/{date.year} error: {err}\n")
    return True


if __name__ == "__main__":
    path = "logs/test_log.txt"
    write_log("testing... ", path)
    print_log(path)
