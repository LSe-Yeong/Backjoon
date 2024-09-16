package P15649;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static boolean[] isCheck;
    static int[] arr;
    static StringBuilder sb=new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());

        isCheck=new boolean[n+1];
        arr=new int[k];
        func(n,0,k);
        System.out.print(sb.toString());
    }
    public static void func(int n,int count,int k){
        if(k==count){
            for(int i=0;i<arr.length;i++){
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i=1;i<=n;i++){
            if(!isCheck[i]){
                arr[count]=i;
                isCheck[i]=true;
                func(n,count+1,k);
                isCheck[i]=false;
            }
        }
    }
}
