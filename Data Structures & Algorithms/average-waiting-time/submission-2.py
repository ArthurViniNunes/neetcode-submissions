class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        total= 0
        
        for arrive, wait in customers:
            time = max(time, arrive)
            time += wait
            total += time - arrive

        return total / len(customers)