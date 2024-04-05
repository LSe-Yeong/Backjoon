package P1463;

import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        int N;
        Scanner sc=new Scanner(System.in);

        N=sc.nextInt();
        int[] count=new int[N+1];

        for(int i=2;i<=N;i++){
            count[i]=count[i-1]+1;

            if(i%2==0){
                if(count[i]>=count[i/2]+1){
                    count[i]=count[i/2]+1;
                }
            }

            if(i%3==0){
                if(count[i]>=count[i/3]+1){
                    count[i]=count[i/3]+1;
                }
            }
        }

        System.out.println(count[N]);
    }
}
