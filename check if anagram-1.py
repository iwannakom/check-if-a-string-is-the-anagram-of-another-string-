def isAnagram(self, s: str, t: str) -> bool:
        
    if len(s) != len(t):
        return False

    s_count, t_count = {} ,{}

    for i in range (len(s)):
        s_count = 1+ s_count.get(s[i],0)
        t_count = 1+ t_count.get(s[i],0)

    return s_count == t_count

        
        
