import java.util.*;


class Solution {
    
    static int[] dxs = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dys = {0, 1, 1, 1, 0, -1, -1, -1};
    
    public int solution(int[] arrows) {
        int answer = 0;
        
        // 주어진 방향으로 움직이면서 바로바로 방이 생기는지 확인해야 함
        Set<Point> visitedPoint = new HashSet<>();
        Set<Line> visitedLine = new HashSet<>();
        
        Point cur = new Point(0, 0);
        visitedPoint.add(cur);
        
        for (int i = 0; i < arrows.length; i++) {
            for (int j = 0; j < 2; j++) {
                int d = arrows[i];
                int dx = dxs[d], dy = dys[d];
                int nx = cur.x+dx, ny = cur.y+dy;
                Point np = new Point(nx, ny);

                Line curLine = new Line(cur, np);

                if (visitedPoint.contains(np)) {
                    if (!visitedLine.contains(curLine)) {
                        answer++;
                    }
                }
                visitedPoint.add(np);
                visitedLine.add(new Line(cur, np));
                visitedLine.add(new Line(np, cur));
                
                cur = np;
            }
        }
        
        return answer;
    }
    
    static class Point {
		int x;
		int y;

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public boolean equals(Object obj) {
			Point p = (Point) obj;
			return x == p.x && y == p.y;
		}

		@Override
		public int hashCode() {
			return Objects.hash(x, y);
		}
        
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
	}
    
    static class Line {
        Point p1;
        Point p2;
        
        public Line(Point p1, Point p2) {
            this.p1 = p1;
            this.p2 = p2;
        }
        
        @Override
		public boolean equals(Object obj) {
			Line line = (Line) obj;
			return line.p1.equals(p1) && line.p2.equals(p2);
		}

		@Override
		public int hashCode() {
			return Objects.hash(p1, p2);
		}
    }
}