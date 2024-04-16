package org.example;

public class CorHexadecimal {
    public static void main(String[] args) {
        String cor = "#BB1FBF";
        int total = 255;

        int red = Integer.parseInt(cor.substring(1,3), 16);
        int green = Integer.parseInt(cor.substring(3,5), 16);
        int blue = Integer.parseInt(cor.substring(5, 7), 16);

        System.out.println("A cor em Hexadecimal " + cor + " tem a porcentagem do RGB: ");
        System.out.println("Red: " + String.format("%.0f", Math.floor((double) red / total * 100)) + "%");
        System.out.println("Green: " + String.format("%.0f", Math.floor((double) green / total * 100)) + "%");
        System.out.println("Blue: " + String.format("%.0f", Math.floor((double) blue / total * 100)) + "%");
    }
}
