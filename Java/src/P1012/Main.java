package P1012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] check;
    static int count=0;
    static int[][] ddang;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();

        int t=Integer.parseInt(br.readLine());
        for(int i=0;i<t;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int M=Integer.parseInt(st.nextToken());
            int N=Integer.parseInt(st.nextToken());
            int k=Integer.parseInt(st.nextToken());

            check=new int[N+2][M+2];
            ddang=new int[N+2][M+2];

            for(int m=0;m<k;m++){
                st=new StringTokenizer(br.readLine());
                int x=Integer.parseInt(st.nextToken());
                int y=Integer.parseInt(st.nextToken());

                ddang[y+1][x+1]=1;
            }

            for(int x=1;x<N+1;x++){
                for(int y=1;y<M+1;y++){
                    if(check[x][y]==0 && ddang[x][y]==1){
                        DFS(x,y);
                        count++;
                    }
                }
            }
            stringBuilder.append(count).append("\n");
            count=0;
        }
        System.out.print(stringBuilder.toString());
    }

    private static void DFS(int x,int y){
        check[x][y]=1;
        if(ddang[x+1][y]==1 && check[x+1][y]==0){
            DFS(x+1,y);
        }
        if(ddang[x-1][y]==1 && check[x-1][y]==0){
            DFS(x-1,y);
        }
        if(ddang[x][y+1]==1 && check[x][y+1]==0){
            DFS(x,y+1);
        }
        if(ddang[x][y-1]==1 && check[x][y-1]==0){
            DFS(x,y-1);
        }
    }
}
