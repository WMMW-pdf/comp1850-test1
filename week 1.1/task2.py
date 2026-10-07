try:
    eachmonth=int(input("Please entry number"))
    peryear= eachmonth*12
    interest= peryear*0.008
    total=eachmonth+interest
    print("interest=",interest)
    print("total=",total)
except:
    print("invalid amount")