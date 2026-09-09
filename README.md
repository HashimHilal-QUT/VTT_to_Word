# VTT to DOCX Transcript Converter
![VTT to Word Icon](ICON.webp)

<p align="center">
  <strong>Convert WebVTT transcripts into clean, research-ready Microsoft Word documents.</strong>
</p>

<p align="center">
  A lightweight, privacy-conscious Streamlit application for researchers, students, academics, UX/HCD practitioners, and anyone working with interview or meeting transcripts.
</p>

<p align="center">
  <a href="https://vtt-to-word.streamlit.app/"><strong>Launch the application</strong></a>
  ·
  <a href="#privacy-and-data-handling">Privacy</a>
  ·
  <a href="#contributing">Contribute</a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Application-FF4B4B?logo=streamlit&logoColor=white">
  <img alt="Output" src="https://img.shields.io/badge/Output-DOCX-2B579A?logo=microsoftword&logoColor=white">
  <img alt="Input" src="https://img.shields.io/badge/Input-WebVTT-4F46E5">
  <img alt="Licence" src="https://img.shields.io/badge/Licence-Add%20licence-lightgrey">
</p>

---

## Overview

**VTT to DOCX Transcript Converter** transforms WebVTT (`.vtt`) transcript files into readable Microsoft Word (`.docx`) documents. It removes VTT-specific timing and cue information while preserving the original conversational sequence and formatting speaker names for easier review and qualitative analysis.

### Why use it?

- Produce a clean Word transcript without manually removing VTT timestamps
- Preserve interviewer questions, participant responses, and speaker order
- Add an optional project-specific header to every page
- Generate page numbering in the format **Page X of Y**
- Use the hosted application without installing software or creating an account

> [!IMPORTANT]
> This converter formats existing transcript text. It does not perform speech-to-text transcription, correct transcript errors, summarise interviews, interpret responses, or perform thematic analysis.

---

## Features

### Transcript processing

- Upload `.vtt` transcript files through a browser
- Remove `WEBVTT` headers, timestamps, cue numbers, and supported metadata
- Preserve the original order of speaker turns
- Preserve interviewer prompts and participant responses
- Identify and format speaker labels

### Word document output

- Generate Microsoft Word `.docx` files
- Format speaker names in **bold**
- Format transcript text in **Calibri, 12 pt**
- Add an optional document header of up to **four lines**
- Repeat the document header on every page
- Add page numbering in the format **Page X of Y**

### Application design

- Run as a lightweight Streamlit application
- Operate without a transcript database
- Process transcript content for the requested conversion
- Provide the generated document directly for download

---

## Live Application

The application is deployed on Streamlit Community Cloud.

<p align="center">
  <a href="https://vtt-to-word.streamlit.app/">
    <img alt="Open application" src="https://img.shields.io/badge/Open%20VTT%20to%20DOCX%20Converter-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  </a>
</p>

No installation or account is required to use the hosted application.

---

## How It Works

```mermaid
flowchart TD
    A[Select a WebVTT file] --> B[Upload transcript]
    B --> C[Process transcript in memory]
    C --> D[Remove timestamps and cue numbers]
    D --> E[Remove supported VTT metadata]
    E --> F[Preserve speaker turns]
    F --> G[Apply Word formatting]
    G --> H[Generate DOCX]
    H --> I[Download Word document]
```

The converter focuses on document transformation rather than transcript interpretation. The wording and sequence of the supplied transcript are retained as closely as possible while VTT-specific structural content is removed.

---

## Usage

### 1. Add an optional document header

Enter up to four lines of information to be displayed in the header of every page.

```text
Researcher: Jane Smith
Project: Human-Centred Design Study
Participant: Participant A
Session: Follow-up Interview
```

The field is flexible, allowing you to use headings that suit your project or research requirements.

### 2. Upload a WebVTT transcript

Select a file with the `.vtt` extension. A typical input file looks like this:

```vtt
WEBVTT

1
00:00:02.020 --> 00:00:04.729
Interviewer: Thank you for joining the interview.

2
00:00:05.030 --> 00:00:07.009
Participant: Thank you. Happy to participate.
```

### 3. Convert the transcript

The application removes:

- The `WEBVTT` header
- Cue numbers
- Timestamps
- Supported VTT formatting tags and metadata

The original conversational sequence is preserved.

### 4. Download the Word document

Select **Download DOCX** after processing is complete. The generated document will contain formatted dialogue similar to:

> **Interviewer:** Thank you for joining the interview.
>
> **Participant:** Thank you. Happy to participate.

---

## Document Formatting

| Element | Output format |
|---|---|
| File type | Microsoft Word `.docx` |
| Body font | Calibri |
| Font size | 12 pt |
| Speaker names | Bold |
| Dialogue | Normal text |
| Speaker sequence | Preserved |
| Document header | Optional, maximum four lines |
| Header placement | Repeated on every page |
| Footer | Page numbering on every page |
| Page-number format | Page X of Y |

