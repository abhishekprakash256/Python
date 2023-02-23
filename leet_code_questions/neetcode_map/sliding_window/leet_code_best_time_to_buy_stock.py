"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

#test cases
prices = [7,1,5,3,6,4]

prices1 = [2,1,2,1,0,1,2]



class Solution:
	def maxProfit(self,prices:list)->int:
		"""
		The function to find the max profit in the from list after selling the stocks
		Args:
			prices: the list of the stock prices
		Return:
			maxProfit: the max profit can be made by selling the stocks
		"""

		#the left pointer with sliding window 
		l = 0
		r = l + 1
		length = len(prices) - 1

		#the temp profit
		max_profit = 0

		while r <= length:

			#calculate the value of the profit 

			if prices[l] > prices[r]:
				l=r

			elif prices[l] < prices[r]:
				temp_profit = prices[r] - prices[l]
				max_profit = max(temp_profit,max_profit)

			r+=1

		return max_profit


sol = Solution()
res = sol.maxProfit(prices1)
print(res)