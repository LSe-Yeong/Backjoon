package P6588;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc=new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            int N;
            int a,b;
            boolean isvalid=false;
            int idx=0;
            N = Integer.parseInt(br.readLine());

            if(N==0)
                break;

            int[] array = new int[N + 1];
            ArrayList<Integer> prime=new ArrayList<>();

            //소수판별
            for (int i = 1; i <= N; i++) {
                array[i] = i;
            }

            for (int i = 2; i < (int) Math.sqrt(N); i++) {
                if (array[i] != 0) {
                    for (int j = i * i; j <= N; j = j + i) {
                        array[j] = 0;
                    }
                }
            }
            for (int i = 1; i <= N; i++) {
                if (array[i] != 0 && array[i] != 1) {
                    prime.add(array[i]);
                    idx++;
                }
            }

            //구하기
            for (int i = 1; i<prime.size(); i++) {
                a = prime.get(i);
                b = N - a;
                for (int j = prime.size()-1; j>=0 ; j--) {
                    if (b == prime.get(j)) {
                        isvalid = true;
                        break;
                    }
                }
                if(i+1== prime.size()){
                    System.out.println("Goldbach's conjecture is wrong.");
                    break;
                }
                if (isvalid) {
                    System.out.println(N + "=" + a + "+" + b);
                    break;
                }
            }
        }
    }
}
