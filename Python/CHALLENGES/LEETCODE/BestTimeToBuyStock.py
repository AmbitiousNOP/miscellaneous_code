"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

# price [7,1,5,3,6,4]

def maxProfit(price: list[int]) -> int:
    maxProfit = 0
    # sliding window 
    for i in range(len(price)):
        for j in range(len(price)):
            print(price[i], price[j])
    
#maxProfit([7,1,5,3,6,4])



def testing(price: list[int]) -> int:
    mp = 0

    # create a stack
    # pop from stack
    # 7-1, 7-5...
    # 1-5, 1-3...
    # etc
    
    # loop through the list
    # always going to be compare the 0th index
    while len(price) != 1:
        for i in price:
            if ((price[0] - i) < mp) and ((price[0]-i) < 0):
                mp = price[0]-i
        price.pop(0)
    print(abs(mp))
#testing([7,1,5,3,6,4])
#testing([7,6,4,3,1])


def neetcode(prices: list[int]) -> int:
    res = 0 
    l = 0

    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return res 

print(neetcode([7,1,5,3,6,4]))
