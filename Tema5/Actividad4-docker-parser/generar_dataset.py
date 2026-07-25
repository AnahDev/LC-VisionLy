import os

os.makedirs("dataset", exist_ok=True)

for i in range(1, 11):
    num_networks = i * 3
    content = f"# Configuración de Red Docker Compose - Test {i}\nversion: '3.8'\n\nservices:\n"
    
    for s in range(1, i + 2):
        content += f"  app_service_{s}:\n"
        content += f"    image: nginx:alpine\n"
        content += f"    networks:\n"
        for n in range(1, min(s + 1, num_networks + 1)):
            content += f"      - net_interface_{n}\n"

    content += "\nnetworks:\n"
    for n in range(1, num_networks + 1):
        content += f"  net_interface_{n}:\n"
        content += f"    driver: bridge\n"
        content += f"    ipam:\n"
        content += f"      config:\n"
        content += f"        - subnet: 10.{n}.0.0/16\n"
        content += f"          gateway: 10.{n}.0.1\n"

    with open(f"dataset/docker-compose-{i}.yml", "w") as f:
        f.write(content)

print("Dataset de 10 archivos generado en 'dataset/'")
