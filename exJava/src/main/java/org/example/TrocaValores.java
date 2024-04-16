package org.example;

import java.util.Scanner;

public class TrocaValores {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o valor de A: ");
        int A = input.nextInt();

        System.out.println("Digite o valor de B: ");
        int B = input.nextInt();

        int temp = A;
        A = B;
        B = temp;

        System.out.println("Valores trocaos: ");
        System.out.println("A: " + A);
        System.out.println("B: " + B);

        input.close();
    }
}
