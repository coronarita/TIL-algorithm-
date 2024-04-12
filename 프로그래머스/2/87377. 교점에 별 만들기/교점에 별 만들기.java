import java.util.*;

class Solution {
    // 점 객체 정의
    private static class Point{
        public final long x, y; // 접근은 해야되니까 public
        
        private Point(long x, long y){ // Constructor
            this.x = x;
            this.y = y;
        }
    }
        
    // 교차점 계산 후 점 객체로 반환
    private Point intersection(long a1, long b1, long c1, long a2, long b2, long c2){
        
        double x = (double) (c2*b1 - c1*b2) / (b2*a1 - b1*a2);
        double y = (double) (c1*a2 - c2*a1) / (b2*a1 - b1*a2);
        
        // 정수일 경우만 반환한다.
        if ((x%1)!=0 || (y%1)!=0) return null;
            
        return new Point((long)x, (long)y);
    }
    
    // 점 최솟값, 최댓값 계산
    private Point getMinimumPoint(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point p : points){
            if (p.x < x) x = p.x;
            if (p.y < y) y = p.y;
        }
        
        return new Point(x, y);
    }
    
    private Point getMaximumPoint(List<Point> points){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for (Point p : points){
            if (p.x > x) x = p.x;
            if (p.y > y) y = p.y;
        }
        
        return new Point(x, y);
    }
    
    // Main
    public String[] solution(int[][] line) {
        // 계산 된 점 저장 리스트
        List<Point> points = new ArrayList<>();
        
        // line 순회하면서 계산
        for (int i=0; i < line.length; i++){
            for (int j=0; j < line.length; j++){
                // 교차점 계산
                Point intersection = intersection(line[i][0], line[i][1], line[i][2], 
                                                 line[j][0], line[j][1], line[j][2]);
                
                if (intersection != null) points.add(intersection);
                
            }
        }
        
//         for (Point p : points){
//             System.out.printf("%d %d", p.x, p.y);
//         }
        
        // 최대, 최솟값 계산
        Point maximum = getMaximumPoint(points);
        Point minimum = getMinimumPoint(points);
        
        int width = (int) (maximum.x - minimum.x + 1);
        int height = (int) (maximum.y - minimum.y + 1);
        
        // '*', '.'으로 이루어짐. char 배열 만들기
        char[][] arr = new char[height][width];
        for (char[] row: arr){
            Arrays.fill(row, '.'); // 정적 메소드로 초기화
        }
        
        // 점 변환해서 대입하기 (평행이동, 뒤집기)
        for (Point p : points){
            int x = (int) (p.x - minimum.x);
            int y = (int) (-(p.y - maximum.y)); // 변환
            arr[y][x] = '*';
        }
        
        String[] result = new String[arr.length];
        for (int i=0; i < result.length; i++){
            result[i] = new String(arr[i]); // (String)(arr[i]); 가 아님..
        }
        
        return result;
    }
}