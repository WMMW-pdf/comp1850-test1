try:
    score=int(input("please entry your score (number range between0-100):"))
    if 70<=score<=100:
        print("Distinction ")
    elif  40 <= score <=69:
        print("pass")
    elif 0<=score<=39:
        print("fail")
    else:
        print("please entry number range  between0-100")
except:
    print("error")
