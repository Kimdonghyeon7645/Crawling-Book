cnt = 0
while True:
    try:
        i = input()
        if not i:
            break
        cnt += len(i)
        print(cnt)
    except:
        break
print(f"\n글자수 {cnt}글자")
