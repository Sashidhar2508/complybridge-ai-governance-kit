# Advisory Decision Log: Project 04 (Model Card & Article 50 Transparency Pack)

This log records the reasoning behind key transparency and Model Card design choices in `Project 04`.

---

## Decision 01: Separating Article 50(1) Human Notice from Article 50(2) Machine-Readable Marking
* **Context:** Product teams frequently assume that adding a *"Powered by AI"* footer satisfies all EU AI Act Article 50 obligations.
* **Decision:** Split the transparency checklist into distinct workflows for **Article 50(1)** (upfront user notification on conversational bots) and **Article 50(2)** (machine-readable technical watermarking/C2PA provenance on synthetic text, image, audio, and video outputs).
* **Reasoning:** Text banners alone do not satisfy Article 50(2) for synthetic media providers, and backend C2PA metadata alone does not satisfy Article 50(1) for conversational interfaces. Separating them prevents incomplete implementations.

## Decision 02: Testing Media Compression & CDN Pipelines for Provenance Stripping
* **Context:** Upstream image/audio APIs increasingly attach C2PA Content Credentials by default, yet downstream SaaS apps routinely lose those credentials during image resizing, format conversion, or CDN optimization.
* **Decision:** Added a mandatory **Pipeline Preservation Test** to `02_Article_50_and_India_IT_Rules_2026_Transparency_Checklist.md`.
* **Reasoning:** Under both the EU AI Act (July 2026 Code of Practice) and India's IT Amendment Rules 2026, platforms are explicitly barred from stripping permanent synthetic-content identifiers. Verifying end-to-end persistence closes a common engineering blind spot.

## Decision 03: Embedding Patent & Open-Source License Attribution Directly in the Model Card
* **Context:** Model Cards traditionally focus only on accuracy and bias metrics, leaving Legal and Procurement guessing about commercial licensing and patent indemnity.
* **Decision:** Added Section 1 (`Intellectual Property, Patent & License Status`) to `01_Standard_AI_Model_Card_Template.docx`.
* **Reasoning:** Putting model license terms, proprietary RAG boundaries, and upstream patent indemnity status on page 1 of the Model Card lets enterprise buyers clear technical and legal reviews from a single artefact.
