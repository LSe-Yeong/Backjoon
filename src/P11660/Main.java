package P11660;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        int n;
        int m;
        int x1,y1,x2,y2;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        int[][] array=new int[n+1][n+1];
        int[][] D=new int[n+1][n+1];

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                array[i][j]=sc.nextInt();
            }
        }

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                D[i][j]=D[i-1][j]+D[i][j-1]-D[i-1][j-1]+array[i][j];
            }
        }

        for(int t=0;t<m;t++){
            int result=0;
            x1=sc.nextInt();
            y1=sc.nextInt();
            x2=sc.nextInt();
            y2=sc.nextInt();

            result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1];
            System.out.println(result);
        }
    }
}
