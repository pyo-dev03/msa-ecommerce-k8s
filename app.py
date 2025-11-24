from flask import Flask, jsonify, request
import sys
import datetime

# Flask 애플리케이션 생성
app = Flask(__name__)

# 간단한 상품 데이터
products = [
    {"id": 1, "name": "Product 1", "price": 1200000},
    {"id": 2, "name": "Product 2", "price": 25000}
]

# '/products' 경로로 요청이 오면 상품 목록을 JSON으로 반환
@app.route("/products")
def get_products():
    # [추가됨] 통신 로그 시각화
    # 표준 에러(stderr)로 출력해야 버퍼링 없이 kubectl logs에서 즉시 확인 가능
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    now = datetime.datetime.now()

    # 로그 포맷: [시간] IP | User-Agent
    print(f"[{now}] Request received from {client_ip} | Agent: {user_agent}", file=sys.stderr)

    return jsonify(products)

# 서버 실행
if __name__ == '__main__':
    # 0.0.0.0으로 설정하면 외부에서 컨테이너로 접근 가능
    app.run(host='0.0.0.0', port=5050)