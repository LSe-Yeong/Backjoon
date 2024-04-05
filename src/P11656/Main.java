package P11656;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s;
        s=sc.next();
        String[] array=new String[s.length()];

        //접미사 파싱
        for(int i=0;i<s.length();i++){
            array[i]=s.substring(i);
        }
        //사전순 정렬
        Arrays.sort(array);

        for(int i=0;i<s.length();i++){
            System.out.println(array[i]);
        }
    }
}
