package P10799;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String str=br.readLine();
        ArrayList<Integer> laser=new ArrayList<>();
        Stack<Character> charStack=new Stack<>();
        boolean isLaser=true;
        int sum=0;
        int splitNum;
        int stickNum=0;
        StringBuilder sb=new StringBuilder();

        for(int i=0;i<str.length();i++){
            char element=str.charAt(i);
            if(element=='('){
                charStack.push(element);
                isLaser=true;
            }
            else if(element==')'){
                if(isLaser){
                    charStack.pop();
                    splitNum=charStack.size();
                    sum=sum+splitNum;
                }
                else{
                    charStack.pop();
                    stickNum++;
                }
                isLaser=false;
            }
        }
        sum=sum+stickNum;
        sb.append(sum);
        System.out.print(sb.toString());
    }
}
