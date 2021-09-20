n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때 까지 빼기

    #target은 가장 가까운 n이  k로 나눠떨어지는 값을 찾아줌!
    target = (n//k) * k
    
    result += (n - target)
    print(result)
    n = target
    if n<k:
        break
    result += 1

    n //= k
    print("-------------------------------------")

result += (n-1)
print("최종: " + str(result))