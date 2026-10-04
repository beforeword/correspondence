"""Render researcher letters from the bilingual archive data; Python standard library only."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = {"en": "Kirill Shebetov · beforeword", "ru": "Кирилл Шебетов · beforeword"}


def body_text(x, lang):
    return "\n\n".join(x["body_" + lang]) + "\n"


def render(x, lang, previous, following):
    ru = lang == "ru"
    readme = "README.ru.md" if ru else "README.md"
    other = "README.md" if ru else "README.ru.md"
    name = x["name_" + lang]
    heading = ("Письмо: " if ru else "Letter to ") + name
    lines = [
        "[← " + ("Все письма" if ru else "All letters") + "](../../../" + readme + ") · [" + ("English original" if ru else "Русский перевод") + "](" + other + ")",
        "# " + heading,
        "**" + x["question_" + lang] + "**",
        "**Статус:** письмо показано в папке «Отправленные». Ответ не опубликован." if ru else "**Status:** the letter is shown in the Sent folder. No reply is published.",
        "[Зачем написано](#purpose) · [Читать перевод](#letter) · [Публикации](#sources) · [Материалы отправки](#record)" if ru else "[Why it was written](#purpose) · [Read the letter](#letter) · [Publications](#sources) · [Sending record](#record)",
        '<a id="purpose"></a>',
        "## Зачем написано это письмо" if ru else "## Why this letter was written",
        "*Пояснение beforeword для читателя; не входит в отправленное письмо.*" if ru else "*beforeword’s explanation for readers; separate from the sent letter.*",
    ]
    labels = ["Повод", "Почему это важно читателю", "О чём просит письмо"] if ru else ["Starting point", "Why it matters", "What the letter asks"]
    for label, paragraph in zip(labels, x["why_" + lang]):
        lines.append("**" + label + ".** " + paragraph)
    lines += [
        '<a id="letter"></a>',
        "## Русский перевод" if ru else "## English transcription",
        "Письмо отправлено на английском. Это перевод beforeword, редакция 2. [Сопоставить с английским текстом](README.md#letter)." if ru else "Transcribed from the author’s screenshots. Screen line wraps are joined and overlapping passages appear once; wording and punctuation are retained.",
        "[Текстовый файл](letter.ru.txt) · [Данные записи](record.json)" if ru else "[Plain-text version](letter.en.txt) · [Record data](record.json)",
        "**" + ("Тема: " if ru else "Subject: ") + x["subject_" + lang] + "**",
        "---",
    ]
    lines += [("\\+" if p == "+" else p.replace("\n", "  \n")) for p in x["body_" + lang]]
    lines += ["---", "*Конец перевода письма.*" if ru else "*End of the transcribed letter.*", '<a id="sources"></a>',
              "## Публикации, обсуждаемые в письме" if ru else "## Publications discussed in the letter",
              "Ссылки и указатели ниже добавлены для читателя и не входят в текст письма. Они позволяют найти обсуждаемые места; обоснованность выводов можно рассмотреть отдельно." if ru else "The links and locators below are reader guidance, separate from the letter. They help locate the passages under discussion; the grounds for the claims remain open to examination."]
    for s in x.get("public_sources", []):
        lines.append("- [" + s["title"] + "](" + s["url"] + ") — " + s.get("locator_" + lang, "") + (" " + s["note_" + lang] if s.get("note_" + lang) else ""))
    lines += ['<a id="record"></a>', "## Материалы отправки" if ru else "## Sending record"]
    sending = x["sending"]
    date = x.get("date")
    if date:
        date_display = ("2 октября 2026" if ru else "2 October 2026") + ", " + x["time_display"]
        date_display += " · часовой пояс не указан" if ru else " · timezone not supplied"
    else:
        date_display = "В заголовке показано только «пятница»; календарная дата не установлена." if ru else "The header shows only “Friday”; the calendar date is not established."
    to = ", ".join("`" + a + "`" for a in x["to"]) or ("Полный адрес не показан." if ru else "The full address is not shown.")
    lines += [
        "| " + ("Поле | Запись" if ru else "Field | Record") + " |\n| --- | --- |\n"
        + "| " + ("Автор" if ru else "Author") + " | " + AUTHOR[lang] + " |\n"
        + "| " + ("Адресат письма" if ru else "Intended addressee") + " | " + name + " |\n"
        + "| " + ("Адрес отправки" if ru else "Sent to") + " | " + to + " |\n"
        + "| " + ("Дата в материалах" if ru else "Date in the materials") + " | " + date_display + " |",
        "Основание записи — скриншоты папки «Отправленные», предоставленные автором. Они не устанавливают получение или прочтение адресатом." if ru else "The record is based on author-supplied screenshots of the Sent folder. These do not establish delivery or reading by the recipient.",
    ]
    if sending["additional_recipient_address_not_shown"]:
        lines.append("Интерфейс показывает ещё одного получателя, но его полный адрес в материалах не виден." if ru else "The interface indicates another recipient whose full address is not visible in the supplied materials.")
    if sending["forwarding_requested"] and not sending.get("notes", {}).get(lang):
        lines.append("Письмо отправлено на указанный адрес с просьбой переслать его адресату. Выполнение пересылки не установлено опубликованными материалами." if ru else "The message asks the listed contact to forward the letter to its intended addressee. The published materials do not establish that it was forwarded.")
    note = sending.get("notes", {}).get(lang)
    if note:
        lines.append(note)
    lines += ["### Скриншоты автора" if ru else "### Author-supplied screenshots",
              "Исходные изображения сохранены без изменений. Контрольные суммы приведены в [record.json](record.json)." if ru else "The supplied images are preserved without modification. Their checksums are listed in [record.json](record.json)."]
    for i, e in enumerate(x["evidence"], 1):
        lines.append("- [" + ("Скриншот " if ru else "Screenshot ") + str(i) + " · " + Path(e["file"]).name + "](" + e["file"] + ")")
    lines += ["Отсутствие опубликованного ответа не означает согласия или отказа. Появление имени в архиве не означает поддержки beforeword." if ru else "No published reply does not mean agreement or rejection. Inclusion in this archive does not imply support for beforeword.", "---"]
    nav = []
    if previous:
        nav.append("[← " + previous["name_" + lang] + "](../" + previous["id"] + "/" + readme + ")")
    nav.append("[" + ("Все письма" if ru else "All letters") + "](../../../" + readme + ")")
    if following:
        nav.append("[" + following["name_" + lang] + " →](../" + following["id"] + "/" + readme + ")")
    lines.append(" · ".join(nav))
    return "\n\n".join(lines) + "\n"


def build():
    xs = json.loads((ROOT / "data/researchers.json").read_text())
    for i, x in enumerate(xs):
        dest = ROOT / "letters/researchers" / x["id"]
        dest.mkdir(parents=True, exist_ok=True)
        editions = []
        for lang in ["en", "ru"]:
            readme = "README.ru.md" if lang == "ru" else "README.md"
            (dest / readme).write_text(render(x, lang, xs[i-1] if i else None, xs[i+1] if i+1 < len(xs) else None))
            label = "Русский перевод beforeword · редакция 2" if lang == "ru" else "English transcription from author-supplied screenshots"
            header = "beforeword · " + label + "\n" + ("Тема: " if lang == "ru" else "Subject: ") + x["subject_" + lang] + "\n\n"
            (dest / ("letter." + lang + ".txt")).write_text(header + body_text(x, lang))
            editions.append({"language": lang, "role": "translation" if lang == "ru" else "transcription", "subject": x["subject_" + lang], "file": readme,
                             "text_file": "letter." + lang + ".txt", "body_paragraphs": x["body_" + lang],
                             "body_sha256_utf8": hashlib.sha256(body_text(x, lang).encode()).hexdigest(),
                             "body_serialization": "UTF-8; paragraphs joined with two LF characters; one final LF.",
                             "is_sent_wording": lang == "en"})
        record = {"schema_version": 1, "id": x["id"], "series": "researchers", "recipient": x["name_en"], "recipient_ru": x["name_ru"],
                  "author": {"name": "Kirill Shebetov", "project": "beforeword"}, "original_language": "en", "topic": x["topic"],
                  "status": x["status"], "sending": x["sending"], "editions": editions,
                  "editorial_context": {"separate_from_sent_letter": True, "question": {lang: x["question_"+lang] for lang in ["en","ru"]},
                                        "purpose": {lang: x["why_"+lang] for lang in ["en","ru"]}},
                  "discussed_publications": x.get("public_sources", []), "evidence": x["evidence"]}
        (dest / "record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(f"Built {len(xs)} researcher records and {len(xs)*2} reading pages.")


if __name__ == "__main__":
    build()
