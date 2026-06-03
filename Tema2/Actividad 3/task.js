{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Ejecutar Lenguaje L",
            "type": "shell",
            // 1. Quitamos el '3' ya que en Windows casi siempre es solo 'python'
            "command": "python", 
            "args": [
                // 2. Aquí debes poner el nombre REAL del script analizador de tu grupo
                // Si todavía no lo han programado, pon el nombre del archivo de prueba
                "mi_analizador.py", 
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        }
    ]
}