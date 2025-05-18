# 사업자등록정보 확인 웹 애플리케이션

한국 국세청의 사업자등록정보 확인 API를 활용한 웹 애플리케이션입니다.

## 기능

- 사업자등록정보 진위확인: 사업자등록번호, 개업일자, 대표자명 등을 통해 정보의 진위를 확인합니다.
- 사업자등록 상태조회: 여러 사업자등록번호의 상태를 한 번에 조회합니다.

## 설치 및 실행 방법

### 로컬 개발 환경에서 실행하기

1. 이 저장소를 클론합니다:
   ```
   git clone https://github.com/ironman-29/business-verification-app.git
   cd business-verification-app
   ```

2. 필요한 패키지를 설치합니다:
   ```
   pip install -r requirements.txt
   ```

3. 환경 변수를 설정합니다:
   ```
   # Linux/macOS
   export SERVICE_KEY="your_api_key_from_data_go_kr"
   
   # Windows
   set SERVICE_KEY=your_api_key_from_data_go_kr
   ```

4. 애플리케이션을 실행합니다:
   ```
   python app.py
   ```

5. 웹 브라우저에서 `http://localhost:5000`으로 접속합니다.

### API 키 발급 방법

1. [공공데이터포털(data.go.kr)](https://www.data.go.kr/)에 회원가입 및 로그인합니다.
2. "국세청_사업자등록정보 진위확인 및 상태조회 서비스" API를 검색하고 활용 신청합니다.
3. 승인 후 발급된 서비스 키를 환경 변수로 설정합니다.

## 배포 방법

이 프로젝트는 Render를 통해 배포할 수 있도록 설정되어 있습니다.

1. [Render](https://render.com/)에 가입하고 새 웹 서비스를 생성합니다.
2. GitHub 저장소와 연결합니다.
3. 다음 설정을 적용합니다:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - 환경 변수에 `SERVICE_KEY`를 추가합니다.

4. GitHub Actions를 통한 자동 배포를 설정하려면 저장소의 Secrets에 다음을 추가합니다:
   - `RENDER_SERVICE_ID`: Render 웹 서비스 ID
   - `RENDER_API_KEY`: Render API 키

## 기술 스택

- Backend: Flask (Python)
- Frontend: HTML, JavaScript, Bootstrap
- 배포: Render, GitHub Actions

## 라이선스

MIT License

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새 기능 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`).
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`).
4. 브랜치를 푸시합니다 (`git push origin feature/amazing-feature`).
5. Pull Request를 생성합니다.
