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
                bat 'pip install requests pytest'  // Windows环境使用bat命令
                echo "依赖安装完成"
            }
        }
        stage('运行自动化测试') {
            steps {
                bat 'pytest test_httpbin.py -v --junitxml=report.xml'  // Windows使用bat执行pytest
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
                // Windows环境：创建部署目录并复制测试脚本
                bat 'mkdir /tmp/deploy'
                bat 'copy test_httpbin.py C:\\tmp\\deploy'

                // 部署后验证：运行部署目录中的脚本
                bat 'python C:\\tmp\\deploy\\test_httpbin.py'
                echo "部署至C:\\tmp\\deploy完成，验证通过"
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