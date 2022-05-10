```
@app.route('/')
def main():
    myname = "sparta"
    return render_template("index.html", name=myname)
    
    
    # 서버 파일에 위처럼 쓰면 sparta를 
    
    
    
    

<h3>Hello, {{ name }}!</h3>

# {{ }} 는 Jinja2 템플릿의 적용 규칙 문법이다.
# html 으로 전달해서 h3 name 에 전달된다.
