
import re


DIGITS_RE = re.compile(r'([1-9]|one|two|three|four|five|six|seven|eight|nine)(.*)')
# DIGITS_RE = re.compile(r'([1-9])(.*)')
DIGITS_LOOKUP = {
    "1": "1",
    "one": "1",
    "2": "2",
    "two": "2",
    "3": "3",
    "three": "3",
    "4": "4",
    "four": "4",
    "5": "5",
    "five": "5",
    "6": "6",
    "six": "6",
    "7": "7",
    "seven": "7",
    "8": "8",
    "eight": "8",
    "9": "9",
    "nine": "9"
}


def process_line(line):
    unprocessed = line
    processed = []
    while unprocessed:
        print(f"Unprocessed: {unprocessed}")
        match = DIGITS_RE.match(unprocessed)
        if match:
            print("Matched")
            print(match.groups())

            processed.append(DIGITS_LOOKUP[match.group(1)])
            unprocessed = match.group(2)
        else:
            print("Not Matched")
            unprocessed = unprocessed[1:]

    print(processed)
    first_digit = processed[0]
    last_digit = processed[-1]
    result = int(first_digit + last_digit)
    return result


if __name__ == "__main__":
    calib_file = "calibration-data.txt"
    calib_lines = []

    with open(calib_file, "r") as fin:
        calib_lines = fin.readlines()

    # process_line(calib_lines[0])
    processed_lines = [
        process_line(line) for line in calib_lines
    ]
    print(len(processed_lines))
    print(sum(processed_lines))
