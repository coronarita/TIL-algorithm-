
def solution(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    # 시작점의 인접리스트 산출
    for key, val in tickets : 
        graph[key].append(val)
    # print(graph)
    # 도착점 기준 알파벳순 정렬
    for g in graph:
        graph[g].sort()

    def dfs(graph):
        answer = [] # 경로
        stacks = ["ICN"] # 스택

        while stacks :
            stack = stacks[-1]
            # 시작점에 없거나, 더 이상 갈 곳이 없음
            if stack not in graph or len(graph[stack]) == 0 :
                answer.append(stacks.pop())
            else : # 경로에 stack 추가
                stacks.append(graph[stack].pop(0))

        return answer[::-1]

    answer = dfs(graph)
    return answer
