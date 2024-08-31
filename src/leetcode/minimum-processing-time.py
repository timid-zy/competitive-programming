class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sorted_time = sorted(processorTime)
        sorted_tasks = sorted(tasks)

        curr_sum = 0
        min_time = None
        curr_processor = len(sorted_time) - 1
        i = 0
        while i < len(tasks):
            curr_max = sorted_time[curr_processor] + max(sorted_tasks[i:i+4])
            if min_time is None:
                min_time = curr_max
            else:
                min_time = max(min_time, curr_max)
            curr_processor -= 1
            i += 4
        return min_time