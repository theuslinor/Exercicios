package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Crime {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String resposta;
        int somaDasRespostas = 0;

        System.out.println("Qual seu nome? ");
        String nome = input.nextLine();

        List<String> perguntas = new ArrayList<>(
                List.of("Telefonou para a vítima?",
                        "Esteve no local do crime?",
                        "Mora perto da vítima?",
                        "Devia para a vítima?",
                        "Já trabalhou com a vítima?")
        );

        System.out.println("Sobre o crime, irei realizar algumas perguntas, seja sincero e responda apenas com 'Sim' ou 'Não'.");
        System.out.println();

        for (int i = 0; i < perguntas.size(); i++){
            System.out.println(perguntas.get(i));
            resposta = input.nextLine();
            
            if (resposta.equals("Sim") || resposta.equals("sim")){
                somaDasRespostas += 1;
            }
        }


        if (somaDasRespostas == 2){
            System.out.println(nome + " é suspeito.");
        }
        if (somaDasRespostas == 3 || somaDasRespostas == 4){
            System.out.println(nome + " é cúmplice.");
        }
        if (somaDasRespostas >= 5){
            System.out.println(nome + " é assassino.");
        }
        if (somaDasRespostas <= 1){
            System.out.println(nome + " é inocente.");
        }

    }
}
