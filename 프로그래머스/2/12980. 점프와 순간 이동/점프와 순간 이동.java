import java.util.*;

public class Solution {
    
    public int solution(int n) {
        // 문제를 변환해보면, 결국 이진법을 구해서 1의 갯수를 더하면 된다.
        return Integer.bitCount(n);
    }
    
}