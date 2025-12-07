# HTML PPT 디자인 가이드 - 디즈니 발표용

## 추천: Reveal.js (가장 강력하고 사용하기 쉬움)

### 왜 Reveal.js인가?
- ✅ 무료 오픈소스
- ✅ 반응형 디자인 (모든 화면 크기)
- ✅ 키보드/터치 제어
- ✅ PDF 내보내기 가능
- ✅ 애니메이션 효과 풍부
- ✅ 스피커 노트 지원
- ✅ 코드 하이라이팅
- ✅ 차트 삽입 쉬움

---

## 디즈니 테마 디자인 시스템

### 색상 팔레트

```css
/* 디즈니 공식 색상 */
--disney-blue: #0064D2;        /* 메인 블루 */
--disney-light-blue: #4A9EFF;  /* 밝은 블루 */
--disney-dark-blue: #003D82;   /* 어두운 블루 */
--disney-gold: #FFD700;        /* 골드 (강조) */
--disney-white: #FFFFFF;       /* 화이트 */
--disney-black: #1A1A1A;       /* 텍스트 */
--disney-gray: #F5F5F5;        /* 배경 */

/* 섹션별 색상 */
--part1-color: #0064D2;   /* 서론 - 블루 */
--part2-color: #00A651;   /* 전략 - 그린 */
--part3-color: #FF6B35;   /* 사례 - 오렌지 */
--part4-color: #8B5CF6;   /* 시사점 - 퍼플 */
```

### 폰트

```css
/* 추천 폰트 조합 */

/* 영문 */
font-family: 'Montserrat', 'Arial', sans-serif;  /* 제목 */
font-family: 'Open Sans', 'Arial', sans-serif;   /* 본문 */

/* 한글 */
font-family: 'Noto Sans KR', sans-serif;  /* 제목+본문 */
font-family: '나눔스퀘어', sans-serif;      /* 대안 */

/* 크기 */
--title-size: 3.5rem;      /* 48px */
--subtitle-size: 2rem;     /* 28px */
--body-size: 1.5rem;       /* 21px */
--small-size: 1.2rem;      /* 17px */
```

---

## 기본 구조 (시작 템플릿)

### 1. 프로젝트 폴더 구조

```
글로벌경영ppt/
├── index.html              # 메인 파일
├── css/
│   ├── custom.css         # 커스텀 스타일
│   └── reveal.min.css     # Reveal.js 기본
├── js/
│   ├── reveal.min.js      # Reveal.js 스크립트
│   └── chart.min.js       # Chart.js (차트용)
├── images/
│   ├── disney-logo.png
│   ├── mickey.png
│   └── ...
└── data/
    └── charts-data.js     # 차트 데이터
```

---

## 2. 기본 HTML 템플릿

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>디즈니의 글로벌 경영전략</title>

    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/white.css">

    <!-- 구글 폰트 -->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Montserrat:wght@600;800&display=swap" rel="stylesheet">

    <!-- 커스텀 CSS -->
    <link rel="stylesheet" href="css/custom.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">

            <!-- 슬라이드는 여기에 -->

        </div>
    </div>

    <!-- Reveal.js JS -->
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>

    <!-- 초기화 -->
    <script>
        Reveal.initialize({
            hash: true,
            transition: 'slide',
            transitionSpeed: 'default',
            controls: true,
            progress: true,
            center: true,
            slideNumber: 'c/t',
            width: 1920,
            height: 1080,
        });
    </script>
</body>
</html>
```

---

## 3. 커스텀 CSS (custom.css)

```css
/* 전역 설정 */
:root {
    /* 색상 */
    --disney-blue: #0064D2;
    --disney-gold: #FFD700;
    --disney-white: #FFFFFF;
    --disney-black: #1A1A1A;
    --disney-gray: #F5F5F5;

    /* 폰트 크기 */
    --title-size: 3.5rem;
    --subtitle-size: 2rem;
    --body-size: 1.5rem;
}

