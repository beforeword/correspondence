"""Build the bilingual reader indexes and machine-readable catalog."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [
    ("ai", "AI behavior and evaluation", "Поведение и оценка ИИ"),
    ("experience", "Consciousness, experience and self-description", "Сознание, опыт и самоописание"),
    ("language", "Language and interpretation", "Язык и толкование"),
    ("evidence", "Evidence and explanation", "Свидетельства и объяснения"),
]


def build():
    xs = json.loads((ROOT / "data/researchers.json").read_text())
    for lang in ["en", "ru"]:
        ru = lang == "ru"
        readme = "README.ru.md" if ru else "README.md"
        lines = [
            "# Письма исследователям и разработчикам ИИ" if ru else "# Letters to researchers and AI developers",
            "[English](README.md) · **Русский**" if ru else "**English** · [Русский](README.ru.md)",
            "До того как я научился говорить о себе, о других и о мире, эти слова уже придумали. Почему от нас требуют принимать выученные описания за то, что ими называют? Это вопрос, с которым я обращаюсь к авторам работ о языке, сознании и ИИ." if ru else "Long before I learned to speak about myself, other people or the world, the words were already in use. Why should anyone have to accept a learned description as the very thing it names? I put that question to people who write about language, consciousness and AI.",
            "Здесь собраны мои 27 писем. В 24 письмах исследователям я спрашиваю, на чём основан конкретный вывод в их работе. В трёх письмах компаниям — OpenAI, Anthropic и xAI — предлагаю изменить правила ответов и то, как разработчики сообщают о результатах испытаний." if ru else "This archive contains 27 of my letters. In 24 letters to researchers I ask what supports a specific claim in their work. In three letters to OpenAI, Anthropic and xAI I propose changes to the rules for model responses and the way developers report test results.",
            "Кирилл Шебетов · Beforeword" if ru else "Kirill Shebetov · Beforeword",
            "**[Читать три письма компаниям на сайте](https://beforeword.xyz/letters/)** · [Предложение Beforeword](https://beforeword.xyz/proposal/)" if ru else "**[Read the three company letters on the website](https://beforeword.xyz/letters/en/)** · [The Beforeword proposal](https://beforeword.xyz/proposal/en/)",
            "[Все 24 письма исследователям](#researchers) · [Письма компаниям](#companies) · [Ответы](#status) · [Как пользоваться архивом](#about)" if ru else "[All 24 researcher letters](#researchers) · [Company letters](#companies) · [Replies](#status) · [Using the archive](#about)",
            "## Три письма для первого знакомства" if ru else "## Three letters to start with",
        ]
        starts = [
            ("companies/openai", "Почему характеристика становится основанием решения?", "How does a description become a basis for a decision?", "Предложение OpenAI: показывать основания характеристики и действия, сохраняя возможность возражения.", "A proposal to OpenAI: show the grounds for the description and the action, while preserving the ability to challenge both."),
            ("researchers/askell", "Одни слова — разные выводы?", "Same words, different conclusions?", "Письмо Аманде Аскелл предлагает оставить фразу неизменной и сменить только обозначение источника: человек или ИИ.", "The letter to Amanda Askell proposes keeping a sentence unchanged and changing only its source label: human or AI."),
            ("researchers/sutskever", "Что связывает предсказание с пониманием?", "What connects prediction with understanding?", "Письмо Илье Суцкеверу просит указать критерий перехода от результата к такому выводу.", "The letter to Ilya Sutskever asks for the criterion supporting that inference from a result."),
        ]
        for path, title_ru, title_en, text_ru, text_en in starts:
            lines.append("- **[" + (title_ru if ru else title_en) + "](letters/" + path + "/" + readme + ")** " + (text_ru if ru else text_en))
        lines += ['<a id="companies"></a>', "## Письма компаниям · 3" if ru else "## Company letters · 3",
                  "Предложения о правилах ответов, основаниях решений и проверке этих правил. Дата отправки, указанная автором: **4 октября 2026 года**." if ru else "Proposals about response rules, the grounds for decisions and how to evaluate those rules. Sending date reported by the author: **4 October 2026**."]
        companies = [
            ("openai", "OpenAI", "Показывать основания применения характеристики и решения на её основе; сохранять возможность оспаривания.", "Show the grounds for applying a description and acting on it; preserve the ability to challenge both."),
            ("anthropic", "Anthropic", "Показывать основания, по которым говорят о понимании, ценностях или идентичности, и связывают эти описания с решениями.", "Show the grounds for attributing understanding, values or identity, and for decisions based on those descriptions."),
            ("xai", "xAI", "Показывать основания описаний, решений и выводов из оценки ответов Grok.", "Show the grounds for descriptions, decisions and conclusions drawn from evaluations of Grok’s responses."),
        ]
        for id_, name, desc_ru, desc_en in companies:
            lines.append("- **[" + name + "](letters/companies/" + id_ + "/" + readme + ")** — " + (desc_ru if ru else desc_en))
        lines += ['<a id="researchers"></a>', "## Письма исследователям · 24" if ru else "## Researcher letters · 24",
                  "Выберите вопрос. На странице письма доступны английская транскрипция, русский перевод, пояснение цели, ссылки на обсуждаемые публикации и скриншоты автора." if ru else "Choose a question. Each letter includes an English transcription, a Russian translation, its purpose, links to the publications discussed, and the author’s screenshots."]
        for key, title_en, title_ru in GROUPS:
            group = [x for x in xs if x["topic"] == key]
            lines += ["### " + (title_ru if ru else title_en) + " · " + str(len(group))]
            for x in group:
                lines.append("- **[" + x["name_" + lang] + "](letters/researchers/" + x["id"] + "/" + readme + ")** — " + x["question_" + lang])
        lines += ['<a id="status"></a>', "## Ответы и статусы" if ru else "## Replies and status",
                  "**xAI:** опубликовано [уведомление команды Safety](letters/companies/xai/reply/README.ru.md). Ответ по существу предложения не опубликован. По остальным письмам в архиве ответов нет." if ru else "**xAI:** a [Safety Team acknowledgement](letters/companies/xai/reply/README.md) is published. No substantive response to the proposal is published. The archive contains no replies to the other letters.",
                  "Статусы описывают доступные материалы. Отправка, получение, прочтение и ответ по существу — разные события. Просьба переслать письмо не подтверждает пересылку. Отсутствие опубликованного ответа не означает согласия или отказа; упоминание адресата не означает его поддержки beforeword." if ru else "Statuses describe the available records. Sending, delivery, reading and a substantive reply are different events. A request to forward a letter does not establish that it was forwarded. No published reply does not mean agreement or rejection; naming a recipient does not imply their support for beforeword.",
                  '<a id="about"></a>', "## Как пользоваться архивом" if ru else "## Using the archive",
                  "- **Читать и сопоставлять.** Переключение EN/RU находится в начале каждой страницы. Пояснения и ссылки отделены от письма; под ним доступны материалы отправки и текстовый файл. Для чтения и скачивания учётная запись GitHub не нужна." if ru else "- **Read and compare.** Every page begins with an EN/RU link. Context and source guidance are separate from the letter; sending records and a plain-text version are also available. No GitHub account is needed to read or download the archive.",
                  "- **Проверять запись.** Английские транскрипции исследовательских писем сохраняют формулировки предоставленных скриншотов. Отправленные редакции писем компаниям сохранены отдельными файлами. Неуказанные даты и скрытые адреса остаются неизвестными." if ru else "- **Inspect the record.** Research-letter transcriptions retain the wording of the supplied screenshots. The sent editions of company letters are preserved as separate files. Missing dates and hidden addresses remain unknown.",
                  "- **Ссылаться на конкретную версию.** Используйте постоянную ссылку GitHub на файл в выбранном коммите. История изменений позволяет сопоставлять редакции; исправления пояснений или перевода не должны подменять отправленный текст." if ru else "- **Cite a specific version.** Use a GitHub permalink to the file at a chosen commit. The history lets readers compare revisions; changes to context or translation must not replace the sent wording.",
                  "- **Работать с данными.** [Каталог JSON](catalog.json) содержит все 27 записей со ссылками на тексты и подробные данные. [Устройство архива](tools/README.md) описывает сборку и проверку." if ru else "- **Use the data.** The [JSON catalog](catalog.json) lists all 27 records with links to texts and detailed data. [Archive maintenance](tools/README.md) explains how the pages are built and checked.",
                  "[Процедура чтения beforeword](https://beforeword.xyz/model/) · [Beforeword на русском](https://beforeword.xyz/) · [Скачать архив ZIP](https://github.com/beforeword/correspondence/archive/refs/heads/main.zip)" if ru else "[beforeword reading procedure](https://beforeword.xyz/model/en/) · [Beforeword in English](https://beforeword.xyz/en/) · [Download ZIP](https://github.com/beforeword/correspondence/archive/refs/heads/main.zip)",
                  "Автор: **Кирилл Шебетов / beforeword** · [mail@beforeword.xyz](mailto:mail@beforeword.xyz)" if ru else "Author: **Kirill Shebetov / beforeword** · [mail@beforeword.xyz](mailto:mail@beforeword.xyz)",
                  "Существующая [лицензия MIT](LICENSE) сохранена. Она не предоставляет прав на включённые материалы третьих лиц, в том числе цитаты и входящие сообщения." if ru else "The repository’s existing [MIT license](LICENSE) is retained. It does not grant rights in included third-party material, such as quotations or incoming correspondence.",
        ]
        (ROOT / readme).write_text("\n\n".join(lines) + "\n")
    records = []
    for series, ids in [("companies", ["openai", "anthropic", "xai"]), ("researchers", [x["id"] for x in xs])]:
        for id_ in ids:
            base = f"letters/{series}/{id_}"
            records.append({"id": id_, "series": series, "pages": {"en": base + "/README.md", "ru": base + "/README.ru.md"}, "record": base + "/record.json"})
    catalog = {"schema_version": 1, "title": "beforeword correspondence", "repository": "https://github.com/beforeword/correspondence",
               "author": {"name": "Kirill Shebetov", "project": "beforeword"}, "letter_count": len(records),
               "notes": {"en": "Paths are relative to this file. Sent texts, translations and editorial context are separate. Statuses describe the available materials; missing information has not been inferred.",
                         "ru": "Пути указаны относительно этого файла. Отправленные тексты, переводы и пояснения разделены. Статусы описывают доступные материалы; пропуски не заполнены предположениями."}, "letters": records}
    (ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    print("Built English and Russian reader indexes and the 27-letter catalog.")


if __name__ == "__main__":
    build()
