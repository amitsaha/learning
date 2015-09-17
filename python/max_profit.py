'''
Given an array of stock prices in an array where an
index represents the time of the price, find the maximum
profit that can be made on the day
'''
def find_best_profit(stock_prices_yesterday):
    max_profit = -1
    # O(n^2)
    for time, price in enumerate(stock_prices_yesterday):
        if price:            
            for next_time in range(time +1, len(stock_prices_yesterday)):
                if stock_prices_yesterday[next_time]:
                    profit = stock_prices_yesterday[next_time] - price                    
                    if profit > max_profit:
                        max_profit = profit
    result1 = max_profit
    # O(n)
    min_price = stock_prices_yesterday[0]
    for time, price in enumerate(stock_prices_yesterday):
        if price:
            if price-min_price > max_profit:
                max_profit = price-min_price
            if price < min_price:
                min_price = price

    result2 = max_profit
    
    assert result1 == result2
    return max_profit

print(find_best_profit([500, 400, 600, 1000, 800]))
                
            
