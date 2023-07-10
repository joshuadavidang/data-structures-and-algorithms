def max_profit(prices):
    if len(prices) < 2:
        return 0

    buy = 0
    sell = 0
    max_profit = 0

    while sell < len(prices):
        curr_profit = prices[sell] - prices[buy]
        if curr_profit > max_profit:
            max_profit = curr_profit
        elif prices[sell] < prices[buy]:
            buy = sell
        sell += 1

    return max_profit
