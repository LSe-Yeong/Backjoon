package P2667;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main { ;
    static int[][] check;
    static int count=0;
    static ArrayList<Integer> countTown=new ArrayList<>();
    static int countDanji=0;
    static int[][] town;
    static StringBuilder stringBuilder=new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        town=new int[N+2][N+2];

        for(int i=1;i<N+1;i++){
            String str= br.readLine();
            for(int j=1;j<N+1;j++){
                town[i][j]=str.charAt(j-1)-48;
            }
        }

        check=new int[N+2][N+2];

        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                if(town[i][j]==1 && check[i][j]==0){
                    countDanji++;
                    DFS(i,j);
                    countTown.add(count);
                    count=0;
                }
            }
        }
        Collections.sort(countTown);
        stringBuilder.append(countDanji).append("\n");
        for(int i=0;i<countTown.size();i++){
            stringBuilder.append(countTown.get(i)).append("\n");
        }
        System.out.print(stringBuilder.toString());
    }
    private static void DFS(int x,int y){
        check[x][y]=1;
        count++;
        if(town[x+1][y]==1 && check[x+1][y]==0){
            DFS(x+1,y);
        }
        if(town[x-1][y]==1 && check[x-1][y]==0){
            DFS(x-1,y);
        }
        if(town[x][y+1]==1 && check[x][y+1]==0){
            DFS(x,y+1);
        }
        if(town[x][y-1]==1 && check[x][y-1]==0){
            DFS(x,y-1);
        }
    }
}
