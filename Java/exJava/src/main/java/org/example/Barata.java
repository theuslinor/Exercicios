package org.example;

import java.util.Scanner;

public class Barata {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite a velocidade da barata: ");
        double velocidade = input.nextDouble();

        int velocidadeSegundos = (int) (velocidade *  0.277778);

        System.out.println("Velocidade da barata é " + velocidadeSegundos + " metros/s");

        input.close();
    }


}
