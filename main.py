
# Electricity Bill Calculator
# Student: V. Janita
# USN: 01FE25BCA213
# Division: D

def units_cost(units):
    if units < 0:
        raise ValueError("Units cannot be negative")

    if units <= 100:
        return units * 4.50
    elif units <= 200:
        return (100 * 4.50) + ((units - 100) * 6)
    else:
        return (100 * 4.50) + (100 * 6) + ((units - 200) * 7.50)


def fixed_charge():
    return 50


def total_bill(units):
    return units_cost(units) + fixed_charge()


# New feature added in feature branch
def bill_category(amount):
    if amount <= 500:
        return "Low Bill"
    elif amount <= 1000:
        return "Medium Bill"
    else:
        return "High Bill"


def main():
    print("========================================")
    print("       ELECTRICITY BILL CALCULATOR")
    print("========================================")

    try:
        units = float(input("Enter electricity units consumed: "))

        if units < 0:
            print("Error: Units cannot be negative.")
            return

        energy = units_cost(units)
        fixed = fixed_charge()
        total = total_bill(units)
        category = bill_category(total)

        print("\n========== BILL DETAILS ================")
        print("Student Name: V. Janita")
        print("USN: 01FE25BCA213")
        print("Units Consumed:", units)
        print("Energy Charge: Rs.", energy)
        print("Fixed Charge: Rs.", fixed)
        print("----------------------------------------")
        print("Total Electricity Bill: Rs.", total)
        print("Bill Category:", category)
        print("========================================")
        print("Thank you!")

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
