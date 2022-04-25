def convert (sum, rate):
    return round(sum * rate, 2)

EUR = int(input("ievadi EUR: "))
reit = int(input("ievadi rate: "))

print("USD ir: ", convert(EUR, reit))