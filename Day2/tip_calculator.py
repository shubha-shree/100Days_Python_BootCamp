def calc_split(total_bill, tip, people):
    split = (total_bill+(total_bill*(tip/100)))/people
    return round(split,2)




def main():
    print("Welcome to the tip calculator!")
    total_bill = float(input('What was the total bill? ').lstrip('$'))
    tip = int(input('How much tip would you like to give(in percentage)? 10, 12, or 15? '))
    people = int(input('How many people to split the bill? '))
    split = calc_split(total_bill, tip, people)
    print(f"Each person should pay: ${split}")

main()