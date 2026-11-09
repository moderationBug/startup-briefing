# Research notes — 2026-11-08 verify + Daegu sweep (Asia/Seoul)

Checked the morning of Sunday 2026-11-08 (box local = Asia/Seoul).  
Audience filter (do **not** paste personal details into the public page): 예비창업자 / no business registration / born 1989 / Daegu / IT / zero capital / preserve 예창패.

Verified facts only. If a page blocked, timed out, or was JS-empty, that is stated. Nothing invented.

Method: WebFetch + curl/python on DASH list pages 1–5 and selected detail URLs; WebSearch only as a cross-check when a primary page was 403/JS-empty.

---

## A) Re-verification of currently-open items

| # | 사업 | Status | Deadline (today) | What the checked page showed | URL checked |
|---|------|--------|------------------|------------------------------|-------------|
| 1 | 생성형 AI 활용 창업아카데미 | **OPEN** — closes **today** | Header/list **2026-11-08 23:00**. Body once says “11. 8.(일) **24:00**까지”. **Use 23:00** (same conflict as 11/7). | Detail title `[모집 중] 생성형 AI 활용 창업아카데미 교육 참가자 모집`. 접수기간 `2026-11-04 16:00 ~ 2026-11-08 23:00`. 대상 예비창업자, 정원 **30명 내외**, 교육비 **전액 무료** + PC·AI 구독료·중식, 교육 **2026-11-20 ~ 11-29** 대구창경·영남이공대(대면). DASH 목록 1~3쪽에는 없고 **4쪽**에 `[모집 중]` + **오늘 마감** + 동일 23:00. | https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00005091 |
| 2 | 2026 청년 어촌창업 아이디어 공모전 | **OPEN** — closes **today** | Official page: **2026. 11. 8.(일)**. Fetched text did **not** show a clock time (previous briefings used 23:59). “마감일까지 이메일로 제출”. | Homepage reachable. 신청 `2026. 10. 07.(수) ~ 11. 08.(일)`, 만 19~39세 개인·팀, 총 7명(팀)·총상금 **1,500만원**, 이메일 `co.vill@naver.com`. 서류합격일 기준 **사업자등록 없어야** 함. 분야4에 디지털 플랫폼·기술 서비스 예시. 배너/마감 표시 없음. | https://co-vill.imweb.me/ |
| 3 | GVC AI Platform | **OPEN** (D-1 on aggregator) | Aggregator: **2026.11.02 ~ 2026.11.09** (no clock time). Badge `마감임박 D-1`. | chchclub K-Startup **179681**. 대상에 예비창업자 포함, 전국. 신청 링크 https://global.venture.center/launchpad . **규모(현금·인원) 미기재**. Official launchpad loaded (마케팅 페이지): 예비 또는 창업 3년 이내 AI·플랫폼·SaaS, 1개월 업무공간 무상·1:1 멘토링 언급. 마감일·금액은 공식 페이지에 없음. | https://chchclub.com/notice/179681 ; official https://global.venture.center/launchpad |
| 4 | 2026 CBC KOREA 창업경진대회 | **OPEN** | **2026.10.15 ~ 11.10.(화) 18:00** (Linkareer + official) | Linkareer 시상규모 헤더 1,840만원(세션 합산). SESSION 01 총 7팀 / **1,450만원**, SESSION 02 총 6팀 / 390만원. Official https://ainnov.co.kr/cbc : SESSION 01은 **대표 포함 최소 2인**, “2027 CBC Global Finals **영어 프레젠테이션 가능 팀**”. 예비 또는 창업 7년 이내. | https://linkareer.com/activity/357190 ; official https://ainnov.co.kr/cbc |
| 5 | 의왕시 청년e-Room | **OPEN** | **2026.10.19 17:00 ~ 2026.11.11(수) 18:00**. VS badge `마감4일전`. | 19~39세, 의왕시 지속가능발전 아이디어. 예선 10팀 → 멘토링 → 데모데이 **11.27 14:00~17:00 의왕시 유니콘로드(현장)**. 상금 대상 **100만원**·최우수 50만원·우수 30만원. | https://www.venturesquare.net/announcement/1121670 |
| 6 | 러닝메이트 9기 | **OPEN** | **2026.10.26 ~ 2026.11.11(수) 23:59**. 사전과제 **~11.12(목) 23:59**. | eopla 페이지 일정 확인. 대상 극초기 창업팀(예비 또는 법인 3년 이내). 필수 OT **2026.11.17(화) 19:00-21:00 (온라인 진행)** — eopla 원문. 공식 https://www.orangepark.or.kr/articles/A4072237 는 HTTP 200이나 JS라 본문이 거의 안 보임. 2차 출처 gendoc(K-Startup 전재)에 **비용: 무료**, 신청 11/11 23:59 재기재. (gendoc는 11/17을 ‘오프라인 모임’으로도 적어 eopla와 불일치 → OT 형태는 eopla ‘온라인’을 우선) | https://eopla.net/magazines/48375 ; official (JS) https://www.orangepark.or.kr/articles/A4072237 ; secondary https://gendoc.ai/grants/8668 |
| 7 | 스쿨모아 쇼핑몰 | **OPEN** | **2026.10.28 ~ 2026.11.12** (D-4). Clock time not on page. | 온라인·무료 3시간(구글 미트) + 수료 시 **200만원 상당** 사이트 제작 쿠폰. 예비 포함. 신청 https://academy.runmoa.com/classes/9615 . K-Startup **179651**. | https://chchclub.com/notice/179651 |
| 8 | 북구 창업지원오피스 | **OPEN** | **2026-10-26 09:00 ~ 2026-11-13 18:00** (방문·우편 도착분) | Detail 제목에 `[모집 중]` 배지는 없음. 제목 `[북구청] 2026년 창업지원오피스 신규 업체 모집 공고`. 예비 또는 3년 미만, **1개 업체**, 31.5㎡, 입주 2027.1.8~2028.1.7, 입주부담금 없음(관리비·공공요금 별도). **입주 후 6개월 이내 사업자등록 필수**. 방문·우편만(팩스·이메일 불가). 목록 1쪽에도 동일 기간, `마감 5일전`. | https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00005093 |
| 9 | Spark-up 1876 | **OPEN** (news + apply URL) | 연합뉴스: **11월 16일까지** (시각 없음). 이전 브리핑의 18:00는 **이번 확인에서 재확인 못 함**. | 연합뉴스 2026-10-26: 예비 또는 창업 1년 미만, 개인 또는 최대 4인, 지역 제한 없음. 발표평가 10팀 내외 → 최종 4팀. 시상 분야별 최우수 300만·우수 200만 × 2분야 = **총 1,000만원**. 공식 접수 https://www.go-simsa.com/recruit/Jozu4OXw (HTTP 200, 제목 `해양 창업아이디어 공모전 「Spark-up 1876」`만 추출, **JS라 마감 시각·본문 미추출**). | https://www.yna.co.kr/view/AKR20261026052900051 ; official apply (JS) https://www.go-simsa.com/recruit/Jozu4OXw |
| 10 | AI 올라운더 8기 | **OPEN** | Official K-Startup: **2026-09-28 ~ 2026-11-16 00:00** | 상세 페이지 모집중. 대상 만 20~39세, 업력 예비창업자, 내일배움카드. 제외: 사업자등록 기준 3년 이상(폐업이력 포함). 교육 2026.11.16~2027.3.12, **평일 09:00~18:00 오프라인** KDT 강의장. 총 교육비 **12,016,000원** / 국비 97% **11,616,000원** / **자부담 400,000원** (훈련장려금으로 상쇄 가능 안내). | https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179353 |
| 11 | 스쿨모아 강의사이트 | **OPEN** | **2026.11.03 ~ 2026.11.19** (D-11). Clock time not on page. | 온라인·무료 3시간 + 수료 시 **200만원 상당** 쿠폰. 예비 포함(“사업자 등록 전” 문구). 신청 https://academy.runmoa.com/classes/9576 . K-Startup **179702**. | https://chchclub.com/notice/179702 |
| 12 | 창업 A-Z 교육 | **OPEN** | **2026.10.28 ~ 2026.11.25** (D-17). Clock time not on page. | 하우그로우 원격평생교육원. 대상 (예비)창업자·기창업자·수강 희망자. **비용 미기재**. 신청 https://lms.howgrow.io/kstartup . K-Startup **179650**. | https://chchclub.com/notice/179650 |
| 13 | K-Tech 트랙5 온라인 | **OPEN** | Official Google site: TRACK 5 **접수진행중** (날짜 숫자 없음). Secondary gendoc/K-Startup 전재: **2026.09.10 10:00 ~ 2026.11.27(금) 18:00**. | 공식 홈: 교육비 **무료**, 정원 **40명 선착순**, 대상에 예비창업자 포함. TRACK 1~3 종료, TRACK 4 “11월 접수진행중”(집체), TRACK 5 “접수진행중”(온라인 역량강화). | Official https://sites.google.com/view/2026k-tech0/%ED%99%88 ; secondary https://gendoc.ai/grants/6764 |
| 14 | 취약분야 상시 컨설팅 | **OPEN** (aggregator) | **2026.10.14 00:00 ~ 2026.11.29(일) 23:59** | aitimeskorea는 K-Startup 수집 페이지. 예비·기창업자, 무료 멘토링. 온라인(ZOOM) 또는 오프라인, 평일 14:00·15:30. 주관 강동구 청년해냄센터 02-488-6880. **원문 K-Startup 상세는 이번 라운드에서 직접 열지 않음**. | https://aitimeskorea.com/navigator/11-10pd8wv |
| 15 | 대구 창업-BuS Station IR | **OPEN** | Official DASH: **2026-03-04 09:00 ~ 2026-11-30 23:59** | 공식 상세 제목 `[상시모집] 대구 창업-BuS Station IR 참여기업 모집 공고`. 예비 또는 설립 7년 미만. 매주 화요일까지 신청 → 해당 주 목요일 14:00, 대구창경 3층 Station 피칭 Zone (대면). startupcompass 정리는 2026.10.24 원문확인으로 같은 내용. **브리핑 링크는 DASH 공식 URL을 쓰는 편이 좋음.** | Official https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00004717 ; secondary https://startupcompass.kr/n-dcei-bus-station-ir-2026 |
| 16 | 북구 기업경영지원단 무료 경영자문 | **OPEN** | **2026-10-30 09:00 ~ 2026-12-31 09:00** (헤더). 본문 “연중 수시”. | 대상 **관내** 중소기업 및 예비창업자. 상담비용 전액 무료. 이메일 `jnuri323@korea.kr` 또는 팩스·방문(신청 후 확인 전화 필수). 문의 053-665-2662. `[모집 중]` 배지 없음. | https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00005094 |
| 17 | 2026 하반기 언론홍보 무료 기사 배포 | **OPEN** | 본문 접수기간 `8.26.(수)~ 12.31.(목) 00:00`. 페이지 헤더는 `마감 2026-12-30`. | 주관 (주)한국법률데이터. 대상에 예비창업자 포함, 전국. 아직 닫힌 배너 없음. 마감 표기가 헤더 12/30 vs 본문 12/31 00:00로 어긋남 → 신청 전 원문 재확인. | https://www.wepiu.kr/announcements/startup-pub-9b67874407d6dd6168b09a68 |
| 18 | 스타트업 원스톱 온라인 심화상담 | **OPEN** (상시) | 종료일 없음 (상시 서비스 페이지) | FAQ: 전국 예비창업자 및 창업기업, **소상공인 아닌 기술창업**. 지원한도 문구 “기업별 **300만원**”(해외 법률 일부는 한도 포함/미포함 구분). 온라인 신청 시 온라인 답변. | https://www.k-startup.go.kr/onestop |

