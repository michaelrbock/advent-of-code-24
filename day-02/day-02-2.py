
def safe_report(report):
  if report[0] == report[1]:
    return 0
  direction = "inc" if report[0] < report[1] else "dec"
  for i in range(len(report) - 1):
    if abs(report[i] - report[i+1]) > 3:
      return 0
    if direction == "inc" and report[i+1] <= report[i]:
      return 0
    elif direction == "dec" and report[i+1] >= report[i]:
      return 0
  return 1

def count_safe_reports(raw_lines):
  safe_reports = 0
  for raw_line in raw_lines:
    report = [int(x) for x in raw_line.split()]
    any_safe = 0
    for i in range(len(report)):
      if safe_report(report[:i] + report[i+1:]):
        any_safe = 1
    safe_reports += any_safe
  return safe_reports

if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-02.input')]
  print(count_safe_reports(lines))
