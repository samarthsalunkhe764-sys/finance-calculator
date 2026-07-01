def emi(principal, annual_rate, years):
    m=annual_rate/1200
    n=years*12
    return principal*m*(1+m)**n/((1+m)**n-1)
