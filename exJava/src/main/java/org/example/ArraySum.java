package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class ArraySum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in).useLocale(Locale.US);

        double smaller = Double.MAX_VALUE;
        double max = Double.MIN_VALUE;
        double numb = 0;
        List<Double> numeros = new ArrayList<>();

        while(numb != -1) {
            System.out.print("Digite um número ou -1 para parar: ");
            numb = input.nextDouble();

            if (numb == -1) {
                break;
            }
            if (numb < smaller) {
                smaller = numb;
            }
            if (numb > max) {
                max = numb;
            }

            numeros.add(numb);
        }

        double sum = numeros.stream().reduce(0.0, Double::sum);

        System.out.println("O menor valor da lista é " + smaller);
        System.out.println("O maior valor da lista é " + max);
        System.out.println("Os valores da lista somados são " + sum);

        input.close();
    }
}
