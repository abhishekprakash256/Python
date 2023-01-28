"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. 
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

"""
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
out = 3 


class Solution:
    def carFleet(self, target: int, position: list, speed: list) -> int:
        """
        The function is to solve the car fleet problem
        Args:
            target: (int) The target that to reach 
            position: (list) The list of the position of the car
            speed: (ist) The list of the speed of the car
        Return:
            out: (int) The car meeting point  
        """
        combined_stack = []
        lst_pos_speed = []
        
        #append the value in the list 
        for p,s in zip(position,speed):
            lst_pos_speed.append([p,s])
        
        #sort the list as per position
        lst_pos_speed.sort()
        
        for p,s in reversed(lst_pos_speed):
            
            combined_stack.append((target-p)/s)
            if len(combined_stack) >=2 and combined_stack[len(combined_stack)-1] <= combined_stack[len(combined_stack)-2]:
                combined_stack.pop()          
        
        return len(combined_stack)


sol = Solution()
res = sol.carFleet(target,position,speed)

print(res)
