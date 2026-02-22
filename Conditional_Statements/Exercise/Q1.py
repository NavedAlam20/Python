def friends_in_trouble(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry) :
        return True
    else:
        return False
        
j_angry = True
s_angry = True
print(friends_in_trouble(j_angry, s_angry)) #True