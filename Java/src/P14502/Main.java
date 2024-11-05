package P14502;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[][] my_map;
    static int row;
    static int col;

    public static void bfs(int[] start,int[][] map){
        boolean[][] isVisit = new boolean[row][col];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(start);
        isVisit[start[0]][start[1]]=true;
        int[] dRow={0,0,1,-1};
        int[] dCol={1,-1,0,0};
        while(!queue.isEmpty()){
            int[] ele = queue.poll();
            for(int i=0;i<dRow.length;i++){
                int nRow=ele[0]+dRow[i];
                int nCol=ele[1]+dCol[i];
                if(nRow < 0 || nRow>row-1 || nCol<0 || nCol>col-1){
                    continue;
                }
                if(map[nRow][nCol]==0){
                    queue.offer(new int[]{nRow,nCol});
                    map[nRow][nCol]=3;
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());
        my_map = new int[row][col];
        int max_count=0;
        ArrayList<int[]> wallList = new ArrayList<>();

        for(int i=0;i<row;i++){
            st= new StringTokenizer(br.readLine());
            for(int j=0;j<col;j++){
                my_map[i][j]=Integer.parseInt(st.nextToken());
                if(my_map[i][j]==0){
                    wallList.add(new int[]{i,j});
                }
            }
        }

        for(int i=0;i< wallList.size()-2;i++){
            for(int j=i+1;j<wallList.size()-1;j++){
                for(int k=j+1;k< wallList.size();k++){
                    int[][] copy_map = new int[row][col];
                    for(int r=0;r<my_map.length;r++){
                        for(int c=0;c<my_map[r].length;c++){
                            copy_map[r][c]=my_map[r][c];
                        }
                    }
                    int[] point1= wallList.get(i);
                    int[] point2 = wallList.get(j);
                    int[] point3 = wallList.get(k);
                    copy_map[point1[0]][point1[1]]=1;
                    copy_map[point2[0]][point2[1]]=1;
                    copy_map[point3[0]][point3[1]]=1;

                    for(int r=0;r< copy_map.length;r++){
                        for(int c=0;c<copy_map[r].length;c++){
                            if(copy_map[r][c]==2){
                                bfs(new int[]{r,c},copy_map);
                            }
                        }
                    }
                    int count=0;
                    for(int r=0;r<copy_map.length;r++){
                        for(int c=0;c<copy_map[r].length;c++){
                            if(copy_map[r][c]==0){
                                count++;
                            }
                        }
                    }
                    if(count>max_count){
                        max_count=count;
                    }
                }
            }
        }

        sb.append(max_count);
        System.out.print(sb.toString());
    }
}
