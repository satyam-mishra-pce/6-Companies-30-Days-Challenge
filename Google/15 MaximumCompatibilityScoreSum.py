class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])

        def getcompatibilityscore(student_idx, mentor_idx):
            score = 0
            for s, m in zip(students[student_idx], mentors[mentor_idx]):
                score += not(s ^ m)
            return score

        def recursion(student_idx, used_mentors):
            if student_idx >= m:
                return 0
            
            maxcompatibility = 0
            for i in range(m):
                if i not in used_mentors:
                    used_mentors.add(i)
                    score = getcompatibilityscore(student_idx, i) + recursion(student_idx + 1, used_mentors)
                    maxcompatibility = max(maxcompatibility, score)
                    used_mentors.remove(i)
            
            return maxcompatibility
        
        return recursion(0, set())
