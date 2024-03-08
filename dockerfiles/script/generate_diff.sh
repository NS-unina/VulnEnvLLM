#!/bin/bash

# Cartella contenente i Dockerfile originari
folder1="../fixed"

# Cartella contenente i Dockerfile modificati
folder2="../with-llms"

# Creazione della cartella per i file di diff
diff_folder="../diffs"
mkdir -p "$diff_folder"

# Trova tutti i Dockerfile nelle sottocartelle di folder1 e confrontali con i corrispondenti in folder2
find "$folder1" -type f -name Dockerfile | while read -r file; do
    # Costruzione del percorso relativo per folder2
    relative_path="${file#$folder1}"
    file2="$folder2$relative_path"

    # Controlla se il file esiste in folder2
    if [ -f "$file2" ]; then
        # Esegue il diff e salva il risultato in un file nella cartella dei diff
        diff_result="$(diff "$file" "$file2")"
        if [ -n "$diff_result" ]; then 
            # Estrai il nome della cartella padre
            parent_folder=$(basename "$(dirname "$file")")
            # Crea un file di diff nella cartella diff
            echo "$diff_result" > "$diff_folder/${parent_folder}_diff.txt"
        fi
    fi
done
