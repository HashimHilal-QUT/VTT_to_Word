import re
from io import BytesIO

import streamlit as st
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH


FONT_NAME = "Calibri"
FONT_SIZE = 12


def set_document_font(document):
    style = document.styles["Normal"]

    style.font.name = FONT_NAME
    style.font.size = Pt(FONT_SIZE)

    style.element.rPr.rFonts.set(qn("w:ascii"), FONT_NAME)
    style.element.rPr.rFonts.set(qn("w:hAnsi"), FONT_NAME)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), FONT_NAME)


def set_run_font(run, bold=False):
    run.font.name = FONT_NAME
    run.font.size = Pt(FONT_SIZE)
    run.bold = bold

    if run._element.rPr is None:
        run._element.get_or_add_rPr()

    run._element.rPr.rFonts.set(qn("w:ascii"), FONT_NAME)
    run._element.rPr.rFonts.set(qn("w:hAnsi"), FONT_NAME)
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT_NAME)


def is_timestamp(line):
    pattern = (
        r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->\s+"
        r"\d{2}:\d{2}:\d{2}\.\d{3}"
    )

    return re.match(pattern, line.strip()) is not None


def parse_vtt(vtt_text):
    lines = vtt_text.splitlines()

    transcript_blocks = []
    current_block = []

    for raw_line in lines:
        line = raw_line.strip()

        if not line:
            if current_block:
                transcript_blocks.append(" ".join(current_block))
                current_block = []
            continue

        if line.upper() == "WEBVTT":
            continue

        if line.isdigit():
            continue

        if is_timestamp(line):
            continue

        if line.startswith(("NOTE", "STYLE", "REGION")):
            continue

        line = re.sub(r"<[^>]+>", "", line)

        current_block.append(line)

    if current_block:
        transcript_blocks.append(" ".join(current_block))

    return transcript_blocks


def validate_header_text(header_text):
    """
    Limit header content to a maximum of 4 non-empty lines.
    """

    lines = [
        line.strip()
        for line in header_text.splitlines()
        if line.strip()
    ]

    if len(lines) > 4:
        return False, lines

    return True, lines


def add_document_header(document, header_text):
    """
    Add custom user-entered text to the Word header.
    Maximum 4 lines.
    """

    section = document.sections[0]
    header = section.header

    paragraph = header.paragraphs[0]
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)

    valid, lines = validate_header_text(header_text)

    if not valid:
        raise ValueError(
            "Document header can contain a maximum of 4 lines."
        )

    for index, line in enumerate(lines):
        run = paragraph.add_run(line)
        set_run_font(run)

        if index < len(lines) - 1:
            run.add_break()


def add_field(run, field_name):
    """
    Add a Microsoft Word field such as PAGE or NUMPAGES.
    """

    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")

    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = field_name

    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")

    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")

    run._r.append(begin)
    run._r.append(instr)
    run._r.append(separate)
    run._r.append(end)


def add_page_numbers(document):
    """
    Add centered footer:
    Page 1 of 10
    """

    for section in document.sections:
        footer = section.footer

        paragraph = footer.paragraphs[0]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = paragraph.add_run("Page ")
        set_run_font(run)

        page_run = paragraph.add_run()
        set_run_font(page_run)
        add_field(page_run, "PAGE")

        run = paragraph.add_run(" of ")
        set_run_font(run)

        total_run = paragraph.add_run()
        set_run_font(total_run)
        add_field(total_run, "NUMPAGES")


def create_docx(transcript_blocks, header_text):
    document = Document()

    set_document_font(document)

    if header_text.strip():
        add_document_header(
            document,
            header_text
        )

    add_page_numbers(document)

    for block in transcript_blocks:
        paragraph = document.add_paragraph()

        paragraph.paragraph_format.space_after = Pt(6)
        paragraph.paragraph_format.space_before = Pt(0)

        match = re.match(r"^([^:]+):\s*(.*)$", block)

        if match:
            speaker = match.group(1).strip()
            dialogue = match.group(2).strip()

            speaker_run = paragraph.add_run(f"{speaker}: ")
            set_run_font(speaker_run, bold=True)

            dialogue_run = paragraph.add_run(dialogue)
            set_run_font(dialogue_run)

        else:
            run = paragraph.add_run(block)
            set_run_font(run)

    output = BytesIO()
    document.save(output)
    output.seek(0)

    return output


# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------

st.set_page_config(
    page_title="VTT to DOCX Converter",
    page_icon="📄",
    layout="centered"
)


st.title("VTT to DOCX Transcript Converter")

st.write(
    "Convert WebVTT (.vtt) interview transcripts into clean "
    "Microsoft Word (.docx) documents."
)

st.info(
    "Speaker turns are preserved. VTT timestamps, cue numbers, "
    "and metadata are removed."
)


# ---------------------------------------------------------
# Document Header
# ---------------------------------------------------------

st.subheader("Document Header")

st.caption(
    "Optional. Enter up to 4 lines of text. "
    "This text will appear in the Word document header on every page."
)

header_text = st.text_area(
    "Header text:",
    height=120,
    placeholder=(
        "Researcher Name: Jane Smith\n"
        "Research Project: Human-Centred Design Study\n"
        "Participant: Participant A\n"
        "Interview Type: Follow-up Interview"
    )
)


# Validate header immediately
header_valid, header_lines = validate_header_text(header_text)

if not header_valid:
    st.error(
        "The document header is limited to a maximum of 4 lines. "
        "Please remove one or more lines."
    )
else:
    st.caption(
        f"Header lines used: {len(header_lines)} / 4"
    )


# ---------------------------------------------------------
# File Upload
# ---------------------------------------------------------

st.subheader("Upload Transcript")

uploaded_file = st.file_uploader(
    "Upload VTT transcript",
    type=["vtt"]
)


if uploaded_file is not None:

    try:
        vtt_text = uploaded_file.read().decode("utf-8-sig")

        transcript = parse_vtt(vtt_text)

        if len(transcript) == 0:
            st.error(
                "No transcript content was found in the uploaded VTT file."
            )

        elif not header_valid:
            st.warning(
                "Please correct the document header before downloading."
            )

        else:
            st.success(
                f"Transcript loaded successfully. "
                f"{len(transcript)} transcript blocks found."
            )

            docx_file = create_docx(
                transcript,
                header_text
            )

            output_filename = (
                uploaded_file.name.rsplit(".", 1)[0]
                + ".docx"
            )

            st.download_button(
                label="Download DOCX",
                data=docx_file,
                file_name=output_filename,
                mime=(
                    "application/"
                    "vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                ),
                use_container_width=True
            )

    except UnicodeDecodeError:
        st.error(
            "The uploaded file could not be read as a UTF-8 VTT file."
        )

    except Exception as error:
        st.error(f"An error occurred: {error}")


# ---------------------------------------------------------
# Footer Disclaimer
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align: center;
        color: black;
        font-size: 0.85rem;
        padding-top: 10px;
        padding-bottom: 20px;
    ">
        <strong>Privacy & Data Handling Notice:</strong>
        This application does not store or retain any voice recordings, transcripts, or generated Word documents.
        Your data is processed in memory solely to perform the requested conversion and is automatically discarded immediately upon completion.             
        No transcript content is saved to databases, logs, or persistent storage.
    </div>
    """,
    unsafe_allow_html=True
)