
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


def tokenize_line(line):
    unprocessed = line
    processed = []
    while unprocessed:
        print(f"Unprocessed: {unprocessed}")
        match = DIGITS_RE.match(unprocessed)
        if match:
            print("Matched")
            print(match.groups())

            processed.append(match.group(1))
            unprocessed = match.group(2)
        else:
            print("Not Matched")
            unprocessed = unprocessed[1:]

    print(processed)
    return processed


def extract_last(line):
    """
    Process the last digit by starting at the end of the line
    and moving backward towards the beginning of the line.
    """
    print("Matching last digit")
    for i in range(1, len(line) + 1):
        unprocessed = line[-i:]
        print(f"Unprocessed: {unprocessed}")
        match = DIGITS_RE.match(unprocessed)
        if match:
            print("Matched")
            print(match.groups())

            return match.group(1)


def extract_first(line):
    unprocessed = line
    while unprocessed:
        print(f"Unprocessed: {unprocessed}")
        match = DIGITS_RE.match(unprocessed)
        if match:
            print("Matched")
            print(match.groups())

            return match.group(1)
        else:
            print("Not Matched")
            unprocessed = unprocessed[1:]

    return None


def extract_first_last(line):
    first = DIGITS_LOOKUP[extract_first(line)]
    last = DIGITS_LOOKUP[extract_last(line)]
    return int(first + last)


def test_tokenize():
    test1 = tokenize_line("two1nine")
    assert len(test1) == 3
    assert test1[0] == "two"
    assert test1[-1] == "nine"

    test2 = tokenize_line("eightwothree")
    assert len(test2) == 2
    assert test2[0] == "eight"
    assert test2[-1] == "three"

    test3 = tokenize_line("abcone2threexyz")
    assert len(test3) == 3
    assert test3[0] == "one"
    assert test3[-1] == "three"

    test4 = tokenize_line("xtwone3four")
    assert len(test4) == 3
    assert test4[0] == "two"
    assert test4[-1] == "four"

    test5 = tokenize_line("4nineeightseven2")
    assert len(test5) == 5
    assert test5[0] == "4"
    assert test5[-1] == "2"

    test6 = tokenize_line("zoneight234")
    assert len(test6) == 4
    assert test6[0] == "one"
    assert test6[-1] == "4"

    test7 = tokenize_line("7pqrstsixteen")
    assert len(test7) == 2
    assert test7[0] == "7"
    assert test7[-1] == "six"


def test_extract_last():
    result = extract_last("8ninefivegzk7ftqbceightwogfv")
    assert result == "two"


if __name__ == "__main__":
    calib_file = "calibration-data.txt"
    calib_lines = []

    with open(calib_file, "r") as fin:
        calib_lines = fin.readlines()

    # test_tokenize()
    # test_extract_last()
    
    # process_line(calib_lines[0])
    line_values = [
        extract_first_last(line) for line in calib_lines
    ]
    print(sum(line_values))
