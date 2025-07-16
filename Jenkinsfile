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
                bat 'pip install requests pytest'  // Windows使用bat命令安装依赖
                echo "依赖安装完成"
            }
        }
        stage('运行自动化测试') {
            steps {
                // 执行测试并生成JUnit报告（Windows路径）
                bat 'pytest test_httpbin.py -v --junitxml=report.xml'
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
                // 1. 创建Windows格式的部署目录
                bat 'mkdir C:\\tmp\\deploy'

                // 2. 复制测试脚本到部署目录
                bat 'copy test_httpbin.py C:\\tmp\\deploy\\'

                // 3. 运行部署后的脚本验证结果
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