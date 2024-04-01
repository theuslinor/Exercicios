package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ArraySum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int smaller = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int numb = 0;
        List<Integer> numeros = new ArrayList<>();

        while(numb != -1){
            System.out.print("Digite um número ou -1 para parar: ");
            numb = input.nextInt();

            if (numb == -1){
                break;
            }
            if (numb < smaller){
                smaller = numb;
            }
            if (numb > max){
                max = numb;
            }

            numeros.add(numb);
        }

        Integer sum = numeros.stream().reduce(0, Integer::sum);
        
        System.out.println("O menor valor da lista é " + smaller);
        System.out.println("O maior valor da lista é " + max);
        System.out.println("Os valores da lista somados são " + sum);

    }

}

