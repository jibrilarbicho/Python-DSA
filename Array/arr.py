comments=["jimma","jim","jimer","james"]
for i in comments:
    print(i)
total=[i for i in comments if "jim" in i or "james" in i]
# print(len(total))
print(len(total))