def eliminar_recursividad_izq(no_terminal, producciones):
    alphas = []
    betas = []
    
    # 1. Separar producciones recursivas (alpha) y no recursivas (beta)
    for prod in producciones:
        if prod.startswith(no_terminal):
            alphas.append(prod[len(no_terminal):].strip())
        else:
            betas.append(prod)
            
    # 2. Generar las nuevas reglas si hay recursividad
    if not alphas:
        return {no_terminal: producciones}
        
    nuevo_nt = no_terminal + "'"
    nuevas_reglas = {
        no_terminal: [f"{beta} {nuevo_nt}" for beta in betas],
        nuevo_nt: [f"{alpha} {nuevo_nt}" for alpha in alphas] + ["ε"]
    }
    
    return nuevas_reglas

# Prueba del caso práctico
reglas_L = ["L , id", "id"]
resultado = eliminar_recursividad_izq("L", reglas_L)

for nt, prods in resultado.items():
    print(f"{nt} -> {' | '.join(prods)}")