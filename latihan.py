class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        
        for price in prices:
            buy1 = max(buy1, -price)           # beli pertama
            sell1 = max(sell1, buy1 + price)   # jual pertama
            buy2 = max(buy2, sell1 - price)    # beli kedua
            sell2 = max(sell2, buy2 + price)   # jual kedua
        
        return sell2
