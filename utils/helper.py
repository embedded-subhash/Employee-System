from datetime import datetime


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_header(title):

    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)