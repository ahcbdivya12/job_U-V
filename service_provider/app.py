from flask import Flask, render_template, request, redirect, session, Response, flash
import mysql.connector

import re
 

app = Flask(__name__)
  
app.secret_key = 'abcdef'

conn_1=mysql.connector.connect(host="localhost",user="root",password="",database="u_v")

cursor_1=conn_1.cursor()

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route("/home")
def index():
    username = session['username']
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
 
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/show')
def show():
    cursor_1.execute("""SELECT `f_name`, `email`, `mobile` FROM `app_name_s_payment` where id = 1 """)
    user=cursor_1.fetchall()

    cursor_1.execute("""SELECT `f_name`, `email`, `mobile` FROM `app_name_s_payment` where id = 2 """)
    user_1=cursor_1.fetchall()

    cursor_1.execute("""SELECT `f_name`, `email`, `mobile` FROM `app_name_s_payment` where id = 6 """)
    user_6=cursor_1.fetchall()
    cursor_1.execute("""SELECT `f_name`, `email`, `mobile` FROM `app_name_s_payment` where id = 7 """)
    user_7=cursor_1.fetchall()
    cursor_1.execute("""SELECT `f_name`, `email`, `mobile` FROM `app_name_s_payment` where id IN ('8','9','10','11','12','13') """)
    user_8=cursor_1.fetchall()
    print(user)
    return render_template("show_details.html",user=user,user_1=user_1,user_6=user_6,user_7=user_7,user_8=user_8)



