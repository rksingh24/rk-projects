#currency converter 
#top 8 currenccy holder
def currency():
     print("welcome to th currency conveter ")
     print("convert  currency  to INR ")
     USD=74.10
     EUR=87.94
     JPY=0.71
     GBP=98.24
     CHF=81.41
     CAD=56.74
     ZAR=4.81
     
     print("USD-",USD,"\nEUR-",EUR,"\nJPY-",JPY,"\nGBP-",GBP,"\nCHF-",CHF,"\nCAD-",CAD,"\nZAR-",ZAR,"\n",)
     
     inr=float(input("Enter Amount\t"))
     cur=input("Enter Currency --\t")
     
     if cur=='USD':
         convert=inr*USD
         print("convertion of currency USD to INR--\t",convert)
    
     elif cur=='EUR':
         convert=inr*EUR
         print("convertion of currency  EUR to INR--\t",convert)
    
     elif cur=='JPY':
         convert=inr*JPY
         print("convertion of currency  JPY to INR--\t",convert)
     elif cur=='GBP':
         convert=inr*GBP
         print("convertion of currency  GBP to INR--\t",convert)
     elif cur=='CHF':
         convert=inr*CHF
         print("convertion of currency  CHF to INR--\t",convert)
     elif cur=='CAD':
         convert=inr*CAD
         print("convertion of currency  CAD to INR--\t",convert)
     elif cur=='ZAR':
         convert=inr*ZAR
         print("convertion of currency  ZAR to INR--\t",convert)
     else:
         print("enter one of this currency")
currency()
    