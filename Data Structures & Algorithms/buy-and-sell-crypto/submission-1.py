class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        buy_day = 0
        sell_day = 1

        while buy_day < sell_day and sell_day < len(prices):
            # if buy price > sell price
            if prices[buy_day] > prices[sell_day]:
                buy_day += 1
                if buy_day == sell_day:
                    sell_day += 1
                continue
            # if sell price > buy price
            if prices[sell_day] > prices[buy_day]:
                # if current profit > max profit
                if prices[sell_day] - prices[buy_day] > max_profit:
                    max_profit = prices[sell_day] - prices[buy_day]
                sell_day += 1
            # buy price == sell price
            else:
                if sell_day == len(prices)-1:
                    buy_day += 1
                else:
                    sell_day += 1
        
        return max_profit
            
            
        