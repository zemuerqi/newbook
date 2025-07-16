pipeline {
    agent any
    stages {
        stage('拉取代码') {
            steps {
                git url: 'https://github.com/zemuerqi/newbook.git', branch: 'main'
                echo "代码拉取完成，当前目录：${workspace}"
            }
        }
        stage('安装依赖') {
            steps {
                sh 'pip install requests pytest'  // Linux环境，Windows替换为bat命令
                echo "依赖安装完成"
            }
        }
        stage('运行自动化测试') {
            steps {
                sh 'pytest test_httpbin.py -v --junitxml=report.xml'
                echo "测试完成，生成报告：report.xml"
            }
            post {
                always {
                    junit 'report.xml'  // 收集测试报告
                }
            }
        }
        stage('部署与验证') {
            steps {
                // 模拟部署：复制测试脚本到本地部署目录
                sh 'mkdir -p /tmp/deploy && cp test_httpbin.py /tmp/deploy'
                // 部署后验证：运行部署目录中的脚本
                sh 'python /tmp/deploy/test_httpbin.py'
                echo "部署至/tmp/deploy完成，验证通过"
            }
        }
    }
    post {
        success {
            echo "流水线运行成功！"
        }
        failure {
            echo "流水线运行失败，请查看日志"
        }
    }
}