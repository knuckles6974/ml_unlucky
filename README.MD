- 특정한 영화정보를 받아오는 RESTFUL API를구현
- 그에 따른 입력값에 따른 결과값 도출

  ### Postman 설치

#### Postman이란

-REST API 설계 개발

-테스팅을 할 수 있는 GUI 툴로 개발 생산성을 높여주는 프로그램

-Query String이 포함된 GET 방식 호출

-JSON이 사용된 POST 방식 호출이가능한 플랫폼

#### ※ 사 용 방 법 ※

1. Workspances 생성

2. [+} 버튼 클릭

3. GET or POST 요청

4. Body 버튼클릭

form-data, json, text, xml 등의 데이터 타입 중 json 요청 파라미터로 설정

5. 메서드 설정 후 Endpoint 설정 후 Send버튼 클릭

## 기술스택

`Python`

`Django 4.0.6`

`MySQL` or `SQLlite`{command +shift + p 누른 후 sqllite viewer 검색 후 설치 )

## 설치방법

필수 패키지 설치

Requirements.txt

`Django==4.0.6`

`django-cors-headers==3.13.0`

`django-extensions==3.1.5`

`PyMySQL==1.0.2`

$ pip install -r requirements.txt 명령어 실행

서버 실행

$ python manage.py runserver

# 질문 1.

```
{
    "movieinfo": {
        "movieimage": [
            "https://w.namu.la/s/f45387e9868479b97a91b58cc2788a35c9efc51122361b48f8d77ba03b082e9f0e39ea20b939c8bbd127069a4af29156e916e942f80677b78d0864a68b863374934bbd8068a7d271265af7fba5bfd8cfd5fab4046898fb0678cd35aee4fd7227b1333834f571502c849141c98adb24d9"
        ],
        "name": "화양연화",
        "original_name": "In the mood for love ",
        "rating": "9.0",
        "genre": "romance",
        "running_time": 130,
        "director": "왕가위",
        "cast": "양조위, 장만옥",
        "synopsis": "1962년 홍콩. 상하이에서 이주해온 사람들이 주로 거주하고 있는 아파트에 두 가구가 동시에 이사를 온다. 퇴근 후 홀로 있는 시간이 많은 주모운과 소려진은 국수 가게로 가는 길목에서 자주 부딪히게 되고 어느새 이웃으로서 가까워진다.",
        "like": true,
        "dislike": false,
        "teaser": "https://www.youtube.com/watch?v=EqzNNUy-CZA",
        "shorts": "https://www.youtube.com/watch?v=bOq_jnvDXV8",
        "trailer": "https://www.youtube.com/watch?v=WFxDkU-M-J0"
    }
}
```

### JSON 데이터타입으로는 객체가 전달이 되어야합니다.

### HTTP STATUS CODE : 200 "OK"

# 질문 2.

## API 메소드

### 1) . POST(영화기본정보등록)

#### Request

`Post 127.0.0.1/movies/movieinfo`

#### Response

```
{
    "name" : "화양연화",
    "original_name" : "In the mood for love ",
    "rating" : "9.0",
    "genre" : "romance",
    "running_time" : "122",
    "director" : "왕가위",
    "cast" : "양조위, 장만옥",
    "synopsis" : "1962년 홍콩. 상하이에서 이주해온 사람들이 주로 거주하고 있는 아파트에 두 가구가 동시에 이사를 온다. 퇴근 후 홀로 있는 시간이 많은 주모운과 소려진은 국수 가게로 가는 길목에서 자주 부딪히게 되고 어느새 이웃으로서 가까워진다.",
    "like" : "1",
    "dislike" : "0"
}
```

### 1-1) . POST(영화이미지등록)

#### Request

`POST 127.0.0.1/movies/movieimage`

#### Response

```
{
    "image_url" : "https://w.namu.la/s/f45387e9868479b97a91b58cc2788a35c9efc51122361b48f8d77ba03b082e9f0e39ea20b939c8bbd127069a4af29156e916e942f80677b78d0864a68b863374934bbd8068a7d271265af7fba5bfd8cfd5fab4046898fb0678cd35aee4fd7227b1333834f571502c849141c98adb24d9",
    "movieinfo_id" : 3
}
```

### 1-2) . POST(영화비디오등록)

#### Request

`POST 127.0.0.1/movies/movievideo`

#### Response

```
{
    "teaser" : "https://www.youtube.com/watch?v=EqzNNUy-CZA",
    "shorts" : "https://www.youtube.com/watch?v=bOq_jnvDXV8",
    "trailer" : "https://www.youtube.com/watch?v=WFxDkU-M-J0",
    "movieinfo_id" : 3
}
```

## 2) . GET(영화페이지조회)

#### Request

`GET 127.0.0.1/movies/movieinfo/3`

#### Response

```
{
    "movieinfo": {
        "movieimage": [
            "https://w.namu.la/s/f45387e9868479b97a91b58cc2788a35c9efc51122361b48f8d77ba03b082e9f0e39ea20b939c8bbd127069a4af29156e916e942f80677b78d0864a68b863374934bbd8068a7d271265af7fba5bfd8cfd5fab4046898fb0678cd35aee4fd7227b1333834f571502c849141c98adb24d9"
        ],
        "name": "화양연화",
        "original_name": "In the mood for love ",
        "rating": "9.0",
        "genre": "romance",
        "running_time": 130,
        "director": "왕가위",
        "cast": "양조위, 장만옥",
        "synopsis": "1962년 홍콩. 상하이에서 이주해온 사람들이 주로 거주하고 있는 아파트에 두 가구가 동시에 이사를 온다. 퇴근 후 홀로 있는 시간이 많은 주모운과 소려진은 국수 가게로 가는 길목에서 자주 부딪히게 되고 어느새 이웃으로서 가까워진다.",
        "like": true,
        "dislike": false,
        "teaser": "https://www.youtube.com/watch?v=EqzNNUy-CZA",
        "shorts": "https://www.youtube.com/watch?v=bOq_jnvDXV8",
        "trailer": "https://www.youtube.com/watch?v=WFxDkU-M-J0"
    }
}
```

## 3) . DELETE(영화페이지삭제)

#### Request

`DELETE 127.0.0.1/movies/3`

#### Response

```
{
    "message": "삭제완료"
}
```

## 4) . PATCH(영화정보수정)

#### Request

`PATCH 127.0.0.1/movies/3`

#### Response

```
{
    "messeage": "수정완료"
}
```
