import java.util.Scanner;

package testetarget2;


public class TesteTarget2 {


    public static void main(String[] args) {
        
        //Declarando as variaveis de suporte   
        int primeiro = 0;
        int segundo = 1;
        int proximo = 0;
        
        //Armazenando o numero
        Scanner ler = new Scanner(System.in);
        System.out.print("Informe um número: ");
        int num = ler.nextInt();
        
        boolean pertence = false;
        
        
        while (proximo <= num) {
            if (proximo == num) {
                pertence = true;
                break;
            }
            proximo = primeiro + segundo;
            primeiro = segundo;
            segundo = proximo;
        }
        
        if (pertence) {
            System.out.println(num + " pertence à sequência de Fibonacci.");
        } else {
            System.out.println(num + " não pertence à sequência de Fibonacci.");
        }

    }
