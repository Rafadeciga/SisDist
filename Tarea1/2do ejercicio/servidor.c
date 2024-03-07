#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#define PORT 4000 // Puerto donde escucha el servidor

int main() {
    int server_fd, client_fd; // Descriptores de los sockets
    struct sockaddr_in server_addr, client_addr; // Estructuras para las direcciones
    socklen_t client_len; // Tamaño de la dirección del cliente
    int num; // Número entero que se recibe y se envía

    // Crear el socket del servidor
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Error al crear el socket");
        exit(1);
    }

    // Configurar la dirección del servidor
    memset(&server_addr, 0, sizeof(server_addr)); // Llenar con ceros
    server_addr.sin_family = AF_INET; // Familia IPv4
    server_addr.sin_addr.s_addr = INADDR_ANY; // Cualquier dirección
    server_addr.sin_port = htons(PORT); // Puerto en orden de red

    // Asociar el socket con la dirección
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Error al asociar el socket");
        exit(1);
    }

    // Escuchar conexiones entrantes
    if (listen(server_fd, 1) == -1) {
        perror("Error al escuchar el socket");
        exit(1);
    }

    printf("Servidor escuchando en el puerto %d\n", PORT);

    // Aceptar una conexión de un cliente
    client_len = sizeof(client_addr);
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd == -1) {
        perror("Error al aceptar la conexión");
        exit(1);
    }

    printf("Cliente conectado\n");

    // Recibir y enviar números enteros hasta que el cliente envíe un cero
    do {
        // Recibir un número entero del cliente
        if (read(client_fd, &num, sizeof(num)) == -1) {
            perror("Error al leer del socket");
            exit(1);
        }

        // Convertir el número a orden de host
        num = ntohl(num);

        printf("Recibido: %d\n", num);

        // Incrementar el número en uno
        num++;

        // Convertir el número a orden de red
        num = htonl(num);

        // Enviar el número al cliente
        if (write(client_fd, &num, sizeof(num)) == -1) {
            perror("Error al escribir en el socket");
            exit(1);
        }

        printf("Enviado: %d\n", ntohl(num));

        // Si el número es cero, salir del bucle
        if (num == 0) {
            break;
        }
    } while (1);

    // Cerrar los sockets
    close(client_fd);
    close(server_fd);

    printf("Cliente desconectado\n");

    return 0;
}
