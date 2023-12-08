

# Read in file in lines
# Process each line to find the first and last digits
# Sum the configuration value of the line

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def process_line(line):
    processed = [x for x in line if x in DIGITS]
    first_digit = processed[0]
    last_digit = processed[-1]
    return int(first_digit + last_digit)


if __name__ == "__main__":
    conf_file = "calibration-data.txt"
    config_lines = []

    with open(conf_file, "r") as fin:
        config_lines = fin.readlines()

    print(len(config_lines))
    calibration_values = [process_line(line) for line in config_lines]
    print(sum(calibration_values))



