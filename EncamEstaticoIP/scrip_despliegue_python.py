import os
from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab

# Directorio donde se encuentran los archivos de configuración
CONFIG_DIR = "/home/andresmasa/Documents/TFG/EncamEstaticoIP"

# Función para crear una máquina en el laboratorio
def crear_maquina(lab, nombre, imagen, interfaces):
    print(f"Creando {nombre}...")
    maquina = lab.new_machine(nombre, **{"image": imagen})
    for interfaz in interfaces:
        lab.connect_machine_to_link(maquina.name, interfaz)
    return maquina

# Función para configurar una máquina con un archivo de inicio
def configurar_maquina(maquina, archivo_inicio):
    print(f"Configurando {maquina.name}...")
    lab.create_file_from_path(os.path.join(CONFIG_DIR, archivo_inicio), f"{maquina.name}.startup")

# Crear instancia del laboratorio
lab = Lab("kathara-python")


#Crear y configurar r1
r1 = crear_maquina(lab, "r1", "kathara/base", ["r1-r2", "A"])
configurar_maquina(r1, "r1.startup")

# Crear y configurar r2
r2 = crear_maquina(lab, "r2", "kathara/base", ["r1-r2", "r2-r3", "r2-r4"])
configurar_maquina(r2, "r2.startup")

# Crear y configurar r3
r3 = crear_maquina(lab, "r3", "kathara/base", ["r2-r3", "B"])
configurar_maquina(r3, "r3.startup")

# Crear y configurar r4
r4 = crear_maquina(lab, "r4", "kathara/base", ["r2-r4", "C"])
configurar_maquina(r4, "r4.startup")

# Crear y configurar pc1
pc1 = crear_maquina(lab, "pc1", "kathara/base", ["A"])
configurar_maquina(pc1, "pc1.startup")

# Crear y configurar pc2
pc2 = crear_maquina(lab, "pc2", "kathara/base", ["B"])
configurar_maquina(pc2, "pc2.startup")

# Crear y configurar pc3
pc3 = crear_maquina(lab, "pc3", "kathara/base", ["C"])
configurar_maquina(pc3, "pc3.startup")


# Desplegar el laboratorio
Kathara.get_instance().deploy_lab(lab)

# Conectar a todas las máquinas
#for maquina in [r1, r2, r3, r4, pc1, pc2, pc3]:
#    Kathara.get_instance().connect_tty(maquina.name, lab_name=lab.name)
