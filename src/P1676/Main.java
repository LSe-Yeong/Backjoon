package P1676;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        double fact= 1.0;
        int count=0;
        // n!
        for(int i=1;i<=N;i++){
            fact=fact*i;
        }
        while(true){
            if(fact%10==0){
                fact=fact/10;
                count++;
            }
            else{
                break;
            }
        }
        System.out.println(count);
    }
}
