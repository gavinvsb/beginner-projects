# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True

    return s == s[::-1]

s1 = 'radkar'
print(s1)
print(solution(s1))

s2 = 'racecar'
print(s2)
print(solution(s2))
