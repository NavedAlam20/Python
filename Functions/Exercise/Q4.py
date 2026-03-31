usd = float(input("Enter USD:"))

def curr_converter(usd):
    inr = usd * 94.04
    return inr
    
print(f'{usd} USD = {curr_converter(usd)} INR')