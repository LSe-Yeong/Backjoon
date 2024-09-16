package P10828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        int[] stack=new int[N+1];
        int top=0;
        for(int i=0;i<N;i++) {
            String[] inputs = br.readLine().split(" ");
            if(inputs[0].equals("push")){
                stack[top]=Integer.parseInt(inputs[1]);
                top++;
            }
            else if(inputs[0].equals("pop")){
                if(top==0){
                    System.out.println(-1);
                }
                else {
                    top--;
                    System.out.println(stack[top]);
                }
            }
            else if(inputs[0].equals("size")){
                System.out.println(top);
            }
            else if(inputs[0].equals("empty")){
                if(top==0){
                    System.out.println(1);
                }
                else{
                    System.out.println(0);
                }
            }
            else if(inputs[0].equals("top")){
                if(top==0){
                    System.out.println(-1);
                }
                else{
                    System.out.println(stack[top-1]);
                }
            }
        }
    }
}