/* 기본 스타일 */
.reveal {
    font-family: 'Noto Sans KR', sans-serif;
    color: var(--disney-black);
}

.reveal h1 {
    font-family: 'Montserrat', 'Noto Sans KR', sans-serif;
    font-size: var(--title-size);
    font-weight: 800;
    color: var(--disney-blue);
    text-transform: none;
    margin-bottom: 1rem;
}

.reveal h2 {
    font-size: var(--subtitle-size);
    font-weight: 700;
    color: var(--disney-blue);
    margin-bottom: 1rem;
}

.reveal p, .reveal li {
    font-size: var(--body-size);
    line-height: 1.6;
}

/* 강조 텍스트 */
.highlight {
    color: var(--disney-gold);
    font-weight: 700;
}

.blue-text {
    color: var(--disney-blue);
}

/* 표지 슬라이드 */
.title-slide {
    background: linear-gradient(135deg, var(--disney-blue) 0%, var(--disney-light-blue) 100%);
    color: white !important;
}

.title-slide h1,
.title-slide h2,
.title-slide p {
    color: white !important;
}

/* 섹션 구분 슬라이드 */
.section-slide {
    background: var(--disney-blue);
    color: white !important;
}

.section-slide h1 {
    color: white !important;
    font-size: 4rem;
}

/* 카드 스타일 */
.card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    margin: 1rem;
}

.card-header {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--disney-blue);
    margin-bottom: 1rem;
}

/* 통계 카드 */
.stat-card {
    background: linear-gradient(135deg, var(--disney-blue) 0%, var(--disney-light-blue) 100%);
    color: white;
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0, 100, 210, 0.3);
    min-width: 300px;
}

.stat-number {
    font-size: 4rem;
    font-weight: 800;
    color: var(--disney-gold);
    display: block;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 1.5rem;
    opacity: 0.9;
}

/* 비교 레이아웃 */
.comparison {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.vs-divider {
    font-size: 3rem;
    color: var(--disney-gold);
    font-weight: 800;
    align-self: center;
    text-align: center;
}

/* 타임라인 */
.timeline {
    position: relative;
    padding-left: 3rem;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background: var(--disney-blue);
}

.timeline-item {
    position: relative;
    margin-bottom: 2rem;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -3.75rem;
    top: 0.5rem;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--disney-gold);
    border: 4px solid var(--disney-blue);
}

/* 표 스타일 */
.reveal table {
    font-size: 1.3rem;
    border-collapse: collapse;
    width: 100%;
}

.reveal table th {
    background: var(--disney-blue);
    color: white;
    padding: 1rem;
    font-weight: 700;
}

.reveal table td {
    padding: 0.8rem;
    border: 1px solid var(--disney-gray);
}

.reveal table tr:nth-child(even) {
    background: var(--disney-gray);
}

/* 아이콘 박스 */
.icon-box {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 80px;
    height: 80px;
    background: var(--disney-blue);
    color: white;
    border-radius: 50%;
    font-size: 2.5rem;
    margin: 1rem;
}

/* 강조 박스 */
.emphasis-box {
    background: linear-gradient(135deg, rgba(0, 100, 210, 0.1) 0%, rgba(74, 158, 255, 0.1) 100%);
    border-left: 6px solid var(--disney-gold);
    padding: 2rem;
    border-radius: 8px;
    margin: 2rem 0;
}

