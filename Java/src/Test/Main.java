package Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int[][] map;

    static int count=0;
    static int count1=0;
    static ArrayList<Integer> sizeOfArea;
    static int[][] isCheck;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        sizeOfArea=new ArrayList<>();
        map=new int[N+2][N+2];
        isCheck=new int[N+2][N+2];

        for(int i=1;i<=N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=1;j<=N;j++){
                map[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        for(int i=1;i<N+1;i++){
            for(int j=1;j<N+1;j++){
                if(isCheck[i][j]==0 && map[i][j]==1){
                    count++;
                    DFS(i,j);
                    sizeOfArea.add(count1);
                    count1=0;
                }
            }
        }
        sb.append(count).append("\n");

        Collections.sort(sizeOfArea);
        if(count==0){
            System.out.print(sb.toString());
        }
        else {
            for (int i = 0; i < sizeOfArea.size(); i++) {
                sb.append(sizeOfArea.get(i) + " ");
            }
            System.out.print(sb.toString());
        }
    }
    public static void DFS(int row,int col){
            isCheck[row][col]=1;
            count1++;
            if(isCheck[row+1][col]==0 && map[row+1][col]==1){
                DFS(row+1,col);
            }
            if(isCheck[row-1][col]==0  && map[row-1][col]==1){
                DFS(row-1,col);
            }
            if(isCheck[row][col+1]==0  && map[row][col+1]==1){
                DFS(row,col+1);
            }
            if(isCheck[row][col-1]==0  && map[row][col-1]==1){
                DFS(row,col-1);
            }
    }
}
