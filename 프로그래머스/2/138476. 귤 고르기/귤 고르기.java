import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
                
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // C++, 파이썬처럼 유연하게 뽑을 수 있다.
        for (int t : tangerine){
            map.put(t, map.getOrDefault(t, 0) + 1);
        }
        
        // 정렬을 위해서 - 키값을 ?
        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort(
            (o1, o2) -> map.get(o2) - map.get(o1)
        ); // lambda 식으로, 내림차순 정렬하기 위해서
        
        for (Integer key:list){
            k -= map.get(key);
            answer++;
            if (k<=0){break;}
        }
        
        
        return answer;
    }
}