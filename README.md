# 📄 VTT to DOCX Transcript Converter

A simple, privacy-conscious Streamlit application for converting **WebVTT (`.vtt`) transcript files** into clean, formatted **Microsoft Word (`.docx`) documents**.

The application is designed primarily for **researchers, students, academics, UX/HCD practitioners, and anyone working with interview or meeting transcripts**.

🌐 **Live Application:**  
https://vtt-to-word.streamlit.app/

---

## ✨ Features

- Upload and convert `.vtt` transcript files directly in your browser
- Generates a formatted Microsoft Word `.docx` document
- Removes WebVTT timestamps
- Removes VTT cue numbers
- Removes VTT metadata
- Preserves the original sequence of speaker turns
- Preserves interviewer questions and participant responses
- Automatically identifies and formats speaker names
- Speaker names are displayed in **bold**
- Transcript text is formatted using **Calibri, 12 pt**
- Supports an optional custom document header
- Custom document header supports up to **4 lines**
- Automatically adds page numbers to long transcripts
- Word footer uses the format **Page X of Y**
- No transcript content is intentionally stored
- No database is required

---

## 🚀 Live Demo

The application is deployed using **Streamlit Community Cloud**.

### Open the application

👉 **https://vtt-to-word.streamlit.app/**

No installation or account is required to use the online application.

---

## 📖 How to Use

### 1. Enter Document Header Information

The **Document Header** field is optional.

You can enter up to **4 lines of text** that will appear in the header of every page of the generated Word document.

For example:

```text
Researcher: Jane Smith
Project: Human-Centred Design Study
Participant: Participant A
Session: Follow-up Interview
```

The header is deliberately flexible so that researchers can use whatever information is appropriate for their project.

---

### 2. Upload a VTT File

Upload a WebVTT transcript with the `.vtt` extension.

A typical VTT transcript may look like:

```text
WEBVTT

1
00:00:02.020 --> 00:00:04.729
Interviewer: Thank you for joining the interview.

2
00:00:05.030 --> 00:00:07.009
Participant: Thank you. Happy to participate.
```

---

### 3. Convert the Transcript

The application processes the VTT transcript and removes:

- `WEBVTT` headers
- Cue numbers
- Timestamps
- Supported VTT formatting tags and metadata

The conversational sequence is retained.

---

### 4. Download the Word Document

After conversion, select:

**Download DOCX**

The resulting document will contain:

```text
Interviewer: Thank you for joining the interview.

Participant: Thank you. Happy to participate.
```

Speaker names are displayed in **bold**, while the transcript text remains in **Calibri 12 pt**.

---

## 📝 Word Document Formatting

Generated Word documents use the following formatting:

| Feature | Format |
|---|---|
| File type | Microsoft Word `.docx` |
| Font | Calibri |
| Font size | 12 pt |
| Speaker names | Bold |
| Dialogue | Normal |
| Speaker sequence | Preserved |
| Document header | Optional, maximum 4 lines |
| Header placement | Every page |
| Page numbering | Every page |
| Page number format | Page X of Y |

This formatting is intended to produce a clean and readable transcript suitable for research documentation and qualitative analysis.

---

## 🧠 Preserving Interview Context

The converter deliberately preserves individual **speaker turns** rather than combining all consecutive statements from the same speaker.

This is particularly important for research interviews because interviewer questions, follow-up prompts, clarification questions, and participant responses provide important context.

For example:

```text
Participant: I found the interface easy to use.

Interviewer: What specifically made it easy to use?

Participant: The navigation was simple and I could quickly find what I needed.
```

The application maintains this conversational sequence rather than combining participant responses into a single paragraph.

This makes the resulting documents more suitable for:

- Qualitative research
- Contextual Inquiry
- Human-Centred Design research
- User interviews
- Usability studies
- Thematic analysis
- Research coding
- Academic quoting and referencing

---

## 🔒 Privacy & Data Handling Notice

**This application does not store or retain any voice recordings, transcripts, or generated Word documents.**

Your data is processed in memory solely to perform the requested conversion and is automatically discarded immediately upon completion.

**No transcript content is saved to databases, logs, or persistent storage.**

