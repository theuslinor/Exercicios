package org.example;

public class Vogais {

    public static void main(String[] args) {

        String frase = "A jornada da vida é como uma tela em branco, cada escolha é uma pincelada que molda o quadro do nosso destino.";
        int contagemVogais = 0;

        for (int i = 0; i < frase.length(); i++){
            if (frase.toLowerCase().charAt(i) == 'a' ||
                    frase.toLowerCase().charAt(i) == 'e' ||
                    frase.toLowerCase().charAt(i) == 'i' ||
                    frase.toLowerCase().charAt(i) == 'o' ||
                    frase.toLowerCase().charAt(i) == 'u'){
                contagemVogais += 1;
            }
        }

        System.out.println("A frase '" + frase + "' contém " + contagemVogais + " vogais.");
    }
}
