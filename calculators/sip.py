def future_value(monthly, annual_rate, years):
    r=annual_rate/1200
    n=years*12
    return monthly*(((1+r)**n-1)/r)*(1+r)
