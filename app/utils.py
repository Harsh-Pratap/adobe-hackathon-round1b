import os, json, datetime

def load_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read().strip()

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def timestamp_now():
    return datetime.datetime.utcnow().isoformat() + 'Z'
