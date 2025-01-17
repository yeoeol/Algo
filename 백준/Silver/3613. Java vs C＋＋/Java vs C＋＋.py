def cpp_to_java(string):
    s = string.split('_')
    result = s[0]
    for i in range(1, len(s)):
        result += s[i].capitalize()
    return result


def java_to_cpp(string):
    result = ""
    for s in string:
        if s.isupper():
            result += '_'+s.lower()
        else:
            result += s
    return result


def error_check(string):
    cap_flag = False
    under_flag = False
    if string[-1] == '_' or string[0] == '_' or string[0].isupper():
        return False
    for i in range(len(string)):
        s = string[i]
        if s.isupper():
            cap_flag = True
        elif s == '_':
            under_flag = True
        if cap_flag and under_flag:
            return False

        if not s.isalpha():
            if s != '_':
                return False
            if s == '_' and (string[i-1] == '_' or string[i+1] == '_'):
                return False

    return True

var = input()
if error_check(var):
    if var.count('_') > 0: # C++ 형식
        # Java 형식으로 변환
        print(cpp_to_java(var))
    else:   # Java 형식
        # C++ 형식으로 변환
        print(java_to_cpp(var))
else:
    print("Error!")

