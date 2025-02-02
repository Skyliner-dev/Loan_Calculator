import argparse
import math

parser = argparse.ArgumentParser(description = "Loan calculator")
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
def dp(prin, no, inter, mc):
    dm = (prin/no) + (inter * (prin - ((prin*(mc-1))/no)))
    return math.ceil(dm)
def overpay_annuity(pa, pe, pr):
    return math.ceil(pa*pe-pr)
if args.type == "diff":
    if args.periods is not None and args.interest is not None and args.principal is not None:
        n = float(args.periods)
        p = float(args.principal)
        i = float(args.interest) / (12 * 100)
        if n < 0 or p < 0 or i < 0:
            print('Incorrect parameters.')
        else:
            l = []
            for period in range(1,int(n+1)):
                pay = dp(prin=p, no=n, inter=i, mc=period)
                print(f"Month {period}: payment is {pay}")
                l.append(pay)
            overpay = int(sum(l)-p)
            print(f"Overpayment = {overpay}")
    else:
        print('Incorrect parameters.')
elif args.type == "annuity":
    if args.interest is not None:
        if args.payment is None:
            principal = float(args.principal)
            interest = float(args.interest)
            #periods is n
            n = float(args.periods)
            if principal < 0 or interest < 0 or n < 0:
                print('Incorrect parameters.')
            else:
                i = interest / (12 * 100)
                a = principal * ((i*(1+i)**n) / ((1+i)**n - 1))
                payment = math.ceil(a)
                print(f'Your monthly payment = {payment}!')
                print(f"Overpayment = {overpay_annuity(payment, n, principal)}")
        elif args.principal is None:
            # payment is a
            a = float(args.payment)
            n = float(args.periods)
            interest = float(args.interest)
            if a<0 or n<0 or interest<0:
                print('Incorrect parameters.')
            else:
                i = interest / (12 * 100)
                principal = a /((i*(1+i)**n) / ((1+i)**n - 1))
                print(f'Your loan principal = {math.floor(principal)}!')
                print(f"Overpayment = {overpay_annuity(a, n, principal)}")
        elif args.periods is None:
            a = float(args.payment)
            p = float(args.principal)
            interest = float(args.interest)
            if a<0 or p<0 or interest<0:
                print('Incorrect parameters.')
            else:
                i = interest / (12 * 100)
                x = (a/(a-i*p))
                base = 1+i
                n = math.ceil(math.log(x, base))
                year = round(n/12)
                months = round(n - (year * 12))
                if months == 0:
                   if year == 1:
                       print(f'It will take {year} year to repay this loan!')
                   else:
                       print(f'It will take {year} years to repay this loan!')
                else:
                    if months < 0:
                        print(f'It will take {year-1} years and {12 + months} months to repay this loan!')
                    else:
                        print(f'It will take {year} years and {months} months to repay this loan!')
                print(f"Overpayment = {overpay_annuity(a, n, p)}")
        else:
            print('Incorrect parameters.')
    else:
        print('Incorrect parameters.')
else:
    print('Incorrect parameters.')