"""
HTTP Response Code

클라이언트가 서버에 요청(request) 시 서버가 응답(response)을 코드로 보내준다.

 응답 코드는 100번대 단위로 이루어져있다.
100번대 끼리 유사한 형태의 응답코드로 이루어져있고,
200번대 끼리 유사한 형태의 응답코드로 이루어져 있는 형태이다.
(200번대 응답은 서버에서 정상 처리되어 응답한 경우임)

[Response Class]
HTTP Response 처리를 담당하는 클래스
code	code명	상태
1	Informational	리퀘스트를 받아 처리중 상태
2	Success	리퀘스트를 처리 완료
3	Redirection	리퀘스트의 처리 완료를 위해 추가 동작 필요
4	Client Error	클라이언트 요청 처리 에러
5	Sever Error	클라이언트 요청은 문제없으나 서버에서 처리 에러

[주요 응답 코드]
●200 Response
-200(OK)
 요청 처리 성공
-204(No Content)
 요청 처리 성공하였으나 돌려줄 리소스 없음

●400 Response
-400(Bad Request)
 클라리언트 요청 구문이 잘못됨
-401(Unauthorized)
 요청 처리를 위해 HTTP 인증(BASIC, DIGEST 인증) 정보가 필요
 접근 허용 차단
  ex) 서버는 로그인이 필요한 페이지에 이 응답을 제공할 수 있음
-403(Forbidden)
  접근 금지 응답
  사용자가 리소스에 대한 필요 권한을 갖고 있지 않음
   ex) 관리자 페이지 접근 등
-404(Not Found)
 클라이언트가 요청한 리소스가 서버에 없음
-405(Method Not Allowed)
 허용되지 않는 HTTP 메서드를 사용함

●500 Response
-500(Internal Server Error)
 서버에서 클라이언트 요청 처리 중에 에러 발생
-505(HTTP version Not Supported)
 해당 HTTP 버전에서는 지원되지 않는 요청임
"""