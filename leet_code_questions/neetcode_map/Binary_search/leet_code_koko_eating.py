"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

"""

#test cases


piles0 = [3,6,7,11]
h0 = 8
out0 = 4


piles1 = [30,11,23,4,20]
h1 = 5
out1 = 30

piles2 = [30,11,23,4,20]
h2 = 6
out2 = 23


class Solution:
	def minEatingSpeed(self, piles: list, h: int) -> int:
		"""
		The function finds the banana eaten by the koko at the min rate to finish all the bananas
		Args:
			piles: The pile of the bananas 
			h: The time at which the gurads will be back
		Return:
			eating_speed : The min speed at which koko should eat banana
		"""
		l, r = 1, max(piles)
		 
		while l<=r:

			total = 0
			mid = (l+r) // 2

			for i in piles:

				total = round(i//mid) + total

			if total > h:
				right = mid - 1

			elif total < h:
				left = mid + 1
			

		return total

if __name__ == "__main__":
	sol = Solution()
	res = sol.minEatingSpeed(piles0,h0)
	print(res)