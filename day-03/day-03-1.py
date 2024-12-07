
expected = {
  "m": "u",
  "u": "l",
  "l": "(",
  "(": "collecting_num1",
  "collecting_num1": ",",
  ",": "collecting_num2",
  "collecting_num2": ")"
}


def parse_multiplies(input):
  total = 0
  mode = None
  num1 = ""
  num2 = ""

  def reset():
    nonlocal mode, num1, num2
    mode = None
    num1 = ""
    num2 = ""

  for char in input:
    if char == "m":
      # Sequence start
      mode = "m"
    elif mode and char == expected[mode]:
      mode = char
      if mode == "(":
        mode = "collecting_num1"
      elif mode == ",":
        mode = "collecting_num2"
      elif mode == ")":
        total += int(num1) * int(num2)
        reset()
    elif mode == "collecting_num1" and char.isdigit():
      num1 += char
    elif mode == "collecting_num2" and char.isdigit():
      num2 += char
    else:
      reset()

  return total


if __name__ == "__main__":
  input = open('day-03.input').readline().strip()
  print(parse_multiplies(input))