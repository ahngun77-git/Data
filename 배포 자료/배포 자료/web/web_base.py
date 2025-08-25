from flask import Flask, request, redirect, render_template, url_for, flash
import os

app = Flask(__name__)
# Session 관리를 위한 비밀 키 설정
# 실제 배포 시에는 안전한 비밀 키를 사용해야 합니다.
app.secret_key = 'secret_key'

# 현재 파일이 실행 중인 directory를를 기준으로 'upload' 폴더 경로 설정
# web 서버에서 파일을 업로드할 때, 업로드된 파일을 저장할 폴더를 지정합니다.
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../file/upload')
# 'upload' 폴더가 없으면 생성
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')  # HTML 파일 경로를 Flask 기본 경로에 맞게 설정

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('파일을 선택하세요')
        return redirect(url_for('upload_form'))
    file = request.files['file']
    username = request.form['username']
    password = request.form['password']

    print(f"File:{file.filename}\nUsername:{username}\nPassword:{password}")

    if file.filename == '':
        flash('파일이 존재하지 않습니다.')
        return redirect(url_for('upload_form'))
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        flash(f"File '{file.filename}' 성공적으로 업로드 되었습니다!")
        return redirect(url_for('upload_form'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

