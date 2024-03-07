#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int socketCliente;
    struct sockaddr_in direccionServidor;
    char buffer[1024] = {0};
    char mensaje[1024];

    printf("Ingrese el mensaje para enviar al servidor: ");
    fgets(mensaje, 1024, stdin); // Lee el mensaje del usuario desde la entrada estándar

    // Crear el socket
    if ((socketCliente = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Error al crear el socket \n");
        return -1;
    }

    direccionServidor.sin_family = AF_INET;
    direccionServidor.sin_port = htons(12345);

    // Convertir IPv4 o IPv6 de texto a binario
    if(inet_pton(AF_INET, "127.0.0.1", &direccionServidor.sin_addr) <= 0) {
        printf("\nDirección inválida / Dirección no soportada \n");
        return -1;
    }

    // Conectar el cliente al servidor
    if (connect(socketCliente, (struct sockaddr *)&direccionServidor, sizeof(direccionServidor)) < 0) {
        printf("\nConexión fallida. \n");
        return -1;
    }

    // Enviar el mensaje
    send(socketCliente , mensaje , strlen(mensaje) , 0 );
    printf("Mensaje enviado\n");

    // Recibir respuesta del servidor
    read( socketCliente , buffer, 1024);
    printf("Respuesta del servidor: %s\n", buffer );

    // Cerrar el socket
    close(socketCliente);

    return 0;
}
