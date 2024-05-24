def mark(a,b):
    if a >= 90:
        print(f"you got A grade {b}")
    elif a >= 80:
        print(f"you got B grade {b} ")
    else:
        print(f"you got C grade {b} ")

while True:
        h=input("enter your subject name:")
        g = int(input("Enter your mark: "))
        mark(g,h)
   
