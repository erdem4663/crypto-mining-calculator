def calculate_profit(hash_rate, power_cost, coin="bitcoin", days=30):
    # Simplified calculation for demo purposes
    if coin == "bitcoin":
        reward_per_day = 0.0005
        coin_price = 30000
    elif coin == "ethereum":
        reward_per_day = 0.01
        coin_price = 2000
    else:
        reward_per_day = 0
        coin_price = 0

    profit = (reward_per_day * days * coin_price) - (power_cost * days)
    return profit

if __name__ == "__main__":
    profit = calculate_profit(hash_rate=100, power_cost=5, coin="bitcoin")
    print("Estimated profit:", profit)
