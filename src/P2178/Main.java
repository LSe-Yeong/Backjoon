package P2178;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[][] check;
    static int[][] map;

    static Queue<Point> queue=new LinkedList<>();
    static int[][] dir;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();
        StringTokenizer st=new StringTokenizer(br.readLine());

        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());

        check=new int[n+2][m+2];
        map=new int[n+2][m+2];
        dir=new int[n+2][m+2];

        for(int i=1;i<n+1;i++){
            String str=br.readLine();
            for(int j=1;j<m+1;j++){
                map[i][j]=str.charAt(j-1)-'0';
            }
        }

        Point start=new Point(1,1);

        BFS(start);

        stringBuilder.append(dir[n][m]);
        System.out.print(stringBuilder.toString());
    }

    private static void BFS(Point spot){
        queue.offer(spot);
        dir[spot.x][spot.y]=1;
        check[spot.x][spot.y]=1;
        while(!queue.isEmpty()){
            Point element=queue.poll();
            if(map[element.x-1][element.y]==1 && check[element.x-1][element.y]==0){
                queue.offer(new Point(element.x-1, element.y));
                dir[element.x-1][element.y]=dir[element.x][element.y]+1;
                check[element.x-1][element.y]=1;
            }
            if(map[element.x+1][element.y]==1 && check[element.x+1][element.y]==0){
                queue.offer(new Point(element.x+1, element.y));
                dir[element.x+1][element.y]=dir[element.x][element.y]+1;
                check[element.x+1][element.y]=1;
            }
            if(map[element.x][element.y-1]==1 && check[element.x][element.y-1]==0){
                queue.offer(new Point(element.x, element.y-1));
                dir[element.x][element.y-1]=dir[element.x][element.y]+1;
                check[element.x][element.y-1]=1;
            }
            if(map[element.x][element.y+1]==1 && check[element.x][element.y+1]==0){
                queue.offer(new Point(element.x, element.y+1));
                dir[element.x][element.y+1]=dir[element.x][element.y]+1;
                check[element.x][element.y+1]=1;
            }
        }
    }
}
