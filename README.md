# 창업 정보 데일리 브리핑

정적 GitHub Pages 사이트: https://moderationbug.github.io/startup-briefing/  (빌드 단계 없음, 순수 HTML/CSS)

## 하루치 추가
1. `content/YYYY-MM-DD.json` 작성:
```json
{"date":"2026-10-19","note":"(선택) 한 줄 요약",
 "sections":[
  {"title":"📌 모두의창업 시즌3 · 재도전","columns":["추천","항목","일정","링크","PS"],
   "rows":[["⭐","재도전 멘토링","10/26~12/14","https://modoo.or.kr","재도전 가점 확보"]]},
  {"title":"📋 신규 공고","rows":[]},
  {"title":"⏰ 마감 임박","rows":[]},
  {"title":"🗓 연간 주요 프로그램","columns":["추천","사업명(링크)","주관","통상 모집 시기","올해 공고 상태","대상 요건","예창패 영향","PS"],"rows":[]},
  {"title":"🐦 X 동향","rows":[]},
  {"title":"🔍 확인 현황","rows":[]}]}
```
- `🗓 연간 주요 프로그램`은 선택 섹션(없으면 페이지에서 생략). 나머지 섹션 제목은 위와 정확히 일치. `columns`는 첫 칸 `추천`, 마지막 칸 `PS` 필수. 추천 값은 `⭐` 또는 `""`.
- `rows`가 비면 "없음" 표시. 셀 안의 URL은 자동 링크.
- 공개 사이트이므로 개인 정보(나이, 거주지, 사업자 여부, 개인 합불 결과)는 쓰지 않는다.
2. `python3 scripts/add_briefing.py content/YYYY-MM-DD.json` → 일자 페이지, prev/next, index, `data/briefings.json` 재생성
3. `git add -A && git commit -m "briefing YYYY-MM-DD" && git push origin main`
