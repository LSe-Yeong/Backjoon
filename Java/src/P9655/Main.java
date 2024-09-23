package P9655;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int n=Integer.parseInt(br.readLine());
        if(n%2==1){
            sb.append("SK");
        }
        else{
            sb.append("CY");
        }
        System.out.print(sb.toString());
    }
}