@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method=='POST':
        que=request.form.get('question')
        op1=request.form.get('opt1')
        op2=request.form.get('opt2')
        op3=request.form.get('opt3')
        op4=request.form.get('opt4')
        answer=request.form.get('ans')
       
        que_1=request.form.get('question_1')
        op1_1=request.form.get('opt1_1')
        op2_1=request.form.get('opt2_1')
        op3_1=request.form.get('opt3_1')
        op4_1=request.form.get('opt4_1')
        answer_1=request.form.get('ans_1')
       
        que_2=request.form.get('question_2')
        op1_2=request.form.get('opt1_2')
        op2_2=request.form.get('opt2_2')
        op3_2=request.form.get('opt3_2')
        op4_2=request.form.get('opt4_2')
        answer_2=request.form.get('ans_2')
       
        que_3=request.form.get('question_3')
        op1_3=request.form.get('opt1_3')
        op2_3=request.form.get('opt2_3')
        op3_3=request.form.get('opt3_3')
        op4_3=request.form.get('opt4_3')
        answer_3=request.form.get('ans_3')
       
        que_4=request.form.get('question_4')
        op1_4=request.form.get('opt1_4')
        op2_4=request.form.get('opt2_4')
        op3_4=request.form.get('opt3_4')
        op4_4=request.form.get('opt4_4')
        answer_4=request.form.get('ans_4')
       
        que_5=request.form.get('question_5')
        op1_5=request.form.get('opt1_5')
        op2_5=request.form.get('opt2_5')
        op3_5=request.form.get('opt3_5')
        op4_5=request.form.get('opt4_5')
        answer_5=request.form.get('ans_5')
       
        que_6=request.form.get('question_6')
        op1_6=request.form.get('opt1_6')
        op2_6=request.form.get('opt2_6')
        op3_6=request.form.get('opt3_6')
        op4_6=request.form.get('opt4_6')
        answer_6=request.form.get('ans_6')
       
        que_7=request.form.get('question_7')
        op1_7=request.form.get('opt1_7')
        op2_7=request.form.get('opt2_7')
        op3_7=request.form.get('opt3_7')
        op4_7=request.form.get('opt4_7')
        answer_7=request.form.get('ans_7')
       
        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que,op1,op2,op3,op4,answer))
        conn_1.commit()

        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_1,op1_1,op2_1,op3_1,op4_1,answer_1))
        conn_1.commit()
        
        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_2,op1_2,op2_2,op3_2,op4_2,answer_2))
        conn_1.commit()

        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_3,op1_3,op2_3,op3_3,op4_3,answer_3))
        conn_1.commit()

        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_4,op1_4,op2_4,op3_4,op4_4,answer_4))
        conn_1.commit()

        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_5,op1_5,op2_5,op3_5,op4_5,answer_5))
        conn_1.commit()

        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_6,op1_6,op2_6,op3_6,op4_6,answer_6))
        conn_1.commit()

        cursor_1.execute("""INSERT INTO `app_name_quiz` (`id`, `question`, `opt1`, `opt2`, `opt3`, `opt4`, `answer`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(que_7,op1_7,op2_7,op3_7,op4_7,answer_7))
        conn_1.commit()
        return redirect('/show')
    else:
        error = "Something not valid chek it!!!!!!" 
        return render_template("add_quiz.html", error=error)

@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method=='POST':
        subject=request.form.get('n_subject')
        dt=request.form.get('n_dt')
        title=request.form.get('title')
        description=request.form.get('n_description')
        cursor_1.execute("""INSERT INTO `app_name_sp_news` (`id`, `subject`, `date_time`, `title`, `sp_new`) VALUES (NULL,'{}','{}','{}','{}')""".format(subject,dt,title,description))
        conn_1.commit()
        return redirect('/home')
    else:
        error = "Something not valid chek it!!!!!!" 
        return render_template("news.html", error=error)
   

@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method=='POST':
        fname=request.form.get('firstname')
        lname=request.form.get('lastname')
        address=request.form.get('address')
        city=request.form.get('city')
        f_zip=request.form.get('zip')
        email=request.form.get('email')
        phone=request.form.get('phone')
        gst=request.form.get('gst')
        cln=request.form.get('cln')
        jobs=request.form.get('jobs')
        category_l=request.form.get('s_language')
        salary=request.form.get('salary')
        subject=request.form.get('subject')
        iso_c=request.form.get('iso_c')
        gmp_c=request.form.get('gmp_c')
        logo=request.form.get('logo')

        regex = "^[0-9]{2}[A-Z]{5}[0-9]{4}" +"[A-Z]{1}[1-9A-Z]{1}" +"Z[0-9A-Z]{1}$"
     
        # Compile the ReGex
        p = re.compile(regex)
        if(re.search(p, gst)):
            cursor_1.execute("""INSERT INTO `app_name_c_job` (`id`, `f_name`, `l_name`, `address`, `city`, `zip_p`, `email`, `phone`, `gst_no`, `cln`, `job`, `language`, `salary`, `subject`, `iso_c`, `gmp_c`, `logo`) VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(fname,lname,address,city,f_zip,email,phone,gst,cln,jobs,category_l,salary,subject,iso_c,gmp_c,logo))
            conn_1.commit()

            return redirect('/quiz')
        else:
            error = "Invalid Gst no. and recheck information" 
            return render_template("add_product.html", error=error)
    return render_template("add_product.html")



@app.route('/reg')
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/login_valid', methods=['GET', 'POST'])
def login_u():
    uname=request.form.get('username')
    pass1=request.form.get('password1')
    cursor_1.execute("""SELECT * FROM `app_name_sp_registration` WHERE `name` = '{}' AND `pass1` = '{}'""".format(uname,pass1))
    users=cursor_1.fetchall()
    if len(users)>0:
        session['username'] = request.form.get('username')
        return redirect('/home')
    else:
        return redirect('/login')
    # return "the email {} and the {}".format(username,pass1)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    uname=request.form.get('username')
    email=request.form.get('email')
    pass1=request.form.get('password1')
    pass2=request.form.get('cpassword')
    address=request.form.get('address')
    mobile=request.form.get('mobile')
    gender=request.form.get('gender')
    state=request.form.get('state')
    cursor_1.execute("""INSERT INTO `app_name_sp_registration` (`id`,`name`, `email`, `pass1`, `pass2`, `address`, `mobile`, `gender`, `state`) VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}')""".format(uname,email,pass1,pass2,address,mobile,gender,state))
    conn_1.commit()
    
    return redirect('/login')
   

if __name__ == '__main__':
	app.run()
