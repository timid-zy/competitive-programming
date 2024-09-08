class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pf, nf = set(positive_feedback), set(negative_feedback)
        dct = defaultdict(int)
        for i in range(len(report)):
            for word in report[i].split(' '):
                diff = 0
                if word in pf: diff = 3
                if word in nf: diff = -1
                dct[student_id[i]] += diff
        
        arr = [(-v, k) for k, v in dct.items()]
        arr.sort()
        return list(map(lambda x: x[1], arr))[:k]
