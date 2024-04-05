package P10824;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String A, B, C, D;
        Scanner sc = new Scanner(System.in);

        A = sc.next();
        B = sc.next();
        C = sc.next();
        D = sc.next();

        A.trim();
        B.trim();
        C.trim();
        D.trim();

        Long T1 = Long.parseLong(A + B);
        Long T2 = Long.parseLong(C + D);

        System.out.println(T1 + T2);

    }
}
