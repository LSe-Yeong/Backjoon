package P9093;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        boolean isFirst=true;
        StringBuilder stringBuilder = new StringBuilder();
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        Stack<Character> stack=new Stack<>();
        for(int i=0;i<t;i++){
            String str=br.readLine();
            for(int j=0;j<str.length();j++){
                char ch=str.charAt(j);
                if(j==str.length()-1 || Character.isWhitespace(ch)) {
                    if(j==str.length()-1){
                        stack.push(ch);
                    }
                    if(!isFirst) {
                        stringBuilder.append(" ");
                    }

                    while (!stack.isEmpty()) {
                        stringBuilder.append(stack.pop());
                    }
                    isFirst=false;
                }
                else{
                    stack.push(ch);
                }
            }
            System.out.println(stringBuilder.toString());
            stringBuilder.setLength(0);
            isFirst=true;
        }
    }
}
