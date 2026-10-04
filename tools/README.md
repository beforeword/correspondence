# Archive maintenance / Устройство архива

[← English index](../README.md) · [← Русское оглавление](../README.ru.md)

## English

The reader pages are generated from local data. Python 3.9 or later is sufficient; no packages or network access are required.

```sh
python3 tools/build_archive.py
python3 tools/verify_archive.py
```

- `data/researchers.json` contains the 24 researcher-letter transcriptions, translations, purposes and sending metadata.
- `data/companies/` and `data/company-events.json` contain company-letter context and correspondence events. The six preserved TXT editions under `letters/companies/*/files/` are read by the generator and never rewritten.
- Every letter has a `record.json`. Paths inside a record are relative to that record unless stated otherwise. The top-level `catalog.json` provides an entry point to all 27 letters.
- `data/integrity.json` records the initial English subjects and body hashes, plus hashes of supplied screenshots and preserved company files. Verification checks those records, page wording, metadata boundaries and local links.

Keep the sent English wording and source images unchanged. Publish a new edition or a clearly labeled correction alongside an existing sent edition. Translation or context changes belong in a separate commit whose message explains the change. Record a reply separately from translations and commentary, and distinguish an acknowledgment from a substantive response. Keep missing dates, hidden addresses and unconfirmed forwarding explicit.

Publication history is available in Git. A file URL pinned to a commit identifies the exact version cited; an unpinned `main` URL follows later changes.

## Русский

Страницы для чтения собираются из локальных данных. Достаточно Python версии 3.9 или новее; дополнительные пакеты и доступ к сети не нужны. Команды сборки и проверки приведены выше.

- `data/researchers.json` содержит транскрипции 24 исследовательских писем, переводы, пояснения целей и сведения об отправке.
- `data/companies/` и `data/company-events.json` содержат контекст писем компаниям и события переписки. Шесть сохранённых TXT-редакций в `letters/companies/*/files/` используются при сборке и не перезаписываются.
- Для каждого письма предусмотрен `record.json`. Если не указано иное, пути в нём заданы относительно самого файла. Общий каталог `catalog.json` ведёт ко всем 27 письмам.
- `data/integrity.json` хранит исходные темы и контрольные суммы английских текстов, скриншотов и сохранённых файлов писем компаниям. Проверка сопоставляет их с текущими файлами, проверяет текст страниц, ограничения сведений и локальные ссылки.

Отправленные английские тексты и исходные изображения сохраняются неизменными. Новую редакцию или явно обозначенное исправление следует публиковать рядом с отправленной. Изменения перевода и пояснений следует фиксировать отдельным коммитом с указанием причины. Ответ публикуется отдельно от перевода и комментария; подтверждение получения отличается от ответа по существу. Неизвестные даты, скрытые адреса и неподтверждённая пересылка остаются обозначенными.

Историю публикаций хранит Git. Ссылка на файл в конкретном коммите фиксирует цитируемую версию; ссылка на `main` будет вести к последующим изменениям.
