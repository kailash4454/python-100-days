student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# calculating the sum of numbers in a list
# print(sum(student_scores))

# total_score = sum(student_scores)
# print(total_score)
#
# traditional way to calculate
# total = 0
# for score in student_scores:
#     total += score
#
# print(total)

# finding maximum in a list
print(max(student_scores))

# Traditional way to calculate
# maximum = student_scores[0]
maximum = 0
for num in student_scores:
    if num > maximum:
        maximum = num

print(maximum)


# finding minimum in a list
print(min(student_scores))

# Traditional way to calculate

min_score = student_scores[0]
for score in student_scores:
    if score < min_score:
        min_score = score

print(min_score)

