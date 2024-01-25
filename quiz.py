def f(x):
    d =0
    while x> 1:
        x,d = (x/2), d+1 

    return d

def h(x):
    s =0 
    for i in range(2,x):
        if x%i ==0:
            s+=i
    
    return s

def g(a,b):
    res =0

    while a >= b :
        (res,a) = res+1 ,a/b

    return res


if __name__ == "__main__":
    print(f"{f(27182818)}")
    print(f"Second Ques -{h(60)} , {h(45)} , {h(60) - h(45)}")

    for i in range(2,7):
        print(f" for {i} function returns { g(375,i)}")
