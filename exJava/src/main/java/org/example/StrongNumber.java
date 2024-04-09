package org.example;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class StrongNumber {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);

        var numRandom = numberRandom(10);


        for (String elemento : numRandom) {
            System.out.println();
            System.out.println();
            System.out.println("Elemento: " + elemento);

            for (char digito : elemento.toCharArray()) {
                String digitoComoString = String.valueOf(digito);
                verificarStrong(digitoComoString);
            }
        }



//        System.out.println("Digite um número positivo para saber se ele é forte: ");
//        var input = scanner.nextLine();

    }

    public static void verificarStrong(String strong){

        long sumFactorial = 0;


        for (int i = 0; i < strong.length(); i++) {

            var num = Character.getNumericValue(strong.charAt(i));
            long factorial = (long) calculaFatorial(num);
            sumFactorial += factorial;

            System.out.println("o fatorial do numero " + num + "! é: " + factorial);
            System.out.println();
        }

        if (Integer.parseInt(strong) == sumFactorial) {
            System.out.println("O numero " + strong + " é um NUMBER STRONG!");
            System.out.println("Pois a soma dos fatoriais dos digitos de " + strong + " é: " + sumFactorial);
            System.out.println("-".repeat(85));

        } else {
            System.out.println("O numero " + strong + " NÃO É STRONG! pois a soma dos fatoriais dos seus digitos não é igual a " + strong);
            System.out.println("-".repeat(85));
            System.out.println();
            System.out.println();

        }

    }

    public static ArrayList<String> numberRandom(int n){
        var random =  new Random();
        var list = new ArrayList<String>();

        for (int ip = 0; ip < n; ip++){
            var numeroAleatorio = random.nextInt(600);
            var transformar = String.valueOf(numeroAleatorio);
            list.add(transformar);

        }
        return list;
    }

    private static Object calculaFatorial ( int num){

        long factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }
        return factorial;
    }
}