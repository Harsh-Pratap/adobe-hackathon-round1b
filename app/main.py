import os
from utils import load_text, save_json, timestamp_now
from document_parser import extract_sections
from relevance_ranker import Ranker

def main():
    persona = load_text("input/persona.txt")
    job = load_text("input/job.txt")
    os.makedirs("output", exist_ok=True)
    ranker = Ranker()
    results = {
        "persona": persona,
        "job": job,
        "timestamp": timestamp_now(),
        "documents": []
    }

    for pdf in os.listdir("input/documents"):
        if not pdf.lower().endswith(".pdf"):
            continue
        path = os.path.join("input/documents", pdf)
        secs = extract_sections(path)
        top = ranker.rank(persona, job, secs, top_k=5)
        results["documents"].append({
            "filename": pdf,
            "matched_sections": top
        })

    save_json(results, "output/results.json")

if __name__ == "__main__":
    main()
