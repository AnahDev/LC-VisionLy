use std::time::Instant;

fn main() {
    let n = 200;
    let a: Vec<f64> = vec![2.0; n];
    let b: Vec<f64> = vec![5.0; n];
    let c: Vec<f64> = vec![2.0; n];
    let mut x: Vec<f64> = vec![0.0; n];
    
    let iteraciones = 100000;
    
    let start_time = Instant::now();
    
    for _ in 0..iteraciones {
        for i in 0..n {
            let discriminante = (b[i] * b[i]) - (4.0 * a[i] * c[i]);
            x[i] = (-b[i] + discriminante.sqrt()) / (2.0 * a[i]);
        }
    }
    
    let duration = start_time.elapsed();
    println!("Tiempo de ejecución (Rust): {:.2} ms", duration.as_secs_f64() * 1000.0);
    
    // Esta linea obliga al compilador a no borrar el bucle
    println!("Control de optimización (Resultado en x[0]): {}", x[0]);
}