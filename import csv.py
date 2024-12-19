import csv
import os

# Lokasi file CSV yang diekspor dari DBeaver
input_csv = "notification_template_202412191039.csv"  # Ganti dengan nama file CSV Anda

# Direktori output untuk file HTML
output_dir = "output_html"
os.makedirs(output_dir, exist_ok=True)

# Membaca CSV dan membuat file HTML
with open(input_csv, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Membaca file sebagai dictionary
    for row in reader:
        # Ambil kolom filename dan message_content
        filename = row['filename']
        html_content = row['message_content']
        
        # Buat nama file HTML
        output_path = os.path.join(output_dir, f"{filename}.html")
        
        # Tulis konten HTML ke file
        with open(output_path, mode='w', encoding='utf-8') as html_file:
            html_file.write(html_content)

print(f"File HTML berhasil dibuat di folder: {output_dir}")