Users should nevertheless follow their institution's research ethics, privacy, confidentiality, and data-handling requirements when processing research participant information.

---

## 🛡️ Data Processing Design

The application has been intentionally designed as a lightweight conversion utility.

The basic processing workflow is:

```text
User's Browser
      │
      ▼
Upload VTT Transcript
      │
      ▼
Streamlit Application
      │
      ▼
Process Transcript in Memory
      │
      ├── Remove VTT timestamps
      ├── Remove cue numbers
      ├── Remove metadata
      ├── Preserve speaker turns
      ├── Apply document formatting
      └── Generate DOCX
      │
      ▼
Download Word Document
      │
      ▼
Processing Complete
```

The application does not require a transcript database or persistent transcript storage.

---

## 💻 Running Locally

### Prerequisites

You will need:

- Python 3.9 or later
- pip

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/vtt-to-docx-streamlit.git
```

Navigate to the repository:

```bash
cd vtt-to-docx-streamlit
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will normally open the application at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project primarily uses:

```text
streamlit
python-docx
```

These dependencies are defined in:

```text
requirements.txt
```

---

## 📁 Project Structure

```text
vtt-to-docx-streamlit/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `app.py`

Contains:

- Streamlit user interface
- VTT parser
- Transcript processing
- DOCX generation
- Custom header generation
- Word page numbering
- Download functionality

### `requirements.txt`

Contains the Python package dependencies required by the application.

### `.gitignore`

Prevents local Python environments, cache files, and other unnecessary files from being committed to the repository.

---

## 🛠️ Technology Stack

- **Python**
- **Streamlit**
- **python-docx**
- **Microsoft Word Open XML**
- **GitHub**
- **Streamlit Community Cloud**

---

## 🎯 Intended Use

The application can be useful for converting transcripts generated from:

- Research interviews
- Contextual Inquiry sessions
- Human-Centred Design studies
- UX research
- Usability testing sessions
- Academic interviews
- Focus groups
- User research
- Meeting recordings
- Online interview platforms
- Video conferencing transcription tools

The converter expects transcripts to be supplied in the standard **WebVTT (`.vtt`) format**.

---

## ⚠️ Important Notes

### Transcript Accuracy

This application converts and formats existing transcript text.

It does **not**:

- Perform speech-to-text transcription
- Correct transcription errors
- Rewrite participant responses
- Summarise interviews
- Interpret participant statements
- Perform thematic analysis

The content of the original VTT transcript is retained as closely as possible while removing VTT-specific formatting information.

### Page Numbers

Page numbers are implemented using Microsoft Word fields:

```text
PAGE
NUMPAGES
```

They are displayed as:

```text
Page 1 of 10
```

Microsoft Word normally calculates these fields automatically when the document is opened.

Some alternative DOCX viewers may not immediately update Word fields.

---

## 🔬 Research Use

When using the application with research data, researchers remain responsible for ensuring that their use complies with applicable:

- Research ethics approvals
- Participant consent arrangements
- Institutional data-management policies
- Privacy requirements
- Confidentiality requirements
- Data retention policies

Where required, researchers should anonymise or de-identify transcript data before processing or sharing it.

---

## 🤝 Contributing

Suggestions, improvements, bug reports, and contributions are welcome.

You can contribute by:

1. Forking the repository
2. Creating a feature branch
3. Making your changes
4. Submitting a pull request

You can also open a GitHub Issue to report problems or suggest improvements.

---

## 💡 Future Enhancements

Potential future improvements may include:

- Additional document formatting options
- User-selectable fonts and font sizes
- Optional timestamps
- Custom page margins
- Multiple-file conversion
- Batch VTT processing
- Transcript preview before download
- TXT export
- PDF export
- Additional subtitle/transcript formats
- Speaker-name customisation
- Automatic anonymisation options

---

## 📜 License

Add the appropriate open-source licence for your project here.

For example:

```text
MIT License
```

If this repository is intended for public reuse, adding a `LICENSE` file is recommended.

---

## 🌐 Application

**VTT to DOCX Transcript Converter**

👉 https://vtt-to-word.streamlit.app/

Built with Python and Streamlit.
