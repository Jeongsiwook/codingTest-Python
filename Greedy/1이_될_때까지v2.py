# N, M을 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
  # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 뺴기
  target = (n // k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
# N이 0이 될때까지 계산해버리기 때문에 마지막에 result + 1 추가로 된 값을 
result += (n - 1)
print(result)
