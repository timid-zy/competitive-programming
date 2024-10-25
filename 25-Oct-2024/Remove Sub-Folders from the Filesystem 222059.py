# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # folder.sort(key=lambda x: x.count("/"))
        # seen = set()
        # for directory in folder:
        #     valid = True
        #     for i in range(1, len(directory)):
        #         if directory[i] == "/" and directory[:i] in seen:
        #             valid = False
        #             break
            
        #     if valid:
        #         seen.add(directory)
        
        # return list(seen)

        def add(word, root):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c]
            
            curr.is_end = True
            
        def find(word, root):
            curr = root
            for c in word:
                if c not in curr.children:
                    return False
                
                curr = curr.children[c]
                if curr.is_end:
                    return True
            
            return False

        root = TrieNode()
        folder.sort(key=lambda x: x.count("/"))
        ans = []
        for directory in folder:
            directory += "/"
            if not find(directory, root):
                ans.append(directory)
                add(directory, root)
        
        return list(map(lambda x: x[:-1], ans))
        
        