package org.example;

import java.util.Scanner;

public class Bissexto {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int ano;

        while(true){
            System.out.print("Digite um ano: ");
            ano = input.nextInt();

            if (ano <= -1){
                break;
            }

            if (ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0){
                System.out.println("O ano de " + ano + " é ano bissexto.");
            } else{
                System.out.println("O ano de " + ano + " não é bissexto.");
            }

        }

        System.out.println("Fim do Programa.");

        input.close();
    }

}
