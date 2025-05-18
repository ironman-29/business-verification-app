from flask import Flask, render_template, request, jsonify
import requests
import json
from typing import Dict, List, Optional

class BusinessVerificationAPI:
    def __init__(self, service_key: str):
        self.service_key = service_key
        self.base_url = "https://api.odcloud.kr/api/nts-businessman/v1"
        
    def verify_business(self, 
                       business_number: str,
                       start_date: str,
                       representative_name: str,
                       representative_name2: Optional[str] = None,
                       business_name: Optional[str] = None,
                       corporation_number: Optional[str] = None,
                       business_sector: Optional[str] = None,
                       business_type: Optional[str] = None,
                       business_address: Optional[str] = None) -> Dict:
        url = f"{self.base_url}/validate?serviceKey={self.service_key}"
        
        business_info = {
            "b_no": business_number,
            "start_dt": start_date,
            "p_nm": representative_name
        }
        
        if representative_name2:
            business_info["p_nm2"] = representative_name2
        if business_name:
            business_info["b_nm"] = business_name
        if corporation_number:
            business_info["corp_no"] = corporation_number
        if business_sector:
            business_info["b_sector"] = business_sector
        if business_type:
            business_info["b_type"] = business_type
        if business_address:
            business_info["b_adr"] = business_address
            
        data = {
            "businesses": [business_info]
        }
        
        try:
            response = requests.post(
                url,
                data=json.dumps(data),
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {str(e)}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"응답 내용: {e.response.text}")
            return {"error": str(e)}

    def check_status(self, business_numbers: list) -> dict:
        url = f"{self.base_url}/status?serviceKey={self.service_key}"
        data = {
            "b_no": business_numbers
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(data),
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {str(e)}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"응답 내용: {e.response.text}")
            return {"error": str(e)}

# Flask 앱 설정
app = Flask(__name__)

# 환경 변수에서 API 키를 가져오도록 수정
import os
SERVICE_KEY = os.environ.get('SERVICE_KEY', '')
api = BusinessVerificationAPI(SERVICE_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    data = request.form
    
    # 필수 입력 데이터 확인
    if not all([data.get('business_number'), data.get('start_date'), data.get('representative_name')]):
        return jsonify({"error": "사업자등록번호, 개업일자, 대표자명은 필수 입력 항목입니다."})
    
    # API 호출
    result = api.verify_business(
        business_number=data.get('business_number'),
        start_date=data.get('start_date'),
        representative_name=data.get('representative_name'),
        representative_name2=data.get('representative_name2'),
        business_name=data.get('business_name'),
        corporation_number=data.get('corporation_number'),
        business_sector=data.get('business_sector'),
        business_type=data.get('business_type'),
        business_address=data.get('business_address')
    )
    
    return jsonify(result)

@app.route('/status', methods=['POST'])
def status():
    data = request.form
    business_numbers = data.get('business_numbers', '').split(',')
    business_numbers = [num.strip() for num in business_numbers if num.strip()]
    
    if not business_numbers:
        return jsonify({"error": "사업자등록번호를 입력해주세요."})
    
    if len(business_numbers) > 100:
        return jsonify({"error": "한 번에 최대 100개의 사업자등록번호만 조회할 수 있습니다."})
    
    result = api.check_status(business_numbers)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
