# HTTP 프로토콜 처리 로직 보유 
from http.server import HTTPServer, BaseHTTPRequestHandler

class Myhandler(BaseHTTPRequestHandler):
    # 매서드 오버라이딩
    def do_GET(self):
        # 속성 재정의
        # 상태
        self.send_response_only(200, 'OK')
        # 헤더
        self.send_header('Content-type', 'text/plain')
        # 헤더 마무리
        self.end_headers()
        # 바디 
        self.wfile.write("Hello Hello")
        
#모듈이 아닌, 프로그램으로 불러오는 경우 실행
if __name__ == "__main__":
    server = HTTPServer
    
    #서버 실행 (포트 8890, 직접 만든 HTTP 로직 사용)
    server = HTTPServer(('', 8890), Myhandler)
    print("Started Webserver on port 8890")
    print("Press ^C to quit Webserver")
    
    #서버 구동
    server.serve_forever()