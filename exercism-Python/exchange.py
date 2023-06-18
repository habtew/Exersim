"""
Instructions
Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency calculator for him. Here are his specifications for the app:

Task 1
Estimate value after exchange

Task 2
Calculate currency left after an exchange

Task 3
Calculate value of bills

Task 4
Calculate number of bills

Task 5
Calculate leftover after exchanging into bills

Task 6
Calculate value after exchange
"""

def exchange_money(budget, exchange_rate):
    return budget/exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination*number_of_bills

def get_number_of_bills(budget, denomination):
    return int(budget/denomination )

def get_leftover_of_bills(budget, denomination):
    return budget%denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    new_rate = exchange_rate + (exchange_rate * (spread / 100))
    new_currency = exchange_money(budget, new_rate)
    return get_number_of_bills(new_currency, denomination)*denomination
