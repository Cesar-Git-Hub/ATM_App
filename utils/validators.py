def validate_amount(amount: str) -> float:
    try:
        value = float(amount)
        if value > 0:
            return value
    except ValueError:
        pass
    return None

def validate_pin(pin: str) -> bool:
    return pin.isdigit() and len(pin) == 4
