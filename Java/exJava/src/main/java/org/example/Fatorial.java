package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Fatorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int numeroStrong = 1;
        List<Integer> listaDeNumerosFortes = new ArrayList<>();

        System.out.println("Digite um numero maximo: ");
        int maxNumero = Integer.parseInt(input.nextLine());

        for (int i = 0; i < maxNumero + 1; i++){
            numeroStrong = i;
            listaDeNumerosFortes.add(numeroStrong);
        }
        for (int numero : listaDeNumerosFortes){
            verificarStrong(String.valueOf(numero));
        }

        System.out.print("Fim do código!");
    }

    public static void verificarStrong(String stringNumero) {
        List<Integer> lista = new ArrayList<>();
        List<Integer> numerosStrong = new ArrayList<>();

        var numeroConvertido = Integer.parseInt(stringNumero);

        for (int valor = 0; stringNumero.length() > valor; valor++) {
            numeroConvertido = Integer.parseInt(String.valueOf(stringNumero.charAt(valor)));

            int resultado = calcularFatorial(numeroConvertido);
            lista.add(resultado);
        }

        int soma = 0;
        for (int numeroLista : lista) {
            soma += numeroLista;
        }

        if (soma == Integer.parseInt(stringNumero)) {
            numerosStrong.add(Integer.valueOf(stringNumero));
            System.out.println(stringNumero + " STRONG!!");
        }
    }

    public static int calcularFatorial(int numero) {
        int resultado = 1;
        for (int i = 1; i <= numero; i++) {
            resultado *= i;
        }
        return resultado;
    }

}
