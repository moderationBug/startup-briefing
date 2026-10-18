#!/usr/bin/env python3
"""Add/update a day's briefing and regenerate all pages.
Usage: python3 scripts/add_briefing.py content/YYYY-MM-DD.json   (or no arg: just rebuild)
"""
import json, sys, os, html, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = ["📌 모두의창업 시즌3 · 재도전", "📋 신규 공고", "⏰ 마감 임박", "🐦 X 동향", "🔍 확인 현황"]
URL = re.compile(r'(https?://[^\s<>"]+)')

def cell(v):
    s = html.escape(str(v or ""))
    return URL.sub(lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>', s)

def table(sec):
    cols = sec.get("columns") or []
    rows = sec.get("rows") or []
    if not rows: return '<p class="empty">없음</p>'
    assert cols and cols[0] == "추천" and cols[-1] == "PS", f"columns must start with 추천 and end with PS: {cols}"
    h = ['<div class="tw"><table><thead><tr>'] + [f'<th>{html.escape(c)}</th>' for c in cols] + ['</tr></thead><tbody>']
    for r in rows:
        r = list(r) + [""] * (len(cols) - len(r))
        star = "⭐" if str(r[0]).strip() in ("⭐", "*", "true", "True", "1") else ""
        h.append('<tr>' + f'<td data-l="추천" class="star">{star}</td>' +
                 ''.join(f'<td data-l="{html.escape(c)}">{cell(v)}</td>' for c, v in zip(cols[1:], r[1:])) + '</tr>')
    h.append('</tbody></table></div>')
    return ''.join(h)

def page(title, body, css):
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="stylesheet" href="{css}"></head><body><main>{body}</main></body></html>\n'''

def day_html(d, data, prev, nxt):
    nav = '<nav class="pn">' + (f'<a href="{prev}.html">← {prev}</a>' if prev else '<span></span>') + '<a href="../index.html">목록</a>' + (f'<a href="{nxt}.html">{nxt} →</a>' if nxt else '<span></span>') + '</nav>'
    secs = {s.get("title"): s for s in data.get("sections", [])}
    body = [nav, f'<h1>{d} 브리핑</h1>']
    if data.get("note"): body.append(f'<p class="note">{cell(data["note"])}</p>')
    for t in SECTIONS:
        body.append(f'<section><h2>{t}</h2>{table(secs.get(t, {}))}</section>')
    body.append(nav)
    return page(f'{d} 창업 정보 브리핑', ''.join(body), '../style.css')

def main():
    os.chdir(ROOT)
    if len(sys.argv) > 1:
        src = sys.argv[1]; data = json.load(open(src, encoding="utf-8"))
        d = data["date"]; assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", d)
        dst = f"content/{d}.json"
        if os.path.abspath(src) != os.path.abspath(dst):
            json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    dates = sorted(f[:-5] for f in os.listdir("content") if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.json", f))
    for i, d in enumerate(dates):
        data = json.load(open(f"content/{d}.json", encoding="utf-8"))
        open(f"briefings/{d}.html", "w", encoding="utf-8").write(day_html(d, data, dates[i-1] if i else None, dates[i+1] if i+1 < len(dates) else None))
    json.dump({"dates": dates[::-1]}, open("data/briefings.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    body = ['<h1>창업 정보 데일리 브리핑</h1><p class="sub">IT 예비창업자를 위한 정부·지역 창업지원 정보 요약</p>']
    if dates:
        body.append(f'<a class="latest" href="briefings/{dates[-1]}.html">최신 브리핑: {dates[-1]} →</a><h2>이력</h2><ul class="hist">' +
                    ''.join(f'<li><a href="briefings/{d}.html">{d}</a></li>' for d in dates[::-1]) + '</ul>')
    else:
        body.append('<p class="empty">아직 게시된 브리핑이 없습니다.</p>')
    open("index.html", "w", encoding="utf-8").write(page("창업 정보 데일리 브리핑", ''.join(body), "style.css"))
    print("published:", ", ".join(dates) or "(none)")
main()
