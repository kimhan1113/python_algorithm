
# 람다 사용법!!
lambda_ = (lambda a, b : a+b)(5,7)
# print(lambda_ )


# 람다 주로사용!!
array = [('홍길동' , 50),('김길동', 75),('아무개', 30), ('김철수', 25)]
sorted_array = sorted(array, key=lambda x: x[1])
# print(sorted_array)



# 람다 + map함수 같이 사용!!
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

result = map(lambda a,b : a+b, list1, list2)
print(list(result))