#!/usr/bin/env python3
import os
from pathlib import Path
import json
from datetime import datetime

# Базовые пути проекта
BASE = Path(__file__).resolve().parents[1]
ASSETS = BASE / "assets"
CLIPS = BASE / "clips"
OUTPUT = BASE / "render_out"
DOCS = BASE / "docs"

# Псевдо-данные по таймлайну (переделайте под реальный монтаж)
TIMELINE_MD = DOCS / "timeline_5min.md"
STORYBOARD = DOCS / "storyboard.md"
SHOTLIST = DOCS / "shotlist.md"

def ensure_dirs():
    """Создать необходимые директории, если их нет."""
    for d in [OUTPUT, OUTPUT / "frames", OUTPUT / "audio", OUTPUT / "videos"]:
        d.mkdir(parents=True, exist_ok=True)

def collect_contents():
    """Собрать списки материалов: клипы, музыка, SFX."""
    clips = sorted([p for p in CLIPS.glob("*.mp4")])
    music = sorted([p for p in (ASSETS / "music").glob("*.wav")])
    sfx = sorted([p for p in (ASSETS / "sfx").glob("*.wav")])
    return clips, music, sfx

def write_basic_timeline(clips, music, sfx):
    """Сгенерировать базовый таймлайн в docs/timeline_5min.md."""
    content = []
    content.append("# Таймлайн трейлера 5 минут\n")
    content.append("Общая структура таймлайна. Заполните детальнее в редакторе.\n\n")
    content.append("## Кадры (примерная разбивка)\n")
    timeline_points = [
        "0:00–0:45: Открытие — рассвет над Минском",
        "0:45–1:30: Завязка — протагонист за рулём",
        "1:30–3:00: Экшен — погоня и дроны над рекой",
        "3:00–4:15: Контраст природы и индустрии",
        "4:15–4:50: Кульминация — выбор",
        "4:50–5:00: Финал — логотип и релиз"
    ]
    for line in timeline_points:
        content.append(f"- {line}\n")
    content.append("\n## Музыка и SFX\n")
    for m in music:
        content.append(f"- Музыкальный трек: {m.name}\n")
    for s in sfx:
        content.append(f"- SFX: {s.name}\n")

    # Сохранить
    with open(TIMELINE_MD, "w", encoding="utf-8") as f:
        f.writelines(content)

def update_readme_with_status():
    """Добавить простой статус сборки в README (если есть)."""
    readme = BASE / "README.md"
    status_line = f"\n\n# Сборка трейлера (автогенерация)\nСгенерировано: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    try:
        with open(readme, "a", encoding="utf-8") as f:
            f.write(status_line)
    except FileNotFoundError:
        # Если README не найден, пропускаем
        pass

def main():
    print("== Запуск сборки трейлера (5 минут) =============")
    ensure_dirs()
    clips, music, sfx = collect_contents()

    print(f"Найдено клипов: {len(clips)}")
    print(f"Музыка: {len(music)} треков")
    print(f"SFX: {len(sfx)}")

    # Создание базового таймлайна
    write_basic_timeline(clips, music, sfx)
    print(f"Таймлайн создан: {TIMELINE_MD}")

    # Обновление storyboard/shotlist по мере необходимости
    if STORYBOARD.exists() or SHOTLIST.exists():
        print("Обновляйте docs/storyboard.md и docs/shotlist.md по мере разработки.")

    # Пример: копирование/подстановка путей для дальнейшей автоматизации
    # Здесь можно добавить генерацию файлов проекта для DAW/редактора

    update_readme_with_status()
    print("Готово. Продолжайте работу в редакторе и редакторе монтажа.")

if __name__ == "__main__":
    main()
