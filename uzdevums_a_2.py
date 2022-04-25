def convert(sum, rate):
    result = sum * rate
    print(sum, "EUR ir vienāds ar", result, "USD")

sum = int(input("Ievadi EUR summu : "))
convert(sum, 1.10)