This formatting is intended to produce a clean, readable transcript suitable for research documentation and qualitative analysis.

---

## Preserving Interview Context

The converter preserves individual speaker turns rather than combining consecutive statements attributed to the same person.

This is important in research interviews because follow-up prompts, clarification questions, and participant responses provide context that may be lost if dialogue is merged.

### Example

> **Participant:** I found the interface easy to use.
>
> **Interviewer:** What specifically made it easy to use?
>
> **Participant:** The navigation was simple and I could quickly find what I needed.

This structure is useful for:

- Qualitative research
- Contextual Inquiry
- Human-Centred Design research
- User interviews
- Usability studies
- Thematic analysis
- Research coding
- Academic quotation and referencing

---

## Privacy and Data Handling

> [!NOTE]
> **The application is designed not to store or retain voice recordings, transcript content, or generated Word documents after conversion.** Uploaded content is processed for the purpose of generating the requested document, and the application does not require a transcript database.

No transcript content should be deliberately written to application logs or persistent storage. This statement must remain aligned with the deployed source code, application logging configuration, Streamlit hosting configuration, and any third-party services introduced in the future.

Users remain responsible for complying with applicable:

- Research ethics approvals
- Participant consent arrangements
- Institutional data-management policies
- Privacy and confidentiality requirements
- Data-retention obligations

Where required, anonymise or de-identify transcript data before processing or sharing it.

---

## Run the Streamlit App Locally

You can run the application on your own computer for development, testing, or private use.

### Prerequisites

Before you begin, make sure you have:

- **Python 3.9 or later**
- **pip**
- **Git**

You can verify Python is installed with:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### 1. Clone the repository

Open a terminal, PowerShell, or command prompt and run:

```bash
git clone https://github.com/HashimHilal-QUT/VTT_to_Word.git
```

Then move into the project folder:

```bash
cd VTT_to_Word
```

### 2. Create a virtual environment

Creating a virtual environment is recommended so the project dependencies remain isolated from your other Python projects.

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can activate the environment from Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the required packages

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

The application primarily requires:

```text
streamlit
python-docx
```

### 4. Start the Streamlit application

Run:

```bash
streamlit run app.py
```

Streamlit should open the application automatically in your default web browser. If it does not, open:

```text
http://localhost:8501
```

### 5. Use the application locally

Once the page is open:

1. Optionally enter up to four lines in the **Document Header** field.
2. Upload a `.vtt` transcript file.
3. Wait for the transcript to be processed.
4. Select **Download DOCX** to save the generated Word document.

The local version behaves in the same way as the hosted Streamlit application.

### 6. Stop the application

Return to the terminal where Streamlit is running and press:

```text
Ctrl + C
```

### Updating your local copy

If you cloned the repository previously and want the latest version, run:

```bash
git pull origin main
```

Then refresh dependencies if `requirements.txt` has changed:

```bash
pip install -r requirements.txt
```

### Troubleshooting

#### `streamlit` command not found

Make sure the virtual environment is activated, then run:

```bash
pip install streamlit
```

Alternatively, start Streamlit through Python:

```bash
python -m streamlit run app.py
```

#### `ModuleNotFoundError: No module named 'docx'`

Install the required package:

```bash
pip install python-docx
```

#### Port 8501 is already in use

Run Streamlit on another port:

```bash
streamlit run app.py --server.port 8502
```

Then open:

```text
http://localhost:8502
```


## Project Structure

```text
vtt-to-docx-streamlit/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

| File | Purpose |
|---|---|
| `app.py` | Streamlit interface, VTT processing, DOCX generation, headers, page numbering, and downloads |
| `requirements.txt` | Python package dependencies |
| `README.md` | Project documentation |
| `.gitignore` | Excludes local environments, cache files, and unnecessary generated files |

---

## Technology Stack

- **Python**
- **Streamlit**
- **python-docx**
- **Microsoft Word Open XML**
- **GitHub**
- **Streamlit Community Cloud**

---

## Intended Use

The converter may be useful for transcripts produced from:

- Research interviews
- Contextual Inquiry sessions
- Human-Centred Design studies
- UX research
- Usability testing
- Academic interviews
- Focus groups
- User-research sessions
- Meeting recordings
- Online interview platforms
- Video-conferencing transcription tools

Input must be supplied in WebVTT (`.vtt`) format.

---

### Word page fields

Page numbering uses the Microsoft Word `PAGE` and `NUMPAGES` fields and is displayed in the following format:

```text
Page 1 of 10
```

Microsoft Word normally calculates these fields when the document is opened. Some alternative DOCX viewers may not immediately refresh them.

---

## Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Submit a pull request with a clear description.

You can also open a GitHub Issue to report a problem or propose an improvement.

---


## Acknowledgements

Built by Hashim Hilal - Student QUT - Master of AI

<p align="center">
  <a href="https://vtt-to-word.streamlit.app/"><strong>Open VTT to DOCX Transcript Converter</strong></a>
</p>
