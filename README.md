# Team Project-MountainGO


### Preview


<p align= "center"> <img width="600" height="250" alt="스크린샷 2022-05-12 오후 8 14 07" src="https://user-images.githubusercontent.com/85288036/168061679-4740e17e-004b-4f97-92ab-cace2eb6fcb1.png"> </p>


<p align= "center"><img width="600"height="300" src="https://user-images.githubusercontent.com/85288036/168066827-d26a3098-c098-4005-b7f1-7149702e2b73.png"></p>


<p align= "center"><img width="600" height="320" src="https://user-images.githubusercontent.com/85288036/168066834-de9635d6-3a4e-41e5-bffd-c4841271a245.png"></p>
  
<p align= "center"><img width="600" height="300" src="https://user-images.githubusercontent.com/85288036/168066847-16637f0e-8ff7-4e15-a5b7-eccb14527f70.png"></p>



#### 내용
- 등산의 즐거움을 붙일 수 있도록 도와주는 웹 사이트

- 지도를 통해 산의 위치와 정보를 알 수 있도록 하며, 등산 인증샷을 통해 성취감을 줄 수 있다.
#### 목표
- Jinja2 템플릿 엔진을 이용한 서버사이드 렌더링 사용
- JWT 인증 방식으로 로그인 구현
- 지도 API 사용, 산 마킹
- 스토리지를 이용한 사진 업로드
- 서버 배포


#### Member
김하연 (팀장)   
정인성     
김민지

### Note
  
  - Tags
  -  S.A(https://summerlaftel07.tistory.com/34)
- Dependencies
  - flask
  - pymongo
  - PyJWT
  - dnspython
  - Jinja2

  # MountainGo 회의록

  **5월 9일 회의록**

  - 우리 조 프로젝트 제목 : 마운틴 고
  - 개발해야할 기능
    > 로그인, 지도API , 등산 인증, 인증샷, 로그인, 회원가입 : ( 로그인 POST / Get ) , ( 회원가입:POST ) , ( 사진업로드 : POST )
    > 지도 API , 산 API+ 마킹 ( GET 방식 )
    > 서버response 로그인-회원리스트 회원가입-회원 데이터 지도보기- 지도API
  - 페이지 담당 완료

**5월 10일 회의록**

- 맡은 페이지별로 사이트뼈대와 기능 구현
- Git Repo 에 각자 브랜치 생성과 커밋과 푸시 업데이트
- 내일 오전까지 팝업 기능 + 인증사진 업로드 기능 구현
- 내일 오후부터 각자 코드 Git으로 푸쉬 후 코드 병합 예정
- 각자의 에러와 오늘의 TIL 공유
- 스파르타 웹 개발 주차별로 맡아 요점정리

**5월 11일 회의록**

- 각자 맡은 기능 구현 마무리 단계
- AWS EC2 이용하여 아이피 배포까지 완료
- 배포중 생긴 로그인 오류 발생 ( .decode(utf-8) 해결완료 )
- 지도 APi 오류 발생 ( 네이버 클라우드에서 해결완료 )
- 마커 값을 불러오는 에러 발생 ( 미해결 )
- 내일 까지 미해결 문제 해결과 3번째 페이지 css 구성 및 사진 업로드

**5월 12일 회의록**

- 마커 값 불러오는 에러 (해결완료)
- 사이트 배포 및 도메인 배정완료 :: http://sparta-ins.shop/
- 유튜브데모 영상 찍기 완료 :: https://www.youtube.com/watch?v=IAo8xzVYWck


