const std = @import("std");
const time = std.time;
const math = std.math;

pub fn main() !void {
    const n = 200;
    
    // En Zig la gestión de memoria es explícita. Usamos el asignador nativo de Linux.
    const allocator = std.heap.page_allocator;
    
    const a = try allocator.alloc(f64, n);
    const b = try allocator.alloc(f64, n);
    const c = try allocator.alloc(f64, n);
    var x = try allocator.alloc(f64, n); // Este sí se queda como var porque modificamos sus elementos dentro del bucle
    
    // Aseguramos liberar la memoria al terminar el programa
    defer allocator.free(a);
    defer allocator.free(b);
    defer allocator.free(c);
    defer allocator.free(x);
    
    @memset(a, 2.0);
    @memset(b, 5.0);
    @memset(c, 2.0);
    
    const iteraciones = 100000;
    
    const start_time = time.nanoTimestamp();
    
    var k: usize = 0;
    while (k < iteraciones) : (k += 1) {
        var i: usize = 0;
        while (i < n) : (i += 1) {
            const discriminante = (b[i] * b[i]) - (4.0 * a[i] * c[i]);
            x[i] = (-b[i] + math.sqrt(discriminante)) / (2.0 * a[i]);
        }
    }
    
    const end_time = time.nanoTimestamp();
    const tiempo_ms = @as(f64, @floatFromInt(end_time - start_time)) / 1_000_000.0;
    
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Tiempo de ejecución (Zig): {d:.2} ms\n", .{tiempo_ms});
    try stdout.print("Control de optimización (Resultado en x[0]): {d:.1}\n", .{x[0]});
}