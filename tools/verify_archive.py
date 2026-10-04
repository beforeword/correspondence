"""Check preserved wording, source files, record boundaries and local links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify():
    baseline = json.loads((ROOT / "data/integrity.json").read_text())
    xs = json.loads((ROOT / "data/researchers.json").read_text())
    catalog = json.loads((ROOT / "catalog.json").read_text())
    assert len(xs) == 24, "Expected 24 researcher letters"
    assert len(catalog["letters"]) == catalog["letter_count"] == 27
    assert len({x["id"] for x in catalog["letters"]}) == 27
    assert sum(x["sending"]["date"] is None for x in xs) == 20
    assert {x["id"] for x in xs if x["sending"]["forwarding_requested"]} == {"sutskever", "hassabis", "russell"}
    assert all(x["sending"]["timezone"] is None for x in xs)
    for x in xs:
        base = ROOT / "letters/researchers" / x["id"]
        record = json.loads((base / "record.json").read_text())
        original = baseline["researcher_letters"][x["id"]]
        assert original["subject_en"] == x["subject_en"], x["id"] + ": sent subject changed"
        assert original["body_sha256_utf8"] == sha(("\n\n".join(x["body_en"]) + "\n").encode()), x["id"] + ": sent body changed"
        assert record["sending"] == x["sending"]
        for edition in record["editions"]:
            lang = edition["language"]
            body = "\n\n".join(x["body_" + lang]) + "\n"
            assert edition["body_paragraphs"] == x["body_" + lang]
            assert edition["subject"] == x["subject_" + lang]
            assert edition["body_sha256_utf8"] == sha(body.encode())
            assert (base / edition["text_file"]).read_text().split("\n\n", 1)[1] == body
            page = (base / edition["file"]).read_text()
            rendered_body = page.split("\n\n---\n\n", 2)[1].replace("  \n", "\n").replace("\\+", "+") + "\n"
            assert rendered_body == body, x["id"] + ": Markdown wording differs"
        for e in record["evidence"]:
            assert sha((base / e["file"]).read_bytes()) == e["sha256"]
    for path, digest in baseline["files"].items():
        assert sha((ROOT / path).read_bytes()) == digest, "Preserved file changed: " + path
    for company in ["openai", "anthropic", "xai"]:
        base = ROOT / "letters/companies" / company
        record = json.loads((base / "record.json").read_text())
        assert record["sending"]["date"] == "2026-10-04"
        assert record["sending"]["record_basis"] == "author_statement"
        assert not record["status"]["substantive_response_published"]
        for ed in record["editions"]:
            text = (base / ed["path"]).read_text()
            assert sha((base / ed["path"]).read_bytes()) == ed["sha256"]
            page = (base / ("README.md" if ed["language"] == "en" else "README.ru.md")).read_text()
            displayed = page.split("\n\n---\n\n", 2)[1]
            displayed = re.sub(r"(?m)^#{3,4} ", "", displayed)
            displayed = re.sub(r"\[(https?://[^\]]+)\]\(\1\)", r"\1", displayed)
            displayed = re.sub(r"\\([\\`*_{}\[\]<>#!|.])", r"\1", displayed)
            assert displayed.rstrip("\n") == text.rstrip("\n"), company + ": edition display changed"
    checked_links = 0
    pages = list(ROOT.rglob("*.md"))
    for path in pages:
        text = path.read_text()
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert destination.is_relative_to(ROOT), f"Path outside archive: {path}: {target}"
            assert destination.exists(), f"Missing target: {path}: {target}"
            if parsed.fragment:
                dest_text = destination.read_text()
                assert '<a id="' + unquote(parsed.fragment) + '"></a>' in dest_text, f"Missing anchor: {path}: {target}"
            checked_links += 1
    for entry in catalog["letters"]:
        assert (ROOT / entry["record"]).is_file()
        for path in entry["pages"].values():
            assert (ROOT / path).is_file()
    print(f"PASS: 27 letters, 54 reading pages, {len(baseline['files'])} preserved source files, {checked_links} local links.")


if __name__ == "__main__":
    verify()
