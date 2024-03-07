import java.io.*;
import java.net.*;

public class ServidorT {
    public static void main(String[] args) {
        final int PUERTO = 12345;
        try {
            ServerSocket servidorSocket = new ServerSocket(PUERTO);
            System.out.println("ServidorT iniciado, esperando por clientes...");
            
            Socket clienteSocket = servidorSocket.accept(); // Acepta la conexión del cliente
            System.out.println("Cliente conectado.");

            // Para leer lo que envía el cliente
            BufferedReader entrada = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));
            // Para enviar datos al cliente
            PrintWriter salida = new PrintWriter(clienteSocket.getOutputStream(), true);
            
            // Lee el mensaje del cliente
            String mensajeCliente = entrada.readLine();
            System.out.println("Cliente dice: " + mensajeCliente);
            
            // Responde al cliente
            String respuesta = "Hola que tal";
            salida.println(respuesta);
            
            // Cierra las conexiones
            entrada.close();
            salida.close();
            clienteSocket.close();
            servidorSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
