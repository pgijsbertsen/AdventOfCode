import os

# Get the input
input = open(os.path.dirname(__file__) + "/inputs/input.txt", "r").readlines()

# Do the magic
def get_direction(prev_level: int, level: int) -> str | None:
    if level < prev_level:
        return "desc"
    elif level > prev_level:
        return "asc"
    else:
        return None

def get_safe_reports(reports: list[str]) -> int:
    safe_reports = 0

    for report in reports:
        prev_level = None
        report_safe = True
        direction = None

        for level in report.split(" "):
            level = level.rstrip("\n")

            if prev_level is None:
                prev_level = level
                continue
            
            if direction is None:
                direction = get_direction(int(prev_level), int(level))

            if (direction == "asc" and int(level) < int(prev_level)) or (direction == "desc" and int(level) > int(prev_level)):
                report_safe = False
                break

            difference = abs(int(level) - int(prev_level))
             
            if difference == 0 or difference > 3:
                report_safe = False

            prev_level = level

        if report_safe:
            safe_reports += 1

    return safe_reports

# Return the magic
print("Part One: " + str(get_safe_reports(input)))
