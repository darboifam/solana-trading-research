
def calculate_net_return(entry_price, exit_price, fee=0.01):
    """Calculate trade return after entry and exit fees."""
    if entry_price <= 0 or exit_price < 0:
        raise ValueError("Invalid trade prices")

    gross_multiple = exit_price / entry_price
    net_multiple = gross_multiple * (1 - fee) ** 2

    return (net_multiple - 1) * 100


if __name__ == "__main__":
    result = calculate_net_return(100, 115)
    print(f"Net return: {result:.2f}%")
