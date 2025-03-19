n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    name, scores = data[0], list(map(float, data[1:]))
    students[name] = scores

query_name = input()
average = sum(students[query_name]) / len(students[query_name])
print(f"{average:.2f}")