/* 애니메이션 */
.fade-in {
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* 반응형 */
@media (max-width: 1024px) {
    :root {
        --title-size: 2.5rem;
        --subtitle-size: 1.5rem;
        --body-size: 1.2rem;
    }

    .comparison {
        grid-template-columns: 1fr;
    }
}
```

---

## 4. 슬라이드 예시 (주요 타입별)

### 타입 1: 표지 슬라이드

```html
<section class="title-slide">
    <h1>디즈니의 글로벌 경영전략 및 시사점</h1>
    <h2>100년 엔터테인먼트 제국의 성공 전략</h2>
    <br>
    <p>팀명: [팀명]</p>
    <p>팀원: [이름1, 이름2, 이름3]</p>
    <p>2024. XX. XX</p>
</section>
```

### 타입 2: 섹션 구분 슬라이드

```html
<section class="section-slide">
    <h1>Part 2</h1>
    <h2>글로벌 경영전략 분석</h2>
</section>
```

### 타입 3: 통계 카드 슬라이드

```html
<section>
    <h2>숫자로 보는 디즈니 (2023)</h2>

    <div style="display: flex; justify-content: space-around; margin-top: 3rem;">
        <div class="stat-card">
            <span class="stat-number">$82.7B</span>
            <span class="stat-label">연매출</span>
        </div>

        <div class="stat-card">
            <span class="stat-number">1.5억+</span>
            <span class="stat-label">Disney+ 구독자</span>
        </div>

        <div class="stat-card">
            <span class="stat-number">20만+</span>
            <span class="stat-label">직원 수</span>
        </div>

        <div class="stat-card">
            <span class="stat-number">Top 10</span>
            <span class="stat-label">브랜드 가치</span>
        </div>
    </div>
</section>
```

### 타입 4: 비교 슬라이드

```html
<section>
    <h2>Universal vs Disney (테마파크 전쟁)</h2>

    <div class="comparison">
        <div class="card">
            <div class="card-header">Disney (WDW)</div>
            <ul>
                <li><strong>전략:</strong> 생태계 가두기</li>
                <li><strong>강점:</strong> 100년 브랜드</li>
                <li><strong>약점:</strong> 높은 가격</li>
            </ul>
        </div>

        <div class="vs-divider">VS</div>

        <div class="card">
            <div class="card-header">Universal</div>
            <ul>
                <li><strong>전략:</strong> 공격적 확장</li>
                <li><strong>강점:</strong> 혁신적 하드웨어</li>
                <li><strong>약점:</strong> IP 깊이 부족</li>
            </ul>
        </div>
    </div>
</section>
```

### 타입 5: 표 슬라이드

```html
<section>
    <h2>VRIO 분석</h2>

    <table>
        <thead>
            <tr>
                <th>자원/역량</th>
                <th>V</th>
                <th>R</th>
                <th>I</th>
                <th>O</th>
                <th>경쟁우위</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>IP 포트폴리오</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>지속적</td>
            </tr>
            <tr>
                <td>테마파크 문화</td>
                <td>✓</td>
                <td>✓</td>
                <td>△</td>
                <td>✓</td>
                <td>지속적</td>
            </tr>
            <tr>
                <td>스트리밍 기술</td>
                <td>✓</td>
                <td>△</td>
                <td>△</td>
                <td>△</td>
                <td>일시적</td>
            </tr>
        </tbody>
    </table>
</section>
```

### 타입 6: 타임라인 슬라이드

```html
<section>
    <h2>디즈니 글로벌 확장 타임라인</h2>

    <div class="timeline">
        <div class="timeline-item">
            <strong>1923</strong> - 회사 설립
        </div>
        <div class="timeline-item">
            <strong>1983</strong> - 도쿄 디즈니 (첫 해외 진출)
        </div>
        <div class="timeline-item">
            <strong>2006</strong> - 픽사 인수 ($7.4B)
        </div>
        <div class="timeline-item">
            <strong>2009</strong> - 마블 인수 ($4B)
        </div>
        <div class="timeline-item">
            <strong>2019</strong> - Disney+ 런칭
        </div>
    </div>
</section>
```

### 타입 7: 강조 박스 슬라이드

```html
<section>
    <h2>핵심 메시지</h2>

    <div class="emphasis-box">
        <h3 class="blue-text">디즈니의 성공 비결</h3>
        <p>
            <span class="highlight">IP 파워</span> ×
            <span class="highlight">문화 존중</span> ×
            <span class="highlight">전략적 인내</span> ×
            <span class="highlight">과감한 혁신</span>
        </p>
        <p>
            = 100년 지속 가능한 글로벌 기업
        </p>
    </div>
</section>
```

### 타입 8: 차트 슬라이드

```html
<section>
    <h2>5개년 매출 추이</h2>

    <canvas id="revenueChart" width="800" height="400"></canvas>

    <script>
        const ctx = document.getElementById('revenueChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['2019', '2020', '2021', '2022', '2023'],
                datasets: [{
                    label: '연매출 (Billion USD)',
                    data: [69.6, 65.4, 67.4, 82.7, 88.9],
                    borderColor: '#0064D2',
                    backgroundColor: 'rgba(0, 100, 210, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Billion USD'
                        }
                    }
                }
            }
        });
    </script>
