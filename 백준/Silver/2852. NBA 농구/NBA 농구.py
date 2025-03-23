# 각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램
# 농구 경기는 정확히 48분동안 진행

# 분을 초로 환산하는 함수
def get_seconds(t):
    m, s = t.split(':')
    return int(m)*60 + int(s)

def get_HH_MM(seconds):
    h = str(seconds//60)
    if len(h) == 1:
        h = '0'+h
    m = str(seconds%60)
    if len(m) == 1:
        m = '0'+m
    return h+':'+m

n = int(input())
goal = [0, 0, 0] # 1이 골을 넣은 개수
times = [0, 0, 0] # 이기고 있던 시간

prev = 0
for _ in range(n):
    team, time = input().split()
    # 분을 초로 환산
    cur = get_seconds(time)
    # one이 two보다 크다면 time - prev(이전 골 시간) 만큼 더해주기
    if goal[1] > goal[2]:
        times[1] += cur - prev
    # two가 one보다 크다면 time - prev 만큼 더해주기
    elif goal[1] < goal[2]:
        times[2] += cur-prev
    # 두 팀의 골 개수가 같다면 넘기기
    # else:
    prev = cur

    goal[int(team)] += 1

if goal[1] > goal[2]:
    times[1] += 2880 - prev
# two가 one보다 크다면 time - prev 만큼 더해주기
elif goal[1] < goal[2]:
    times[2] += 2880 - prev

print(get_HH_MM(times[1]))
print(get_HH_MM(times[2]))