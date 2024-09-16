package P9012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        boolean flag=true;
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        StringBuilder stringBuilder=new StringBuilder();

        for(int i=0;i<t;i++){
            Stack<Character> stack= new Stack<>();
            String str=br.readLine();
            for(int j=0;j<str.length();j++){
                char ch=str.charAt(j);
                if(ch==')'){
                    if(stack.isEmpty()){
                        stringBuilder.append("NO");
                        System.out.println(stringBuilder.toString());
                        stringBuilder.setLength(0);
                        flag=false;
                        break;
                    }
                    stack.pop();
                }
                else{
                    stack.push(ch);
                }
            }
            if(!stack.isEmpty()){
                stringBuilder.append("NO");
                System.out.println(stringBuilder.toString());
                stringBuilder.setLength(0);
            }
            else if(flag){
                stringBuilder.append("YES");
                System.out.println(stringBuilder.toString());
                stringBuilder.setLength(0);
            }
            flag=true;
        }
    }
}
