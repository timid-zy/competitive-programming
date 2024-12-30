# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[recipes[i]].append(ing)
                graph[ing].append(recipes[i])
                indeg[recipes[i]] += 1
        
        queue = deque(supplies)
        res = []
        while queue:
            curr = queue.popleft()
            for nb in graph[curr]:
                if indeg[nb] == 1:
                    res.append(nb)
                    queue.append(nb)
                
                indeg[nb] -= 1

        return res
        