</section>
```

---

## 5. 추천 디자인 패턴

### 패턴 1: 아이콘 + 텍스트

```html
<div style="display: flex; align-items: center; margin: 2rem 0;">
    <div class="icon-box">💎</div>
    <div style="margin-left: 2rem;">
        <h3>IP는 21세기 핵심 자산</h3>
        <p>콘텐츠 IP의 전략적 가치 재인식</p>
    </div>
</div>
```

### 패턴 2: 3열 그리드

```html
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
    <div class="card">
        <h3>강점</h3>
        <ul>
            <li>100년 브랜드</li>
            <li>강력한 IP</li>
        </ul>
    </div>
    <div class="card">
        <h3>약점</h3>
        <ul>
            <li>높은 비용</li>
            <li>중국 의존</li>
        </ul>
    </div>
    <div class="card">
        <h3>기회</h3>
        <ul>
            <li>신흥 시장</li>
            <li>기술 혁신</li>
        </ul>
    </div>
</div>
```

### 패턴 3: Before/After

```html
<div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 2rem; align-items: center;">
    <div>
        <h3>Before 2019</h3>
        <p>전통 모델</p>
    </div>
    <div style="font-size: 3rem; color: var(--disney-gold);">→</div>
    <div>
        <h3>After 2019</h3>
        <p>디지털 퍼스트</p>
    </div>
</div>
```

---

## 6. 애니메이션 효과

### Reveal.js 내장 애니메이션

```html
<!-- 순차적 나타남 -->
<ul>
    <li class="fragment">첫 번째 항목</li>
    <li class="fragment">두 번째 항목</li>
    <li class="fragment">세 번째 항목</li>
</ul>

<!-- 다양한 효과 -->
<p class="fragment fade-in">페이드 인</p>
<p class="fragment fade-out">페이드 아웃</p>
<p class="fragment fade-up">위로 나타남</p>
<p class="fragment fade-down">아래로 나타남</p>
<p class="fragment zoom-in">줌 인</p>
<p class="fragment highlight-red">빨간색 강조</p>
<p class="fragment highlight-blue">파란색 강조</p>
```

---

## 7. 반응형 이미지

```html
<section>
    <h2>상하이 디즈니랜드</h2>

    <img src="images/shanghai-disney.jpg"
         alt="상하이 디즈니"
         style="max-width: 80%; height: auto; border-radius: 16px; box-shadow: 0 8px 30px rgba(0,0,0,0.2);">

    <p class="fragment" style="margin-top: 2rem;">
        16년 협상 끝에 2016년 개장
    </p>
</section>
```

---

## 8. 스피커 노트 (발표자 전용)

```html
<section>
    <h2>디즈니의 5대 전략</h2>

    <!-- 슬라이드 내용 -->

    <aside class="notes">
        여기에 발표자 노트를 작성합니다.
        - 강조할 포인트
        - 시간 체크
        - 추가 설명

        단축키 'S'를 누르면 스피커 뷰가 열립니다.
    </aside>
