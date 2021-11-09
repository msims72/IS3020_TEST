

#here is my first comment
from flask import Flask,render_template,request

grades_dict={}
colors_dict={}
colors_dict['A']='green'
colors_dict['B']='blue'
colors_dict['C']='orange'
colors_dict['D']='purple'
colors_dict['F']='red'

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}..."


@app.route('/color',methods=['GET','POST'])
def show_page():
    if request.method=='GET':
        return render_template('color.html')
    elif request.method=='POST':
        name=request.form['student_name']
        color=request.form['student_color']
        data={'name' : name, 'color' : color}
        return render_template('color.html',data=data)
        


@app.route('/gradetracker',methods=['GET'])
def show_grades():
    return render_template('grades.html')
    
@app.route('/dictionary',methods=['GET'])
def show_dict():
    return str(grades_dict)

@app.route('/calculate',methods=['POST','GET'])
def show_calculation():
    #global grades_dict
    grades=request.form['grades']
    name=request.form['student_name']
    grades=grades.split(';')
    grades=[int(g) for g in grades]
    final_grade=sum(grades) / len(grades)
    if 90 <=final_grade<=100:
        grade='A'
    elif 80 <=final_grade<90:
        grade='B'    
    elif 70 <=final_grade<80:
        grade='C'
    elif 60 <=final_grade<70:
        grade='D'    
    else:
        grade='F'
     
        
    grades_dict.update({name : [final_grade,grade]})
    grades_output='Here are the final grades:<br><br>'
    for key,val in grades_dict.items():
        color_setting=f"'color:{colors_dict[val[1]]}'"
        grades_output+=f'<label style={color_setting}>{key}:{val[0]}</label><br>'
    grades_output+='<a href="/gradetracker">Enter Grades</a>'    
    
    
    return grades_output
    
   
if __name__=='__main__':
    app.debug=True
    app.run(port=8000)