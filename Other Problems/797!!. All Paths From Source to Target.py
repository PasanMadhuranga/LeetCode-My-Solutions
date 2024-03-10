class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if(not graph): return []

        stack = [(0, [0])]
        answer = []
        lastNode = len(graph) - 1
        while stack:
            curNode, curPath = stack.pop()

            if (curNode == lastNode):
                answer.append(curPath)

            for neighbour in graph[curNode]:
                stack.append((neighbour, curPath + [neighbour]))

        return answer
        