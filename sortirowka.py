import os                                                    
import shutil                                                                                      
from pathlib import Path                                                                               
                                                                                                     
# ---                                                          
folder_path = str(Path.home() / "Downloads")

print("=== Сортировщик файлов v1.0 ===")
print("Раскладываю файлы по папкам (Video, Images, Audio и т.д.)\n")

folder_base = input("Куда сортировать файлы? (Полный путь): ")


if not os.path.exists(folder_path):
    print(f"ОШИБКА: Папка загрузок не найдена. ПРОВЕРЬ ПУТЬ: {folder_path}")
    exit()

if not os.path.exists(folder_base):
    print("ОШИБКА: Такой папки нет, ПРОВЕРЬ ПУТЬ.")
    exit()
# ---


# ---
extensions = {
    #ВИДЕО
    ".mp4": "Video",
    ".avi": "Video",
    ".mkv": "Video",
    ".mov": "Video",
    ".wmv": "Video",
    ".flv": "Video",
    ".webm": "Video",
    ".m4v": "Video",
    ".3gp": "Video",
    ".mpg": "Video",
    ".mpeg": "Video",
    ".m2ts": "Video",
    ".vob": "Video",
    ".ts": "Video",

    #КАРТИНКИ И ИЗОБРАЖЕНИЕ
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",
    ".ico": "Images",
    ".tiff": "Images",
    ".heic": "Images",
    ".raw": "Images",
    ".psd": "Images",
    ".ai": "Images",
    ".xcf": "Images",
    ".heif": "Images",

    #АУДИО 
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".aiff": "Audio",
    ".opus": "Audio",
    ".wma": "Audio",
    ".mka": "Audio",

    #ДОКУМЕНТЫ
    ".doc": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".odt": "Documents",
    ".csv": "Documents",
    ".epub": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".pdf": "Documents",
    ".pages": "Documents",
    ".numbers": "Documents",
    ".key": "Documents",
    ".mobi": "Documents",
    ".fb2": "Documents",

    #АРХИВЫ
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives", 
    ".tgz": "Archives",
    ".cab": "Archives",
    ".lz": "Archives",
    ".zst": "Archives",
    ".lzma": "Archives",
    ".z": "Archives",

    #КОД И ТЕКСТ. ФАЙЛЫ 
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".sh": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".md": "Code",
    ".java": "Code",
    ".php": "Code",
    ".sql": "Code",
    ".yaml": "Code",
    ".yml": "Code",
    ".toml": "Code",
    ".tsx": "Code",
    ".jsx": "Code",
    ".rs": "Code",
    ".go": "Code",
    ".kt": "Code",
    ".swift": "Code",
    ".rb": "Code",
    ".ini": "Code",
    ".cfg": "Code",
    ".env": "Code",
    ".bat": "Code",
    ".ps1": "Code",

    #Инсталляторы и образы
    ".exe": "Installers",
    ".iso": "ISO",
    ".msi": "Installers",
    ".deb": "Installers",
    ".rpm": "Installers",
    ".apk": "Installers",
    ".pkg": "Installers",
    ".appimage": "Installers",
    ".dmg": "Installers",

    #Базы данных и прочее
    ".db": "Databases",
    ".sqlite": "Databases",
    ".sqlite3": "Databases",
    ".mdb": "Databases",
    ".accdb": "Databases",
    ".bak": "Backups",

    #ШРИФТЫ 
    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
    ".woff2": "Fonts",

    #Торренты
    ".torrent": "Torrents"


}
# ---


# --- 
files = os.listdir(folder_path)
count = 0

for file_name in files:
    name, ext = os.path.splitext(file_name)

    if ext in extensions:
        target_folder = extensions[ext]
        target_path = os.path.join(folder_base, target_folder)

        os.makedirs(target_path, exist_ok=True)

        dest_file = os.path.join(target_path, file_name)
        if os.path.exists(dest_file):
            counter = 1
            while os.path.exists(dest_file):
                new_name = f"{name} ({counter}){ext}"
                dest_file = os.path.join(target_path, new_name)
                counter += 1 
 
        try:
            shutil.move(os.path.join(folder_path, file_name), dest_file)
            count += 1
        except Exception as e:
            print(f"❌ НЕ УДАЛОСЬ ПЕРЕМЕСТИТЬ {file_name}. ПРИЧИНА: {e}")
   
if count > 0:
    print(f"✅ ГОТОВО! Отсортировано файлов: {count}")
else:
    print("❌ В папке не нашлось файлов для сортировки.") 
# ---

