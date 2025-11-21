def s_to_i(string):
    m, s = map(int, string.split(':'))
    return m*60+s

def i_to_s(integer):
    one = str(integer//60)
    two = str(integer%60)
    if len(one) < 2:
        one = '0'+one
    if len(two) < 2:
        two = '0'+two
    return one + ":" + two

def solution(video_len, pos, start, end, commands):
    pos = s_to_i(pos)
    video_len = s_to_i(video_len)
    start = s_to_i(start)
    end = s_to_i(end)
    for com in commands:
        if start <= pos <= end:
            pos = end
        if com == "next":
            pos += 10
            if video_len < pos:
                pos = video_len
        else:   # com == "prev"
            pos -= 10
            if pos < 0:
                pos = 0
        
    if start <= pos <= end:
        pos = end
        
    return i_to_s(pos)