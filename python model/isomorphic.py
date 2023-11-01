def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping ={}
    mapped_chars =set()
    
  
            mapping[s[i]] = t[i]
            mapped_chars.add(t[i])

    return True
s = "egg"
t = "add"
result = is_isomorphic(s, t)
print(result)


