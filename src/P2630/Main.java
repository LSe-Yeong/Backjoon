package P2630;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] paper;
    static int blue;
    static int white;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(br.readLine());

        paper=new int[N][N];
        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                paper[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        paperSplit(paper,0,0,N);
        sb.append(white).append("\n");
        sb.append(blue).append("\n");
        System.out.print(sb.toString());

    }

    public static void paperSplit(int[][] p,int row, int col, int paperSize){
        int temp=p[row][col];
        boolean isComplete=true;
        for(int i=row;i<row+paperSize;i++){
            for(int j=col;j<col+paperSize;j++){
                if(temp!=p[i][j]){
                    isComplete=false;
                }
            }
        }
        if(isComplete){
            if(temp==1){
                blue++;
            }
            else{
                white++;
            }
        }
        else{
            paperSplit(p,row+paperSize/2,col,paperSize/2);
            paperSplit(p,row,col,paperSize/2);
            paperSplit(p,row,col+paperSize/2,paperSize/2);
            paperSplit(p,row+paperSize/2,col+paperSize/2,paperSize/2);
        }
    }
}
