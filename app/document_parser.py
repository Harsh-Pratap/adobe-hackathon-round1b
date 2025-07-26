import fitz

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block: continue
            text = " ".join(span["text"] for line in block["lines"] for span in line["spans"]).strip()
            if len(text) < 20: continue
            sections.append({
                "page": page_num,
                "content": text
            })
    return sections
