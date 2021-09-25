
# 재귀 함수 동작 원리

'''
함수 동작 순서를 보시면,
recursive_function(i+1)이 호출된 시점에 
다시 recursive_function 함수가 시작됩니다.

print(i, '번째 재귀함수를 종료합니다.') 라인은 실행되기 전 상태구요.

함수를 만날 때 괄호 안으로 계속 들어가고,
함수가 종료될 때 나오면서 괄호를 닫는다고 생각하시면
이해하시기에 조금 쉬우실 것 같아요.

1 호출 (2 호출 (3 호출 (.... (99 호출 (100 호출 - return 만나서 호출 종료 문장 x) 
99 호출 종료)... 3 호출 종료 ) 2 호출 종료) 1 호출 종료

내부적으로 함수 호출이 스택으로 구현이되어있어서 가장 나중에 호출된 함수가 먼저 종료가 되면서 
하나씩 줄어드는 것 처럼 나옵니다. 

'''

# stack 와 같은 구조로 종료가되면 
# 가장 마지막에 호출되었된 함수부터 차례대로 종료되어 첫번째 호출했던 함수까지 종료함.

def recursive_function(i):

    if i == 10:
        return
    print(f'{i} 번째 재귀함수에서 , {i+1} 번째 재귀함수를 호출.')
    recursive_function(i+1)
    print(f'{i} 번째 재귀함수 종료')

# recursive_function(1)


def recursive_factorial(i):

    if i <= 1:
        return 1
    
    return i * recursive_factorial(i-1)


print(recursive_factorial(5))