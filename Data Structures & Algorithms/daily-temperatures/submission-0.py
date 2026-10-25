class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        days_temp = []
        days_ind = []
        for i, t in enumerate(temperatures):
            while days_temp:
                if t > days_temp[-1]:
                    days_temp.pop()
                    day_ind = days_ind.pop()
                    result[day_ind] = i - day_ind
                else:
                    break
            days_temp.append(t)
            days_ind.append(i)
        return result