#python program to monitor contents of a file and when there is a change, check for "Battery Percentage"
import re
from dotenv import load_dotenv
import os

load_dotenv()

RAZER_LOG_FILE_PATH = os.getenv("RAZER_LOG_FILE_PATH")

def check_file(filename):
    with open(filename) as f:
        content = f.read()
    return content

#method to search for last occurence of "Battery Percentage: " and return the number
def check_battery_percentage(content):
    BATTERY_PERCENTAGE_PATTERN = r"Battery Percentage: (\d+)"
    match = re.findall(BATTERY_PERCENTAGE_PATTERN, content)
    battery_percentage = match[-1]
    return battery_percentage

def main():
    filename = RAZER_LOG_FILE_PATH
    content = check_file(filename)
    battery_percentage = check_battery_percentage(content)
    print(battery_percentage)

if __name__ == "__main__":
    main()