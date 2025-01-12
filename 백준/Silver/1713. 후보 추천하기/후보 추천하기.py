n = int(input())
m = int(input())
lst = list(map(int, input().split()))

frame = []
vote = {}
time = {}

if n == 1:
    print(lst[-1])
    exit(0)

for t, v in enumerate(lst):
    if v in frame:
        vote[v] += 1
        continue
    if len(frame) < n:
        frame.append(v)
        vote[v] = 1
        time[v] = t
    else:
        m_vote = min(vote[s] for s in frame)
        m_students = [s for s in frame if vote[s] == m_vote]

        old = -1
        if len(m_students) >= 2:
            m_students.sort(key=lambda x : time[x])
            old = m_students[0]
        else:
            old = m_students[0]

        frame.remove(old)
        del vote[old]
        del time[old]

        frame.append(v)
        vote[v] = 1
        time[v] = t
print(*sorted(frame))
