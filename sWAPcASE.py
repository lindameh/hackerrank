def swap_case(s):
    result=""
    for i in s:
        if 65<=ord(i)<=90:
            result+=chr(ord(i)+32)
        elif 97<=ord(i)<=122:
            result+=chr(ord(i)-32)
        else:
            result+=i
    return result
