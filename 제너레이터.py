# 제너레이터 함수
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 제너레이터 사용
fib = fibonacci(5)
for num in fib:
    print(num)  # 출력: 0 1 1 2 3
