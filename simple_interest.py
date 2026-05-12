"""Simple Interest Calculator."""


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """Return simple interest for a given principal, annual rate (%), and time in years."""
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")
    return (principal * rate * time) / 100


def main() -> None:
    print("Simple Interest Calculator")
    print("--------------------------")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time period (years): "))

    interest = calculate_simple_interest(principal, rate, time)
    total = principal + interest

    print(f"\nSimple Interest: {interest:.2f}")
    print(f"Total Amount:    {total:.2f}")


if __name__ == "__main__":
    main()
