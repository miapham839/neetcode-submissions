class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each couse to its prereqs
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            # Base case: crs already exist in current dfs path --> Cycle detected
            if crs in visiting:
                return False
            # Base case: all prereq courses are finishable
            if preMap[crs] == []:
                return True
            
            # Add crs to current DFS path
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # Remove from current path --> upper layer node checks its other prereq
            visiting.remove(crs)
            # So whenever we meet this node again we don't need to go through the above loop anymore
            preMap[crs] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

'''
Notes:
- Graph as an adjacency list
- How on earth do I come up with this version of dfs, especially line 25-27
'''
        