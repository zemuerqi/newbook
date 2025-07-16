import pytest
import requests

def test_httpbin_get():
    # 调用公共接口
    response = requests.get("https://httpbin.org/get")
    # 断言响应状态码为200
    assert response.status_code == 200
    # 断言响应包含"origin"字段（接口返回客户端IP）
    assert "origin" in response.json()

if __name__ == "__main__":
    # 生成JUnit格式报告（方便Jenkins识别）
    pytest.main(["-v", "test_httpbin.py", "--junitxml=report.xml"])