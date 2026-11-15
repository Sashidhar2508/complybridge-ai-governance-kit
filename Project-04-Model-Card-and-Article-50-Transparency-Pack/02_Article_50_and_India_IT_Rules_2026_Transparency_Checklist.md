# EU AI Act Article 50 & India IT Amendment Rules 2026 Transparency Checklist

Use this operational checklist to verify transparency and synthetic-content compliance across customer-facing AI features.

---

## 1. Conversational AI User Disclosure (EU AI Act Article 50(1) — Live Since 2 Aug 2026)
* [ ] **Upfront Banner:** Every customer-facing chatbot or voice agent displays a clear disclosure (*"You are chatting with an AI assistant"*) before the first user input.
* [ ] **No Dark Patterns:** Disclosure is visible in plain language on both desktop and mobile viewports without requiring users to hover or open a buried policy link.
* [ ] **Human Escalation Option:** Users can type `"agent"` or click a visible button to escalate to a human support representative.

---

## 2. Machine-Readable Synthetic Content Marking (EU AI Act Article 50(2) — 2 Dec 2026 Legacy Deadline)
* [ ] **Provider vs. Deployer Check:** Identify every feature where your SaaS product generates synthetic text, images, audio, or video under your own brand (making you a **Provider** under Article 50(2)).
* [ ] **Layered Technical Marking:** Verify that generated media embeds tamper-evident provenance metadata (such as **C2PA Content Credentials**) alongside imperceptible watermarking, aligned with the July 2026 EU Code of Practice.
* [ ] **Pipeline Preservation Test:** Confirm that image compression, CDN caching, or PDF export pipelines do not strip C2PA metadata from upstream model outputs.

---

## 3. Synthetically Generated Information (SGI) Labelling (India IT Amendment Rules 2026 — Effective 20 Feb 2026)
* [ ] **Prominent Visual / Audio Label:** Any synthetic visual, audio, or audio-visual output hosted or distributed via Indian intermediary platforms carries a clear, prominent label identifying it as synthetically generated.
* [ ] **Anti-Tampering Safeguard:** Platform upload and sharing workflows block the removal or suppression of permanent SGI provenance identifiers.
* [ ] **Harmful Deepfake Prevention:** Automated filters and acceptable-use warnings block non-consensual intimate imagery, identity impersonation, and fabricated official records.
