cnt = 0
while True:
    try:
        i = input()
        if not i:
            break
        cnt += len(i)
    except:
        break
print(f"글자수 {cnt}글자")
