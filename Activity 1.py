def fun1(bill,tip):
    t=(bill*(1+0.01*tip))
    t=round(t,2)
    print("You will pay: ",t)
fun1(100,60)