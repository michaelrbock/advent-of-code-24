
def parse():
  lines = [line.rstrip('\n') for line in open('day-01.input')]
  list1, list2 = list(), list()
  for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)
  return list1, list2

def calculate_distance(list1, list2):
  sorted_list1, sorted_list2 = sorted(list1), sorted(list2)
  total_dist = 0
  for i in range(len(sorted_list1)):
    num1, num2 = sorted_list1[i], sorted_list2[i]
    total_dist += abs(num1 - num2)
  return total_dist

if __name__ == '__main__':
  list1, list2 = parse()
  print(calculate_distance(list1, list2))
