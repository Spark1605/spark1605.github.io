import os
import json

QUESTIONBANKS_DIR = 'files/questionbanks'
PDF_DIR = 'files/pdf'
IMAGES_DIR = 'files/questionbanks'
JSON_OUTPUT_PATH = 'resources/resources.json'
BASE_URL = 'https://sprk-web.github.io'

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext == '.json':
        return 'site'
    elif ext == '.pdf':
        return 'pdf'
    elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']:
        return 'image'
    else:
        return 'unknown'

def scan_folder(folder_path):
    resources = []
    if not os.path.exists(folder_path):
        return resources
        
    for filename in os.listdir(folder_path):
        if filename.startswith('.'):
            continue
            
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_type = get_file_type(filename)
            
            web_path = f"{BASE_URL}/{folder_path}/{filename}"
            
            resources.append({
                "name": filename,
                "type": file_type,
                "path": web_path
            })
    return resources

def main():
    all_resources = []
    all_resources.extend(scan_folder(QUESTIONBANKS_DIR))
    all_resources.extend(scan_folder(PDF_DIR))
    all_resources.extend(scan_folder(IMAGES_DIR))
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(JSON_OUTPUT_PATH), exist_ok=True)
    
    # Write the structured data to resources.json
    with open(JSON_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_resources, f, indent=2, ensure_ascii=False)
        

if __name__ == "__main__":
    main()
