class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [homepage]
        self.totHisLen = 1
        self.curPos = 0
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curPos + 1]
        self.history.append(url)
        self.curPos += 1
        self.totHisLen = self.curPos + 1
        

    def back(self, steps: int) -> str:
        self.curPos -= steps
        if (self.curPos < 0): 
            self.curPos = 0
        return self.history[self.curPos]
        

    def forward(self, steps: int) -> str:
        self.curPos += steps
        if (self.curPos >= self.totHisLen):
            self.curPos = self.totHisLen - 1
        return self.history[self.curPos]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



# Another solution found in the discussion section
class BrowserHistory {
public:
    stack<string> history;
    stack<string> future;
	
    BrowserHistory(string homepage) {
        history.push(homepage);
        future = stack<string>();           // Reset the forward stack.
    }
    
    void visit(string url) {
        history.push(url);
        future = stack<string>();           // Reset the forward stack.
    }
    
    string back(int steps) {
        while(steps > 0 && history.size() > 1) { // Always keep at least one element in the stack. 
            future.push(history.top());
            history.pop();
            steps--;
        }
        return history.top();
    }
    
    string forward(int steps) {
        while(steps > 0 && future.size() > 0) {
            history.push(future.top());
            future.pop();
            steps--;
        }
        return history.top();
    }
};