stages:
  - test
  - deploy

# 测试阶段（复用前文配置）
python_test:
  stage: test
  image: python:3.9
  before_script:
    - pip install requests pytest
  script:
    - pytest test_httpbin.py -v --junitxml=report.xml
  artifacts:
    reports:
      junit: report.xml

# 部署阶段：将测试脚本复制到容器并验证
deploy:
  stage: deploy
  image: python:3.9
  dependencies:
    - python_test  # 依赖测试阶段成功完成
  script:
    - mkdir -p /app/deploy
    - cp test_httpbin.py /app/deploy
    - cd /app/deploy && python test_httpbin.py  # 部署后验证
    - echo "部署至容器/app/deploy目录完成"
  only:
    - main  # 仅main分支触发部署