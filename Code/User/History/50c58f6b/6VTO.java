import java.util.Scanner;

public class Tutorial {

    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);

        int a,b;


        System.out.println("Digite un numero");
            a = entrada.nextInt();
        System.out.println("Digite el segundo numero");
            b = entrada.nextInt();
        System.out.println("el numero que has  selecionado es: "+a+" y "+b);
    }

}
