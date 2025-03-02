comments=["jimma","jim","jimer","james"]
for i in comments:
    print(i)
total=(1 for i in comments if "jim" in i or "james" in i) #Generator: Only keeps track of the current state to produce the next value.
# print(len(total))
print(sum(total))
