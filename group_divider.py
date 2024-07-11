import random
import json
import csv
import sys
import os
import platform

celeste = "\033[96m"
reset = "\033[0m"

# Reads config.json
def read_config(config_file):
  with open(config_file, 'r') as file:
    config = json.load(file)
  return config

# Reads input files
def read_csv(file_path):
  with open(file_path, 'r') as file:
    reader = csv.reader(file)
    data = [row[0] for row in reader]
  return data

def main(config_file):
  config = read_config(config_file)

  students = read_csv(config['students_file'])
  topics = read_csv(config['topics_file'])
  group_size = config['group_size']
  output_file = config['output_file']

  random.shuffle(students)
  random.shuffle(topics)

  group_number = 1

  with open(output_file, 'w') as file:
    for i in range(0, len(students), group_size):
      group = students[i:i + group_size]
      topic = topics[group_number % len(topics)]
      file.write(f"[Grupo {group_number} - Tema: {topic}]\n")
      for student in group:
        file.write(f"{student}\n")
      file.write("\n")
      group_number += 1

def main(config_file):
    # Tu lógica actual para generar grupos y escribir en el archivo
    config = read_config(config_file)

    students = read_csv(config['students_file'])
    topics = read_csv(config['topics_file'])
    group_size = config['group_size']
    output_file = config['output_file']

    random.shuffle(students)
    random.shuffle(topics)

    group_number = 1

    with open(output_file, 'w') as file:
        for i in range(0, len(students), group_size):
            group = students[i:i + group_size]
            topic = topics[group_number % len(topics)]
            file.write(f"[Grupo {group_number} - Tema: {topic}]\n")
            for student in group:
                file.write(f"{student}\n")
            file.write("\n")
            group_number += 1

    if platform.system() == 'Windows':
        os.system('pause')
    else:
        input("Press Enter to exit")

def launch_english_menu():
  print("\nWelcome to Group Divider! This software, created in an afternoon, allows you to randomly divide groups by selecting from a list of people and topics.")
  print("\nIf you haven't already, I encourage you to check the README.md to learn how to use this.")

  print(f"\n{celeste}Select an option{reset}")
  print("1. Run program\n2. Exit")
  option = input()

  if option == "1":
    main('./config.json')
  elif option == "2":
    sys.exit()
  else:
    print("Invalid input")

def launch_spanish_menu():
  print("\n¡Bienvenido a Group Divider! Este software, creado en una tarde, te permite dividir grupos al azar seleccionando de una lista de personas y temas.")
  print("\nSi aún no lo has hecho, te animo a que consultes el README.md para aprender a usar esto.")

  print(f"\n{celeste}Selecciona una opción{reset}")
  print("1. Ejecutar programa\n2. Salir")
  option = input()

  if option == "1":
    main('./config.json')
  elif option == "2":
    sys.exit()
  else:
    print("Invalid input")
  

while True:
  print(f"\n{celeste}Select a language - Seleccione un idioma{reset}\n1. English\n2. Español")
  language = input()

  if language == "1":
    launch_english_menu()
    break
  elif language == "2":
    launch_spanish_menu()
    break
  else:
    print("Invalid input - Entrada invalida")