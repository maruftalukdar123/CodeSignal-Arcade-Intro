def solution(s1, s2):

    # Split both inputs into its characters
    # If character a in s2 is in s1, then append to common array
    # Then remove that character from s1 to avoid double counting
    # Loop for all characters in s2

    s1,s2 = [*s1],[*s2]
    common = []
    
    for ch in s2:
        if ch in s1:
            common.append(ch)
            s1.remove(ch)

    return print(common)

s1 = "aabcc"
s2 = "adcaa"
solution(s1,s2)