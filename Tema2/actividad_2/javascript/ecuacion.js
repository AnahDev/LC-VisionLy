function calcularCuadraticaVectores() {
    const n = 200;
    const a = new Float64Array(n).fill(2.0);
    const b = new Float64Array(n).fill(5.0);
    const c = new Float64Array(n).fill(2.0);
    const x = new Float64Array(n);
    
    const iteraciones = 100000;
    
    const startTime = performance.now();
    
    for (let k = 0; k < iteraciones; k++) {
        for (let i = 0; i < n; i++) {
            let discriminante = (b[i] * b[i]) - (4 * a[i] * c[i]);
            x[i] = (-b[i] + Math.sqrt(discriminante)) / (2 * a[i]);
        }
    }
    
    const endTime = performance.now();
    const tiempoMs = endTime - startTime;
    console.log(`Tiempo de ejecución (JavaScript): ${tiempoMs.toFixed(2)} ms`);
}

calcularCuadraticaVectores();