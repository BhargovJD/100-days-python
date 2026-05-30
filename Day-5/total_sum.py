score = [10, 20, 30, 40, 50]

total_score = 0

for x in score:
    total_score = total_score + x

print("Total score1:", total_score)


# sum
total_score = sum(score)
print("Total score2:", total_score)

# max
max_score = max(score)
print("Max score:", max_score)

# max primitive way
score = [10, 20, 30, 40, 50]
max_score = score[0]
for x in score:
    if x > max_score:
        max_score = x 

print("Max score (primitive way):", max_score)
