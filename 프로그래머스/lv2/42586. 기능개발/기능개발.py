## 다시 볼 문제 (과정이 도식화가 되면, 코드 짜는건 어렵지 않을 것 같다.)

def solution(progresses, speeds):
    answer = []
    # Queue 사용
    while progresses:
        cnt = 0
        
        while progresses and progresses[0] >= 100 : # 왼쪽부터 100에 도달 시, 작업기능과 속도를 제거
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
        
        if cnt :
            answer.append(cnt)
            
    
    return answer