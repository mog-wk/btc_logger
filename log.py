import os
import datetime


def write_log(log: os.path, b_data: str, date=None) -> bool:
    if not date: date = datetime.datetime.now()
    if not line:
        raise f"provide  a log line"

    date_log = f"{date.hour}:{date.minutes} {date.day}/{date.month}/{date.year}"

    with open(log, 'w') as f:
        line = date_log + b_line + '\n'
        print(line)
        f.write(line)


if __name__ == "__main__":
    pass