**Open-count hint:** all 18 listed items are still open this morning. None newly closed. Do not drop any of the 18 for “closed”.

---

## A2) Annual-list items that are “open” for later-stage founders

Do **not** add these to the 예비 신청가능 list.

| 사업 | Status | Deadline | Eligibility / notes | URL |
|------|--------|----------|---------------------|-----|
| 남구다운 청년 창업 지원사업 3차 | **OPEN** (later-stage / 예창패 위험) | VS: **2026.10.02 09:00 ~ 2026.11.12(목) 18:00** (`마감5일전`). DASH 목록 PROJECT_00005072는 시작일을 `2026-09-01 09:00`으로 표기, 종료는 동일 11/12 18:00. | ❶유형 예비창업: 대구 **남구에서 창업**을 희망하는 청년 예비창업자(팀). 사업화 지원금 **1개社당 최대 2,000만원**, **자부담 5% 이상**. 제외에 **인터넷 창업·무점포 창업**, 공유오피스·자택 사업장 등. **선발 5팀 수치는 이번 VS 본문에 없음** (이전 브리핑 값, 첨부 공고문 미파싱). ❌ 사업화 수혜·사업자등록 가능성 → 예창패 보존 목적과 충돌. | https://www.venturesquare.net/announcement/1119312 ; DASH list PROJECT_00005072 |
| IBK창공 2027 상반기 대구 4기 | **OPEN for 창업기업 only** | DASH: **2026-10-19 09:00 ~ 2026-11-13 14:00** | Official https://www.ibkchanggong.com/scr/appl/applRecrtVw001.do → **HTTP 403**. DASH PROJECT_00005076: 대상 **창업자**, 업력 **7년 미만**, “공고 마감일 기준 7년 이내 창업기업”. 선정 대구 **10개社 내외** (마포·구로·대전·부산 20, 광주·대구 10, 중복지원 불가). 예비 대상 아님. | DASH https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do&project_id=PROJECT_00005076 |
| 대구 창업-비상(飛上) | **Listed OPEN on DASH header; body dates conflict** | Header/list PROJECT_00005059: **2026-10-22 09:00 ~ 2026-11-30 09:00**, 대상 **창업자**, 업력 7년 미만. | 상세 본문 지원내용에는 `신청기간 : 2026. 9. 22.(화) ~ 10. 5.(월)`이 그대로 남아 헤더와 불일치. 지원대상은 창업 7년 이내 기술창업기업 + 협업기관 선정/입주 등(기보 보증 트랙). **예비 대상 아님.** 첨부 공고문(.hwp)은 이번 라운드에서 파싱하지 못함. | https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00005059 |

