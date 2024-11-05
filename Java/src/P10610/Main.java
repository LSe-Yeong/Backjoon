package P10610;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        ArrayList<Character> list = new ArrayList<>();

        String N = br.readLine();

        int sum=0;
        for(int i=0;i<N.length();i++){
            list.add(N.charAt(i));
            sum=sum+N.charAt(i)-'0';
        }

        String result="";
        if(sum%3!=0){
            sb.append(-1);
        }
        else{
            Collections.sort(list,Collections.reverseOrder());
            if(list.get(list.size()-1)!='0'){
                sb.append(-1);
            }
            else {
                for (int i = 0; i < list.size(); i++) {
                    String ele = String.valueOf(list.get(i));
                    result+=ele;
                }
                sb.append(result);
            }
        }

        System.out.print(sb.toString());
    }
}
