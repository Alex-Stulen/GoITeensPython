
account_a = 100
print(f"{account_a=}")

account_b = 80
print(f"{account_b=}")


def create_payment(price: int):
    global account_a, account_b

    has_error = False

    account_a -= price

    if not has_error:
        account_b += price
        print(f"було відправлено від ac1 до ac2 {price}грн")
    else:
        print("сталася помилка")
        account_a += price


create_payment(30)
print(f"{account_a=}")
print(f"{account_b=}")
