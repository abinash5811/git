#Q2 'R' and 'S' are two brothers who started their journey separately with 25000 Rs and 15000 Rs. 
# However, R invested the money in 2 yr Fixed deposits that gave 7% return compounded annually . 
# Whereas S invested the money in Equity Market that compounded at 12% return . After 2 years , 
# who has more money in hand and by how much ?

#ci formula= p*(1+r/n)**nt ;where- p=principal, r= rate of int, n= no of compundings in a yr, t= total time period
p_of_R= 25000
P_of_S= 15000
fd_rr=0.07
equity_rr=0.12
no_of_compounding_in_yr=1
time_period= 2

total_amt_of_R= p_of_R*(1+(fd_rr/no_of_compounding_in_yr))**(no_of_compounding_in_yr*time_period)
total_amt_of_S= P_of_S*(1+(equity_rr/no_of_compounding_in_yr))**(no_of_compounding_in_yr*time_period)

print("total gain of R is=",total_amt_of_R)
print("total gain of S is=",total_amt_of_S)

print("difference between R & S is=",total_amt_of_R-total_amt_of_S)

if(total_amt_of_R>total_amt_of_S):
   print("R has more money in hand")
else:
    print("s has more money in hand")




