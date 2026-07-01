from calculators.emi import emi
from calculators.sip import future_value
from calculators.gst import add_gst
from calculators.fd import maturity

def menu():
    while True:
        print("\nFinance Calculators")
        print("1. EMI")
        print("2. SIP")
        print("3. GST")
        print("4. Fixed Deposit")
        print("5. Exit")
        c=input("Choice: ")
        try:
            if c=="1":
                p=float(input("Principal: "))
                r=float(input("Annual Rate (%): "))
                y=int(input("Years: "))
                print(f"Monthly EMI: {emi(p,r,y):.2f}")
            elif c=="2":
                m=float(input("Monthly Investment: "))
                r=float(input("Annual Return (%): "))
                y=int(input("Years: "))
                print(f"Future Value: {future_value(m,r,y):.2f}")
            elif c=="3":
                a=float(input("Amount: "))
                g=float(input("GST %: "))
                print(f"Total: {add_gst(a,g):.2f}")
            elif c=="4":
                p=float(input("Deposit: "))
                r=float(input("Annual Rate (%): "))
                y=int(input("Years: "))
                print(f"Maturity: {maturity(p,r,y):.2f}")
            elif c=="5":
                break
        except ValueError:
            print("Invalid input")
if __name__=="__main__":
    menu()
