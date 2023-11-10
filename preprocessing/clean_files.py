import os
import time

# Pasta onde os arquivos estão localizados
input_folder = "output_files"

# Pasta onde os arquivos limpos serão salvos
output_folder_clean = "output_folder_clean"

# Certifica-se de que a pasta de saída existe
if not os.path.exists(output_folder_clean):
    os.makedirs(output_folder_clean)

# Itera sobre cada arquivo no diretório
for filename in os.listdir(input_folder):
    time.sleep(2)
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder_clean, filename)

        # Ler o conteúdo do arquivo
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Filtrar linhas não vazias
        non_empty_lines = [line.strip() for line in lines if line.strip()]

        # Escrever de volta no arquivo no diretório de saída
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(non_empty_lines))

        print(f"Linhas em branco removidas e arquivo salvo em {output_file_path}")