</section>
```

---

## 9. 유용한 단축키

| 키 | 기능 |
|----|------|
| `→` / `Space` | 다음 슬라이드 |
| `←` | 이전 슬라이드 |
| `Home` | 첫 슬라이드 |
| `End` | 마지막 슬라이드 |
| `Esc` / `O` | 오버뷰 모드 |
| `S` | 스피커 노트 |
| `F` | 전체화면 |
| `B` / `.` | 화면 블랙아웃 |
| `?` | 단축키 도움말 |

---

## 10. PDF 출력 방법

### 방법 1: Print-to-PDF

1. URL에 `?print-pdf` 추가
   ```
   http://localhost:8000/index.html?print-pdf
   ```

2. 브라우저에서 인쇄 (Ctrl+P)

3. "PDF로 저장" 선택

### 방법 2: Decktape (고품질)

```bash
npm install -g decktape
decktape reveal index.html presentation.pdf
```

---

## 11. 로컬 서버 실행

### Python (간단)

```bash
# Python 3
python -m http.server 8000

# 브라우저에서
http://localhost:8000/index.html
```

### Node.js (추천)

```bash
npm install -g http-server
http-server
```

---

## 12. 추천 폴더 구조 (최종)

```
글로벌경영ppt/
├── index.html                    # 메인 HTML
├── css/
│   ├── custom.css               # 커스텀 스타일
│   └── print.css                # 인쇄용 스타일
├── js/
│   ├── charts.js                # 차트 스크립트
│   └── animations.js            # 애니메이션
├── images/
│   ├── logos/
│   │   ├── disney-logo.png
│   │   ├── marvel-logo.png
│   │   └── ...
│   ├── screenshots/
│   │   ├── shanghai-disney.jpg
│   │   └── ...
│   └── icons/
│       └── ...
├── data/
│   └── financial-data.json      # 데이터 파일
└── README.md                    # 사용 설명서
```

---

## 13. 성능 최적화 팁

### 이미지 최적화
- 해상도: 1920x1080 이하
- 포맷: WebP (크기 30% 감소)
- 압축: TinyPNG 사용

### 로딩 속도
- CDN 사용 (Reveal.js, Chart.js)
- 이미지 lazy loading
- 폰트 preload

```html
<!-- 폰트 preload -->
<link rel="preload" href="fonts/NotoSansKR.woff2" as="font" type="font/woff2" crossorigin>
```

---

## 14. 체크리스트

### 시작 전
- [ ] Reveal.js 다운로드/CDN 링크
- [ ] 폰트 로드 확인
- [ ] 색상 팔레트 설정
- [ ] 이미지 폴더 준비

### 제작 중
- [ ] 슬라이드 33개 제작
- [ ] 애니메이션 적용
- [ ] 차트 삽입
- [ ] 스피커 노트 작성
- [ ] 반응형 테스트

### 마무리
- [ ] 전체 미리보기
- [ ] 모든 브라우저 테스트
- [ ] PDF 출력 테스트
- [ ] 로딩 속도 체크
- [ ] 백업 저장

---

## 15. 문제 해결

### 문제 1: 폰트가 안 보임
**해결**: CDN 링크 확인, CORS 설정

### 문제 2: 이미지가 안 나옴
**해결**: 경로 확인, 상대 경로 사용

### 문제 3: 애니메이션 느림
**해결**: 이미지 최적화, transition 속도 조정

### 문제 4: PDF 출력이 이상함
**해결**: `?print-pdf` 파라미터 사용

---

## 16. 다음 단계

제가 이제 도와드릴 수 있는 것:

1. ✅ **전체 index.html 파일 작성** (33개 슬라이드 전체)
2. ✅ **완성된 custom.css 파일**
3. ✅ **차트 스크립트 작성**
4. ✅ **샘플 슬라이드 5-10개 먼저 제작**

어떤 것부터 시작할까요?

**추천: 샘플 5개 먼저 만들어서 스타일 확인 후 → 전체 제작** 🚀
