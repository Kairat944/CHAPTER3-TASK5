s1 = "kit"
s2 = "hello kit"
def opa(s1, s2):
    result = any(elem in s1 for elem in s2)
    if result:
        return "YES"
    else:
        return "NO"

ups = opa(s1, s2)
print(ups)