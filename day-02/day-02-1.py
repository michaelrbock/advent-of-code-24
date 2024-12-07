
def count_safe_reports(raw_lines):
  safe_reports = 0
  for raw_line in raw_lines:
    report = [int(x) for x in raw_line.split()]
    if report[0] == report[1]:
      continue
    direction = "inc" if report[0] < report[1] else "dec"
    safe = 1
    for i in range(len(report) - 1):
      if abs(report[i] - report[i+1]) > 3:
        safe = 0
      if direction == "inc" and report[i+1] <= report[i]:
        safe = 0
      elif direction == "dec" and report[i+1] >= report[i]:
        safe = 0
    safe_reports += safe
  return safe_reports

if __name__ == '__main__':
  lines = [line.rstrip('\n') for line in open('day-02.input')]
  print(count_safe_reports(lines))
