# Face Verify API

A face verification system built with FastAPI and InsightFace.
Upload two photos and the API will tell you if they belong to the same person.

---


##ScreenShots:
S1
<img width="1858" height="827" alt="image" src="https://github.com/user-attachments/assets/af1806f4-582b-4646-97d3-8b466f5390a6" />
S2
<img width="1852" height="588" alt="image" src="https://github.com/user-attachments/assets/655a548d-23f8-439a-a065-5805ea9c1132" />
S3
<img width="1830" height="897" alt="image" src="https://github.com/user-attachments/assets/a2874f5c-c02a-4a7a-80c9-cfda73b4fb09" />



## Tech Stack

- Python
- FastAPI
- InsightFace
- OpenCV
- NumPy
- ONNX Runtime

---

## Project Structure

```
FaceVerify/
│
├── app.py              # FastAPI server and routes
├── train.py            # Model loading script
├── test.py             # Face detection and comparison logic
├── requirements.txt    # All dependencies
└── README.md
```

---

## Setup

**Step 1 — Create a virtual environment**

```bash
python -m venv venv
```

**Step 2 — Activate it**

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

> First run will automatically download the `buffalo_l` model (~500MB).
> This is a one-time download saved at `C:\Users\<you>\.insightface\`

---

## Running the API

```bash
uvicorn app:server --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

---

## Testing via Swagger UI

1. Open `http://127.0.0.1:8000/docs` in your browser
2. Click **POST /verify**
3. Click **Try it out**
4. Upload **photo1** and **photo2**
5. Click **Execute**

---

## API Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Health check             |
| POST   | `/verify` | Compare two face photos  |

---

## Sample Response

```json
{
  "verification_result": "same person",
  "similarity_score": 0.7505,
  "bounding_box_image1": [130.5, 45.2, 310.8, 290.4],
  "bounding_box_image2": [95.1, 60.3, 280.6, 305.7]
}
```

### Response Fields

| Field | Description |
|---|---|
| `verification_result` | `"same person"` or `"different person"` |
| `similarity_score` | Float between 0 and 1 — higher means more similar |
| `bounding_box_image1` | Face coordinates detected in first photo `[x1, y1, x2, y2]` |
| `bounding_box_image2` | Face coordinates detected in second photo `[x1, y1, x2, y2]` |

---

## How It Works

1. Two photos are uploaded via the `/verify` endpoint
2. Each photo is saved temporarily on disk
3. InsightFace detects faces and extracts embeddings from both photos
4. Cosine similarity is computed between the two embeddings
5. If similarity score is above **0.60** → `same person`, else → `different person`

---

## Tips for Best Results

- Use clear, front-facing photos
- Good lighting improves accuracy
- Avoid very small or blurry images
- Supported formats: JPG, PNG
