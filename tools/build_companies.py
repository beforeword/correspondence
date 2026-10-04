#!/usr/bin/env python3
"""Build the company archive pages from local source data and frozen editions.

Run from any directory. Requires only the Python standard library.
The six files/ TXT editions and xAI reply evidence are inputs, never rewritten.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENTS = json.loads((ROOT / "data/company-events.json").read_text())


def md(text: str) -> str:
    """Escape prose so Markdown syntax does not change the displayed wording."""
    text = re.sub(r"([\\`*_{}\[\]<>#!|])", r"\\\1", text)
    return re.sub(r"(?m)^(\d+)\.", r"\1\\.", text)


def show_edition(text: str, content: dict, language: str) -> str:
    headings = {
        "Appendix. Proposed additions",
        "Приложение. Предлагаемые дополнения",
        "Documents and sources",
        "Материалы и источники",
    }
    subheadings = {item["title"] for item in content[f"appendix_{language}"]}
    paragraphs = text.rstrip("\n").split("\n\n")
    result = []
    for index, paragraph in enumerate(paragraphs):
        if index == 0 or paragraph in headings:
            result.append("### " + md(paragraph))
        elif paragraph in subheadings:
            result.append("#### " + md(paragraph))
        elif re.fullmatch(r"https?://\S+", paragraph):
            result.append(f"[{paragraph}]({paragraph})")
        else:
            result.append(md(paragraph))
    return "\n\n".join(result)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def link(label: str, target: str) -> str:
    return f"[{label}]({target})"


def email_list(items: list[dict]) -> str:
    return ", ".join("`" + item["email"] + "`" for item in items)


def status(company: str, language: str) -> str:
    if language == "en":
        return ("Acknowledgment published · No substantive response published"
                if company == "xai" else "No acknowledgment or company response published")
    return ("Служебное сообщение опубликовано · Ответ по существу не опубликован"
            if company == "xai" else "Подтверждение получения и ответ компании не опубликованы")


def make_page(company: str, content: dict, sent: dict, events: list, language: str) -> str:
    en = language == "en"
    directory = ROOT / "letters/companies" / company
    filename = f"beforeword-{company}-{language}-2026-10-04-v1.0.txt"
    text = (directory / "files" / filename).read_text()
    lines = [
        ("[← All letters](../../../README.md) · [По-русски](README.ru.md)" if en else
         "[← Все письма](../../../README.ru.md) · [English](README.md)"),
        "# " + content[f"title_{language}"],
        content[f"lede_{language}"],
        ("**Sent 4 October 2026 — reported by the author.**" if en else
         "**Отправлено 4 октября 2026 года — по сообщению автора.**"),
        "**" + ("Record as of 4 October 2026: " if en else "Сведения на 4 октября 2026 года: ") + status(company, language) + ".**",
        ("**To:** " if en else "**Кому:** ") + email_list(sent["to"]),
    ]
    if sent.get("cc"):
        lines.append(("**Cc:** " if en else "**Копия:** ") + email_list(sent["cc"]))
    lines.extend([
        ("[Why this letter](#purpose) · [Read the letter](#letter) · [2026 context](#context) · [Sending record](#record)"
         if en else "[Зачем написано письмо](#purpose) · [Читать письмо](#letter) · [Контекст 2026 года](#context) · [Сведения об отправке](#record)"),
    ])
    if company == "xai":
        lines.append("[Read the xAI acknowledgment](reply/README.md)" if en else
                     "[Читать служебное сообщение xAI](reply/README.ru.md)")
    lines.extend([
        '<a id="purpose"></a>',
        "## " + ("Why this letter was written" if en else "Зачем написано это письмо"),
        ("*Editorial context from beforeword; separate from the sent letter.*" if en else
         "*Пояснение beforeword; не входит в отправленное письмо.*"),
        content[f"reason_{language}"],
        '<a id="letter"></a>',
        "## " + ("English sent edition" if en else "Русский перевод"),
        ("Edition 1.0 is reproduced below, including its appendix and source list. The wording is preserved; headings and links are formatted for reading on GitHub."
         if en else "Ниже опубликован русский перевод редакции 1.0 вместе с приложением и списком источников. Для отправки использована английская редакция. Текст перевода сохранён; заголовки и ссылки оформлены для чтения на GitHub."),
        (link("Preserved English TXT", "files/" + filename) + " · " + link("Russian translation", "README.ru.md#letter")
         if en else link("Сохранённый TXT перевода", "files/" + filename) + " · " + link("Отправленная английская редакция", "README.md#letter")),
        "---",
        show_edition(text, content, language),
        "---",
        ("*End of the preserved edition. The material below is archive context.*" if en else
         "*Конец сохранённого текста. Ниже — материалы, добавленные для архива.*"),
        '<a id="context"></a>',
        "## " + ("Public statements from 2026: context for the letter" if en else "Публичные заявления 2026 года: контекст письма"),
        ("The excerpts below identify wording discussed in this archive. They do not indicate endorsement of beforeword or a response to the letter."
         if en else "Ниже приведены формулировки, обсуждаемые в архиве. Эти цитаты не означают поддержки beforeword или ответа на письмо."),
    ])
    for item in content.get("statements", [content["statement"]]):
        lines.extend([
            "### " + link(item["title"], item["url"]),
            item[f"date_{language}"],
            "> " + md(item["quote"]),
        ])
        if not en:
            lines.append("**Перевод:** " + item["translation_ru"])
        lines.extend([item[f"context_{language}"], item[f"connection_{language}"]])
    lines.extend([
        '<a id="record"></a>',
        "## " + ("Sending record and publication limits" if en else "Сведения об отправке и границы опубликованных данных"),
        ("- **Author:** Kirill Shebetov · beforeword\n- **Sending date:** 4 October 2026, reported by the author\n- **Channel:** email\n- **Sent edition:** English, version 1.0\n- **Russian edition:** translation, not recorded as sent"
         if en else "- **Автор:** Кирилл Шебетов · beforeword\n- **Дата отправки:** 4 октября 2026 года, по сообщению автора\n- **Канал:** электронная почта\n- **Отправленная редакция:** английская, версия 1.0\n- **Русская редакция:** перевод; её отправка не заявлена"),
        sent[f"recipient_note_{language}"],
        ("The date and addresses are reported by the author. This record does not establish who read the letter or whether the requested team received it."
         if en else "Дата и адреса указаны автором. Эти сведения не устанавливают, кто прочитал письмо и получила ли его команда, которой адресовано предложение."),
    ])
    if company == "xai":
        ack = next(event for event in events if event["type"] == "acknowledged")
        lines.extend([ack[f"body_{language}"], ack[f"commentary_{language}"],
                      ("The acknowledgment date in the archive records when the author supplied the screenshot. The screenshot does not show a full calendar date."
                       if en else "Дата служебного сообщения в архиве — дата предоставления скриншота автором. Полная календарная дата сообщения на скриншоте не показана."),
                      link("Acknowledgment and screenshot" if en else "Служебное сообщение и скриншот", "reply/README.md" if en else "reply/README.ru.md")])
    else:
        lines.append("No acknowledgment or substantive company response is included in the supplied materials." if en else
                     "В предоставленных материалах нет подтверждения получения или ответа компании по существу.")
    lines.extend([
        ("No published response is a correspondence status; it does not establish agreement, rejection, or a reason for not responding."
         if en else "Отсутствие опубликованного ответа обозначает состояние переписки; оно не устанавливает согласия, отказа или причины отсутствия ответа."),
        "### " + ("Published contact references" if en else "Публикации с контактными адресами"),
    ])
    lines.append("\n".join("- " + link(item[f"label_{language}"], item["url"]) for item in sent["address_sources"]))
    lines.extend([
        "### " + ("Archive files" if en else "Файлы архива"),
        "\n".join([
            "- " + link("English edition 1.0 (TXT)" if en else "Английская редакция 1.0 (TXT)", f"files/beforeword-{company}-en-2026-10-04-v1.0.txt"),
            "- " + link("Russian translation (TXT)" if en else "Русский перевод (TXT)", f"files/beforeword-{company}-ru-2026-10-04-v1.0.txt"),
            "- " + link("Structured record and file hashes (JSON)" if en else "Сведения о письме и контрольные суммы файлов (JSON)", "record.json"),
        ]),
        ("[← All letters](../../../README.md) · [По-русски](README.ru.md)" if en else
         "[← Все письма](../../../README.ru.md) · [English](README.md)"),
    ])
    return "\n\n".join(lines) + "\n"


def build_reply(events: list) -> None:
    directory = ROOT / "letters/companies/xai/reply"
    event = next(event for event in events if event["type"] == "acknowledged")
    for lang in ("en", "ru"):
        en = lang == "en"
        txt = f"xai-safety-message-{lang}-2026-10-04.txt"
        text = (directory / txt).read_text().rstrip("\n")
        paragraphs = text.split("\n\n")
        # Preserve the double space in the source transcription and line breaks.
        body = "\n\n".join(md(p).replace("\n", "  \n") for p in paragraphs)
        lines = [
            ("[← Letter to xAI](../README.md) · [По-русски](README.ru.md)" if en else
             "[← Письмо xAI](../README.ru.md) · [English](README.md)"),
            "# " + ("Acknowledgment from the xAI Safety Team" if en else "Служебное сообщение xAI Safety Team"),
            "**" + ("Acknowledgment published · No substantive response published" if en else
                     "Служебное сообщение опубликовано · Ответ по существу не опубликован") + "**",
            event[f"body_{lang}"],
            event[f"commentary_{lang}"],
            "## " + ("Source record" if en else "Источник"),
            event[f"source_note_{lang}"],
            ("4 October 2026 is the date the author supplied the screenshot, not a full message date visible in the image. The screenshot shows the sender label “Safety” and the time 21:43; it does not display the sender’s email address or a time zone."
             if en else "4 октября 2026 года — дата предоставления скриншота автором, а не полная дата сообщения, показанная на изображении. На скриншоте видны имя отправителя «Safety» и время 21:43; адрес отправителя и часовой пояс не показаны."),
            ("[View the supplied screenshot](xai-safety-message-2026-10-04.png) · [English transcription](xai-safety-message-en-2026-10-04.txt) · [Russian translation](xai-safety-message-ru-2026-10-04.txt)"
             if en else "[Открыть предоставленный скриншот](xai-safety-message-2026-10-04.png) · [Английская транскрипция](xai-safety-message-en-2026-10-04.txt) · [Русский перевод](xai-safety-message-ru-2026-10-04.txt)"),
            "## " + ("English transcription" if en else "Русский перевод"),
            ("The transcription below preserves the supplied transcription file. The original screenshot remains available above."
             if en else "Ниже опубликован перевод английской транскрипции сообщения. Исходный скриншот и английский текст доступны по ссылкам выше."),
            "---", body, "---",
            ("[← Letter to xAI](../README.md) · [All letters](../../../../README.md)" if en else
             "[← Письмо xAI](../README.ru.md) · [Все письма](../../../../README.ru.md)"),
        ]
        (directory / ("README.md" if en else "README.ru.md")).write_text("\n\n".join(lines) + "\n")


def main() -> None:
    for item in EVENTS["letters"]:
        company = item["id"]
        content = json.loads((ROOT / f"data/companies/{company}.json").read_text())
        directory = ROOT / "letters/companies" / company
        sent = next(event for event in item["events"] if event["type"] == "sent")
        files = []
        for lang in ("en", "ru"):
            filename = f"beforeword-{company}-{lang}-2026-10-04-v1.0.txt"
            path = directory / "files" / filename
            files.append({"path": "files/" + filename, "language": lang,
                          "role": "sent_edition" if lang == "en" else "translation",
                          "is_recorded_as_sent": lang == "en", "sha256": sha(path)})
            (directory / ("README.md" if lang == "en" else "README.ru.md")).write_text(
                make_page(company, content, sent, item["events"], lang))
        assert files[0]["sha256"] == sent["sent_sha256"], company
        events = json.loads(json.dumps(item["events"]))
        for event in events:
            if "sent_text" in event:
                event["sent_text"] = "files/" + Path(event["sent_text"]).name
            for key in ("evidence", "text_file", "translation_file_ru"):
                if key in event:
                    event[key] = "reply/" + Path(event[key]).name
        record = {
            "schema_version": 1, "id": company, "series": "companies",
            "recipient": item["recipient"], "author": "Kirill Shebetov · beforeword",
            "edition": item["edition"], "original_language": "en", "record_as_of": EVENTS["updated"],
            "sending": {"date": sent["date"], "record_basis": "author_statement",
                        "channel": "email", "to": sent["to"], "cc": sent.get("cc", []),
                        "read_by_recipient": "not_established_by_supplied_record"},
            "status": {"acknowledgment_published": company == "xai", "substantive_response_published": False},
            "pages": {"en": "README.md", "ru": "README.ru.md"}, "editions": files,
            "editorial_context": {"role": "archive_commentary_not_sent_letter",
                                  "purpose": {lang: content[f"reason_{lang}"] for lang in ("en", "ru")},
                                  "public_statements": content.get("statements", [content["statement"]])},
            "events": events, "source_event_record": "../../../data/company-events.json",
        }
        if company == "xai":
            record["reply_evidence"] = [{"path": "reply/" + p.name, "sha256": sha(p)}
                                         for p in sorted((directory / "reply").iterdir()) if p.suffix in {".png", ".txt"}]
            build_reply(item["events"])
        (directory / "record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
