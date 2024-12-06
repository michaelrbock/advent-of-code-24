from collections import Counter

def parse():
  lines = [line.rstrip('\n') for line in open('day-01.input')]
  list1, list2 = list(), list()
  for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)
  return list1, list2

def calculate_similarity_score(list1, list2):
  counts = Counter(list2)
  similarity_score = 0
  for num in list1:
    similarity_score += num * counts[num]
  return similarity_score

if __name__ == '__main__':
  list1, list2 = parse()
  print(calculate_similarity_score(list1, list2))
