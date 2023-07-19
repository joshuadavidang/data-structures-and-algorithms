def maxProfit(prices):
    totalProfit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            currentProfit = prices[i] - prices[i - 1]
            totalProfit += currentProfit

    return totalProfit
