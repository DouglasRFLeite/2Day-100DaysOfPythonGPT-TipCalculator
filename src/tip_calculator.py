def tip_calculator_console():
    print("Welcom to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    percentage = int(input("What percentage tip would you like to give? ")) / 100
    num_people = int(input("How many people to split the bill? "))

    payment_per_person = calculate_tip(bill, percentage, num_people)

    print(f"Each person should pay: $ {payment_per_person}")

def calculate_tip(bill, percentage, num_people):
    percentage_multiplier = 1+percentage
    total_bill = bill * percentage_multiplier
    bill_per_person = total_bill / num_people
    rounded_value = round(bill_per_person, 2)
    return rounded_value

    

    


if __name__ == "__main__":
    tip_calculator_console()