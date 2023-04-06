def check_str(s: str):
    s = ''.join(filter(str.isalnum, s)).lower()

    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
