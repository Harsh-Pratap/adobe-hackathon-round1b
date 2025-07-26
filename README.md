
# Adobe Hackathon – Round 1B: Persona-Based Document Intelligence System

## 🎯 Objective
Build an offline system that, given a **persona** and a **job-to-be-done (JTBD)**, intelligently analyzes multiple PDFs and extracts the **most relevant sections** for that persona's needs. The system outputs a ranked JSON file showing matched sections for each document.

---

## 🧠 Approach

This solution uses **SentenceTransformers (MiniLM)** to embed both the persona's objective and sections of the documents in a shared vector space, and ranks them based on **cosine similarity**.

### Workflow:
1. **Text Extraction**: Extracts paragraphs and text blocks using PyMuPDF (`fitz`) from each PDF
2. **Embedding & Ranking**: Compares persona+JTBD query to document sections using `MiniLM-L6-v2` embeddings
3. **Relevance Scoring**: Cosine similarity scoring ranks the most contextually relevant sections
4. **Result Generation**: Outputs a ranked JSON for all documents

---

## 🛠️ Technologies Used

- Python 3.10
- [sentence-transformers (MiniLM)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- PyMuPDF (for PDF parsing)
- Scikit-learn (for cosine similarity)
- Docker (CPU-only, offline compatible)

---

## 📂 Folder Structure

```
adobe-hackathon-round1b/
├── app/
│   ├── main.py
│   ├── document_parser.py
│   ├── relevance_ranker.py
│   └── utils.py
├── Dockerfile
├── requirements.txt
├── README.md
├── input/
│   ├── persona.txt
│   ├── job.txt
│   └── documents/
│       └── sample_doc.pdf
├── output/
│   └── results.json
```

---

## ⚙️ How to Build and Run

### ✅ 1. Build the Docker Image

```bash
docker build --platform linux/amd64 -t pdf-intel:round1b .
```

### ✅ 2. Run the Container

#### Windows PowerShell
```powershell
docker run --rm -v "${PWD}\output:/app/output" pdf-intel:round1b
```

#### Linux/macOS (bash)
```bash
docker run --rm -v $(pwd)/output:/app/output pdf-intel:round1b
```

The output JSON will be generated in `output/results.json`.

---

## 🧾 Example Output Format

```json
{
  "persona": "...",
  "job": "...",
  "timestamp": "...",
  "documents": [
    {
      "filename": "doc1.pdf",
      "matched_sections": [
        {
          "rank": 1,
          "page": 3,
          "content": "...",
          "score": 0.78
        }
      ]
    }
  ]
}
```

---

## ✅ Constraints Met

| Constraint                     | Status |
|-------------------------------|--------|
| Runs on CPU (no GPU)          | ✅     |
| Model size ≤ 1 GB             | ✅     |
| No internet access required   | ✅     |
| Output generated < 60s        | ✅     |
| Works across domains (multi-PDF) | ✅  |

---

## 📝 Notes

- Model is downloaded and cached once inside Docker image
- Supports various document domains: legal, IT, HR, sales, etc.
- Easily extendable with more personas or domain-specific filters

---

> ✅ Built for **Adobe India Hackathon 2025 – “Connecting the Dots” Challenge**
