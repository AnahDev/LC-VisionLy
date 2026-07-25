// simulador_pila.js
function validarLenguajeAnBn(cadena) {
    let pila = ['Z0']; // Símbolo inicial de la pila
    let estado = 'q0';
    
    console.log(`Cadena a evaluar: "${cadena}"`);
    console.log(`Estado inicial: ${estado}, Pila: [${pila}]`);

    for (let i = 0; i < cadena.length; i++) {
        let simbolo = cadena[i];

        if (estado === 'q0') {
            if (simbolo === 'a') {
                pila.push('X'); // Operación PUSH
                console.log(`Lee: ${simbolo} -> Estado: q0, Pila: [${pila}]`);
            } else if (simbolo === 'b') {
                // Cambia de estado al encontrar la primera 'b' y desapila
                if (pila[pila.length - 1] === 'X') {
                    pila.pop(); // Operación POP
                    estado = 'q1';
                    console.log(`Lee: ${simbolo} -> Estado: q1, Pila: [${pila}]`);
                } else {
                    return "Cadena Rechazada: Llegó una 'b' pero no hay 'a' en la pila.";
                }
            } else {
                return `Cadena Rechazada: Símbolo no permitido '${simbolo}'`;
            }
        } else if (estado === 'q1') {
            if (simbolo === 'b') {
                if (pila[pila.length - 1] === 'X') {
                    pila.pop(); // Operación POP
                    console.log(`Lee: ${simbolo} -> Estado: q1, Pila: [${pila}]`);
                } else {
                    return "Cadena Rechazada: Demasiadas 'b' para la cantidad de 'a'.";
                }
            } else {
                return "Cadena Rechazada: No pueden venir 'a' después de una 'b'.";
            }
        }
    }

    // Transición épsilon final para verificar aceptación
    if (estado === 'q1' && pila.length === 1 && pila[0] === 'Z0') {
        estado = 'q2'; // Estado final de aceptación
        console.log(`Fin de cadena -> Estado: q2 (Aceptado), Pila: [${pila}]`);
        return "¡Cadena ACEPTADA con éxito!";
    } else {
        return "Cadena Rechazada: Faltaron 'b' por procesar o la pila no quedó vacía.";
    }
}

// Pruebas de ejecución
console.log(validarLenguajeAnBn("aaabbb")); // Caso Exitoso
console.log("\n-----------------------------\n");
console.log(validarLenguajeAnBn("aabbb"));   // Caso Fallido