---

## B) Daegu-local sweep

### B1. DASH list (https://startup.daegu.go.kr/index.do?menu_id=00002552)

List reachable (WebFetch 200; curl HEAD on index.do sometimes 400, GET list 200). Default list is paginated (10 per page, 214 pages of archive mixed with open items).

**Page 1 (still-open / recently posted):**
- PROJECT_00005087 경북대 앵커3-5 멘토링·3D프린팅 — 2026-11-01 ~ 2027-02-28, 예비+창업. Previously excluded (제조·사업자등록 요건). Not re-opened as IT/예창패-safe.
- PROJECT_00005095 「2026년 창업도시 프로젝트」 기술이전 지원 — 2026-11-05 09:00 ~ **2026-11-20 16:00**, **창업자 only**. Not for 예비.
- PROJECT_00005085 벤처확인 인증준비기업 맞춤형 무료 진단 — ~11/30 23:59, 일반기업.
- PROJECT_00005084 벤처·이노비즈·메인비즈 스케일업 밋업 — ~11/30 23:59, 일반기업.
- PROJECT_00005094 북구 경영자문 — known (#16).
- PROJECT_00005093 북구 오피스 — known (#8).
- PROJECT_00005092 대구 중소기업 정보보호 우수기업 — 2026-10-28 ~ **2026-11-12 16:00**, 일반기업.
- PROJECT_00005090 계명대 앵커 딥테크 (예비)추가 모집 — **~11/09 16:00** (see full fields below; **exclude** unless user matches 석·박사/고경력/스핀오프).
- PROJECT_00005082 대구 AX 창업위원회 컨퍼런스 제조 AI 공모전 — ~11/10 18:00, 일반기업.
- PROJECT_00005077 KNU-대구앵커 청년 연구자 경진대회 추가모집 — header ~2027-01-31 but **body describes 10/22~10/26 extra round already past** (see below). Do not treat as open.

**Page 2 highlights:**
- PROJECT_00005076 IBK창공 — see A2.
- PROJECT_00005072 남구다운 — see A2.
- PROJECT_00005059 비상 — see A2.
- PROJECT_00005056 대구스타트업 리더스포럼 제65차 IR피칭 — ~11/24 18:00, **창업자**.
- PROJECT_00004983 달서구 청년 창업 멘토링 — ~11/30 09:00, 예비 표기 (see full fields; **not newly posted**, 달서구 연결 필요 가능).
- PROJECT_00004953 Pre D-Link 5기 — header ~11/30 09:00 but body `모집 기간 26.7.24. ~ 26.8.7.` → **STALE**. Previously treated as closed 8/28. Do not re-add.

**Page 3:** PROJECT_00004717 BuS Station IR official (known #15).

**Page 4:** PROJECT_00005091 AI academy `[모집 중] 오늘 마감` (known #1). Also 대경권 엔젤투자 피칭룸 (예비+창업, ~11/24 09:00) — detail **not fetched** this run; do not invent eligibility.

No brand-new DASH posting that is clearly 예비 + IT + 무자본 + 예창패-safe.

### B2. 대구테크노파크

| URL | Result |
|-----|--------|
| https://www.ttp.org/ | First curl **HTTP 200**, homepage loaded. Hero/news: 소상공인 AI 활용지원 **대경권 주관기관 선정**(공고가 아님), 스포츠산업 창업지원 “**3월 중 14개사 모집 예정**”(미래). 현재 열려 있는 예비 IT 공고는 홈 추출문에서 확인되지 않음. |
| 사업공고 board 추정 URL 여러 개 | 이후 curl **실패(000/ERR)**. 게시판 목록은 이번 라운드에서 열지 못함. |
| https://dgtp.or.kr/ | WebFetch **500**. |
| https://www.daegutp.or.kr/ | curl **실패**. |

→ TP에서 예비 IT 무자본 신규 공고를 **확인하지 못함** (홈에는 없음, 게시판 미접속). Invent하지 말 것.

### B3. University startup centers

| 학교 | URL / result | Open program a non-student 예비 might join? |
|------|----------------|-----------------------------------------------|
| 경북대 창업지원단 | https://startup.knu.ac.kr/ HTTP 200 | 공지: 경북 BuS, 이노 로컬 커넥트(지난 10월), 대경권 캠퍼스 IR 챔피언십(대상 **대구·경북 소재 대학(원) 재학생 또는 졸업 3년 이내**, 마감 텍스트가 `11월 1…`로 잘려 정확한 날짜 미확인, 게시 10-21), IBK창공 안내. **비학생 일반 예비용 신규 없음.** |
| 경북대 창업교육팀 | https://changup.knu.ac.kr/changup HTTP 200 | 80주년 대학(원)생 경진대회는 이미 1차 평가 결과(2차 11/12~13). **[KNU 벤처 메이커스] 재학생만**, 신청 ~**11/20 18:00**, 캠프 11/26~27 경주. 학생 전용. |
| 계명대 | https://startup.kmu.ac.kr/ HTTP 200이나 내용이 **글로벌창업대학원** 사이트. 학사/입학 공지(대학원 신입 등)만 확인. 비학생 예비 대상 신규 창업공고 없음. 딥테크 추가모집은 DASH PROJECT_00005090으로 확인. | 해당 없음 (딥테크는 자격 협소, 아래 참조) |
| 영남대 창업지원단 | https://www.yustartup.com/user/notices 페이지는 열림 | WebFetch 결과에 **2024-08-19 ESG 창업경진대회**만 보임. 2026-11 신규 공고는 이 추출본에서 확인 못 함 (JS/목록 제한 가능). |
| 대구대 창업지원단 | https://dustartup.daegu.ac.kr/front/board/list.php?code=notice&mid=0033%2C0034 | WebFetch **timeout**. |
| 대구대 앵커/RISE | https://rise.daegu.ac.kr/article/NOTICE/list HTTP 200 | **G-Bridge 챌린지 캠프** (10/22 게시): 대상 **권역 내 대학(원)생(휴학생 포함)**, 접수 **~2026.10.31 18:00 → 이미 마감**. 학생 전용. 11/6 게시 `[로컬창업] G-Bridge 레전드 … 특강 안내`는 제목이 ‘안내’라 신규 모집으로 단정하지 않음(상세 미fetch). |

### B4. Free Daegu incubation space

| 공간 | Notes |
|------|-------|
| 북구 창업지원오피스 | Known #8. Free rent (관리비 별도), but **6개월 내 사업자등록** + 방문·우편. |
| DASH/스케일업허브 입주 | 11/7 브리핑: 2차 마감, 다음 차수 미정. 오늘 목록 1~4쪽에 신규 입주 모집 없음. |
| 동성로 1인 창조기업 지원센터 PROJECT_00001020 | 접수 헤더 2026-04-03 ~ **2026-12-31 17:00**, 대상 필드 `1인 창조기업`. 본문은 “(예비)창업자”도 언급하나 **K-Startup 1인 창조기업 정회원 필수**. 예비가 사업자 없이 입주 가능한지는 첨부 공고문 미확인. 무료 여부도 본문에 없음. **신청가능 목록에 넣지 말 것.** |
| KTL 대구분소 입주 PROJECT_00004724 | 상시 ~12/31 23:59, 예비+창업 표기. 위치 서구 와룡로 307. **무료 아님**: 소형 **월 20만원**(부가세 별도)+관리비 약 12~14만원. 디지털 헬스케어 우대. 무자본 필터와 안 맞음. |
| 한국업사이클센터 2차 입주 PROJECT_00005079 | 목록 4쪽 `오늘 마감` 11/8 17:00, 대상 **일반기업**. 예비 목록 아님. |

---

## C) Full fields — Daegu items found in the sweep (not automatically “신규”)

None of these should be added to the eligible 📂 list without the caveats below. **No clearly new, filter-matching Daegu notice** was verified today.

### C1. [계명대학교 앵커] 2026 대학 중심 딥테크 창업 활성화 (예비)추가 모집 — exclude

- **Name:** [계명대학교 앵커]「2026 대학 중심 딥테크 창업 활성화 기반 조성 사업」 (예비)창업자 추가 모집  
- **URL:** https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00005090  
- **Organizer:** 계명대 창업지원단 (DASH 기관명 표기는 대구스케일업허브)  
- **Deadline:** **2026.10.30 ~ 11.9.(월) 16:00**, 이메일 `rhaehf0121@kmu.ac.kr`  
- **Support:** Deep-Tech 창업 기획, 전문가 컨설팅, 전주기 기획. 기획 대상 중 우수 아이템 **시제품 제작 3건**. 기간 선정 후 ~2027.1.31.  
- **Scale:** 추가 모집 **총 2명(팀)**. 시제품 3건(기획 지원 6명(팀) 중 선정 — 본문 표현). 현금 지원 금액은 상세 본문에 없음.  
- **Eligibility:** 다음 중 하나. (1) 지정 산단 입주기업 **10년 이상** 고경력 재직/퇴직(예정)자 (2) 스핀오프(창업기업 대표·재직·퇴직자) (3) 계명대·경북대·DGIST·지역 마이스터대학원 등 **석·박사 재학/졸업(예정)**. 분야: 모빌리티·헬스케어·로봇·ABB(AI·Big Data·Blockchain)·기타 딥테크.  
- **예창패:** DASH 분류 **사업화**. 시제품 지원이 정부 사업화 수혜로 잡힐 수 있음 → ⚠️ 불명확, 예창패 보존 목적이면 비추천.  
- **Online/offline:** 접수 이메일. 교육/기획 형태는 대면 가능성 높으나 상세 본문에 온/오프 명시 없음.  
- **자부담:** 본문에 자부담 문구 없음 (미확인).  
- **Why exclude:** 11/7에도 본 항목(부적합). 일반 예비 IT·무경력/비석박사에게 자격 안 맞음. 신규 게시 아님.

### C2. 달서구 청년 창업 멘토링 — not newly posted; 달서구 연결 필요할 수 있음

- **Name:** 달서구 청년 창업 멘토링  
- **URL:** DASH https://startup.daegu.go.kr/index.do?menu_id=00002552&menu_link=%2Ffront%2Fproject%2FprojectFrontDetail.do%3Fproject_id%3DPROJECT_00004983  
  신청 https://d-youth.or.kr/program/view/343/?category1=2&category2=21 (WebFetch 본문 비어 있음, JS 가능)  
- **Organizer:** 계명대 창업지원단 / 문의 달서구 청년창업지원센터 053-628-1006  
- **Deadline:** DASH 헤더 **2026-08-11 09:00 ~ 2026-11-30 09:00**. 본문 “지원기간: 2026년 11월까지 (예산소진 시 종료)”.  
- **Support:** 멘토링 기업당 **최대 2회(4시간)**, 제조·경영 등 8개 분야.  
- **Scale:** 회당/총액 미기재. 사실상 무료 상담(비용 문구는 ‘지원’이며 유료 명시 없음). 선발 인원 미기재.  
- **Eligibility:** ① 지역 소재 7년 미만 청년창업기업(예비 포함) ② 주민등록상 주소지 또는 달서구 소재 학교·회사 소속 18~39세 청년창업기업(예비 포함) ③ 제조업·지식서비스업 등 기술창업 (단순 서비스업 제외). 나이 헤더 만 20~39.  
- **예창패:** 멘토링만이면 ✅ 영향 없을 가능성이 큼 (사업화 자금 아님).  
- **Online/offline:** DASH 본문에 온/오프 명시 없음. 센터 멘토링이라 대면 가능성.  
- **자부담:** 본문에 없음.  
- **Note:** 8/11부터 열린 **기존 상시성 공고**. 어제 18건 목록에는 없었음. 이용자 주소가 달서구인지는 공유 프로필에 없음(대구만 명시). **달서구 거주/소속이 확인되기 전에는 📂에 넣지 않는 것을 권장.** 신규(오늘 처음 뜬 공고)로 쓰지 말 것.

### C3. KNU-대구앵커 청년 연구자 경진대회 추가모집 — STALE / exclude

- DASH PROJECT_00005077 헤더: 2026-10-06 ~ **2027-01-31 23:59**, 예비+창업, 만 20~39, 업력 3년 미만.  
- 본문: 추가 모집기간 **2026.10.22 ~ 10.26**, 서류평가 10/28·발표 10/30으로 이미 지난 일정, 사업설명회 11/2~ . 선정 15개 사, 사업화 지원금 **최대 1,000만원/700만원**.  
- **헤더와 본문 불일치.** 본문 기준으로는 추가모집이 끝남. “청년 연구자” + 사업화 지원금은 예창패 ❌ 위험. 📂에 넣지 말 것.

### C4. 「2026년 창업도시 프로젝트」 기술이전 지원 — 창업자 only

- PROJECT_00005095, 접수 2026-11-05 09:00 ~ 2026-11-20 16:00, 대상 **창업자**. 예비 목록 금지. 상세 본문은 이번 라운드에서 깊게 파싱하지 않음(대상 필드만으로 제외).

---

## D) Source check status

| Source | HTTP / result | New eligible Daegu item |
|--------|---------------|-------------------------|
| DASH 목록 p.1–5 + key details | 200 | 0 matching 예비·IT·무자본·예창패 |
| DASH 05091 / 05093 / 05094 / 05059 / 05076 / 05090 / 04983 / 04717 / 05077 / 04953 / 01020 / 04724 | 200 | — |
| K-Startup 179353 (올라운더) | 200 | — |
| K-Startup /onestop | 200 | — |
| IBK 공식 신청 | **403** | used DASH instead |
| go-simsa Spark-up | 200 but **JS-empty body** | — |
| orangepark 러닝메이트 | 200 but **JS-thin** | eopla + gendoc cross-check |
| d-youth 달서구 멘토링 신청 | WebFetch empty | — |
| ttp.org homepage | 200 | 0 current 예비 IT calls on homepage |
| ttp.org 사업공고 board | **failed** | unknown |
| dgtp.or.kr | **500** | — |
| daegutp.or.kr | **failed** | — |
| startup.knu.ac.kr / changup.knu.ac.kr | 200 | student-only only |
| startup.kmu.ac.kr | 200 (대학원 사이트) | 0 |
| yustartup notices | 200, stale/partial extract | 0 verified |
| dustartup.daegu.ac.kr | **timeout** | — |
| rise.daegu.ac.kr | 200 | G-Bridge 학생·10/31 마감 |

---

## E) Briefing-writer checklist

1. All **18** previously open eligible items remain open this morning. Do not mark any as closed.  
2. ⭐📵 생성형 AI 아카데미 — **오늘** 마감. DASH 헤더/목록 **23:00** (본문 24:00 한 줄은 무시). 무료, 30명 내외, 교육 11/20~29 대면.  
3. 청년 어촌공모전도 **오늘** 마감(날짜 11/8 확인, 시각은 공식 페이지에 명시 없음).  
4. BuS Station IR 링크는 startupcompass 대신 **DASH PROJECT_00004717**을 권장. 마감 11/30 23:59 재확인.  
5. Spark-up 공식 접수는 https://www.go-simsa.com/recruit/Jozu4OXw . 마감 **11/16**(연합뉴스). **18:00는 이번 확인에서 재확인 못 함.**  
6. CBC 최소 2인·영어 피칭은 공식 https://ainnov.co.kr/cbc 에서 재확인.  
7. 연간: 남구다운 ~11/12 18:00 유지(❌ 예창패·자부담 5%+). IBK ~11/13 14:00, 창업기업만(공식 403, DASH로 확인). 비상은 DASH 헤더 ~11/30 09:00·창업자만, 본문 날짜(9/22~10/5)와 불일치.  
8. **신규 대구 적합 공고 0건.** 계명 딥테크(11/9 16:00)는 자격 협소·사업화 분류라 제외. 달서구 멘토링은 기존 공고이며 달서구 연결이 불명확하면 📂에 넣지 말 것.  
9. 대학: 경북대 벤처 메이커스·80주년 대회·캠퍼스 IR는 학생/최근졸업 중심. 대구대 G-Bridge는 학생 전용·10/31 마감.  
10. 예창패: 오늘 새로 추천할 사업화 지원금 없음. 북구 오피스 6개월 내 사업자등록 ⚠️ 유지.
