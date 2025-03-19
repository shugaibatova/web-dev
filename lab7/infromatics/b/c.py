num = input()
student_answer = input()

is_symmetric = num == num[::-1]

if (is_symmetric and student_answer == "1") or (not is_symmetric and student_answer == "-1"):
    print("YES")
else:
    print("NO")
