#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s <archivo.yml>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error al abrir archivo");
        return 1;
    }

    char line[256];
    int networks_count = 0;
    int subnets_count = 0;

    // Analizador Léxico/Sintáctico básico en C
    while (fgets(line, sizeof(line), file)) {
        if (strstr(line, "net_interface_")) {
            networks_count++;
        }
        if (strstr(line, "subnet:")) {
            subnets_count++;
        }
    }

    fclose(file);
    // printf("C Parser: Redes=%d, Subredes=%d\n", networks_count, subnets_count);
    return 0;
}