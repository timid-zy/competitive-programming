# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserPage:
    def __init__(self, page, prev=None, nextN=None):
        self.page = page
        self.prev = prev
        self.next = nextN

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = BrowserPage(homepage)
        

    def visit(self, url: str) -> None:
        new_page = BrowserPage(url, self.homepage)
        self.homepage.next = new_page
        self.homepage = new_page

    def back(self, steps: int) -> str:
        i = 0
        curr = self.homepage
        if curr is None:
            return

        while i < steps and curr.prev:
            curr = curr.prev
            i += 1

        self.homepage = curr
        return self.homepage.page


    def forward(self, steps: int) -> str:
        i = 0
        curr = self.homepage
        if curr is None:
            return
        
        while i < steps and curr.next:
            curr = curr.next
            i += 1
            
        self.homepage = curr
        return self.homepage.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)