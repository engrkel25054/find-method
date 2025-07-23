# Program specification
"""
Use find to implement a function satisfying the specification
"""

def find_last(s, sub):
    """
    Checks if substring occurs in the given string.
    :param s: non-empty string
    :param sub: non-empty string
    :return: Returns the index of the last occurrence of sub in s; else Returns None if sub does not occur in s
    """
    for i in range(len(sub)):
        for j in range(len(s)):
            if sub[i] == s[j]:
                return j
    return None


s = "This is a beautiful day to learn Python."
sub = "Python"
print(find_last(s, sub))
print(find_last(s, "learn"))
print(find_last(s, "xz"))