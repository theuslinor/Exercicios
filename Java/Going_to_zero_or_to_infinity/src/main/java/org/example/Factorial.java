package org.example;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Escolha um número: ");
        int number = input.nextInt();

        long factorial = 1;
        String steps = "O fatorial de " + number + " é: ";

        for (int i = number; i > 0; i--) {
            factorial *= i;
            steps += i;
            if (i != 1) {
                steps += " x ";
            }
        }

        steps += " = " + factorial;
        System.out.println(steps);

        input.close();
    }
}
