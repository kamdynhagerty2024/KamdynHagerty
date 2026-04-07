#Name: Section11.22problem10
#Purpose:  Lists
#Author: KamdynHagerty
#Created: 4/7/26


def replace(s, old, new):
    result = ""
    i = 0
    while i <= len(s) - len(old):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    result += s[i:] 
    return result
