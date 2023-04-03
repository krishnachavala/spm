def genotp():
    u_c=[chr(i)for i in range(ord(ord()'A'),ord('Z')+1)]
    l_c=[chr(i)for i in range(ord(ord()'a'),ord('z')+1)]
    otp=''
    for i in range(2):
        otp+=randam.choice(u_c)
        otp+=random.randint(0,9)
        otp+=random.choice(1_c)
    return otp
    

    
