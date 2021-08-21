# Crawling Sample

특정 웹사이트를 대상으로 크롤링(Crawaling) 샘플 만들기

> 현재 프로젝트에서는 '네이버 뉴스' 페이지를 대상으로 함

## Install Libaray

### urllib3

urllib는 URL 작업을 위한 패키지

```sh
pip install urllib3
```

### Beautifulsoup4

`request.text`를 이용해 가져온 데이터는 텍스트형태의 html을 객체로 만들어 사용할 수 있도록 하는 라이브러리이다.

```sh
pip install beautifulsoup4
```

## Issues

### 인증 오류

`https` url을 open 할때, MacOS 사용시 아래와 같은 인증서 오류가 발생한다.

```
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)'))
```

> [여기](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)를 참고하여 해결함.
