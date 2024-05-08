package P4949;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();

        while(true){
            String str=br.readLine();
            if(str.equals(".")){
                break;
            }
            Stack<Character> stack=new Stack<>();
            for(int i=0;i<str.length();i++){
                char ch = str.charAt(i);
                if(ch=='(' || ch=='['){
                    stack.push(ch);
                }
                else if(ch==')' || ch==']'){
                    if(stack.isEmpty()){
                        stringBuilder.append("no");
                        break;
                    }
                    char element=stack.pop();
                    if(ch==')' && element=='('){
                        continue;
                    }
                    else if(ch==')' && element=='['){
                        stringBuilder.append("no");
                        break;
                    }
                    else if(ch==']' && element=='('){
                        stringBuilder.append("no");
                        break;
                    }
                    else{
                        continue;
                    }
                }
            }
            if(stringBuilder.toString().equals("no")){
                System.out.println(stringBuilder.toString());
                stringBuilder.setLength(0);
            }
            else if(stack.isEmpty()){
                stringBuilder.append("yes");
                System.out.println(stringBuilder.toString());
                stringBuilder.setLength(0);
            }
            else{
                stringBuilder.append("no");
                System.out.println(stringBuilder.toString());
                stringBuilder.setLength(0);
            }
        }
    }
}
