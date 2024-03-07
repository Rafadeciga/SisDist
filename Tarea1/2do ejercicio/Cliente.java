// Programa Cliente en Java

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Cliente {

    public static void main(String[] args) {
        // Dirección y puerto del servidor
        String host = "localhost";
        int port = 4000;

        try {
            // Crear el socket del cliente
            Socket socket = new Socket(host, port);

            // Obtener los flujos de entrada y salida del socket
            DataInputStream input = new DataInputStream(socket.getInputStream());
            DataOutputStream output = new DataOutputStream(socket.getOutputStream());

            // Crear un scanner para leer de la entrada estándar
            Scanner scanner = new Scanner(System.in);

            // Enviar y recibir números enteros hasta que el usuario escriba un cero
            int num;
            do {
                // Leer un número entero de la entrada estándar
                System.out.print("Ingrese un número entero: ");
                num = scanner.nextInt();

                // Enviar el número al servidor
                output.writeInt(num);

                // Recibir el número incrementado del servidor
                num = input.readInt();

                // Mostrar el número recibido
                System.out.println("Recibido: " + num);
            } while (num != 0);

            // Cerrar el scanner, los flujos y el socket
            scanner.close();
            input.close();
            output.close();
            socket.close();

        } catch (IOException e) {
            // Manejar la excepción de entrada/salida
            e.printStackTrace();
        }
    }
}
