import mysql.connector
from flask import Flask, render_template, request, jsonify
from OpenAI import LLMS_Editorial, LLMS_Chat, LLMS_Question


app = Flask(__name__)
problem_description=""

def connectDatabase(user, password, host, database):
    try:
        # Kết nối đến cơ sở dữ liệu
        cnx = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối đến cơ sở dữ liệu: {err}")
        return None

@app.route('/')
def home():
    # Kết nối đến DB
    cnx = connectDatabase('root', '123456', '127.0.0.1', 'HackerThon')
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)

            # Truy vấn danh sách vấn đề
            cursor.execute("SELECT id, name, accepted, submissions FROM Problems")
            problems = cursor.fetchall()
            cursor.close()
            cnx.close()

            # Render template home.html với dữ liệu problems
            return render_template('home.html', problems=problems)
        except mysql.connector.Error as err:
            print(f"Lỗi truy vấn cơ sở dữ liệu: {err}")
            return "Lỗi truy vấn cơ sở dữ liệu"
    else:
        return "Không thể kết nối đến cơ sở dữ liệu"

@app.route('/static/ide-master/problem/<int:id>')
def problem_detail(id):
    # Kết nối đến cơ sở dữ liệu
    cnx = connectDatabase('root', '123456', '127.0.0.1', 'HackerThon')
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)

            # Truy vấn chi tiết vấn đề dựa trên id
            query = "SELECT * FROM Problems WHERE id = %s"
            cursor.execute(query, (id,))
            problem = cursor.fetchone()

            # gáng biến toàn cục dùng cho EDITORIAL
            if problem:
                problem_description = problem['content'] + ""+problem['constraints']

            cursor.close()
            cnx.close()
            # Sử dụng OPENAI cho mỗi Problem ,editorialContent
            response = LLMS_Editorial.get_algorithm_analysis(problem_description)
           
            # Render template problem_detail.html với dữ liệu của vấn đề
            return render_template('/static/ide-master/problem_detail.html', problem=problem, response = response)
        except mysql.connector.Error as err:
            print(f"Lỗi truy vấn cơ sở dữ liệu: {err}")
            return "Lỗi truy vấn cơ sở dữ liệu"
    else:
        return "Không thể kết nối đến cơ sở dữ liệu"

@app.route('/chat')
def chat_page():
    return render_template('chat.html')



@app.route('/about')
def about():
    return render_template('about.html')

chat_history = []
@app.route('/chat', methods=['POST'])
def chat():
   global chat_history
   message = request.json.get('message')
   print(message)
   if not message:
        return jsonify({'error': 'No message received'}), 400

   response = LLMS_Chat.disscus(message,chat_history)

    # Update chat memory with current conversation
   chat_history.append({'message': message, 'response': response})

   return jsonify({'message': response}) 



@app.route('/questions')
def getInterviewQuestions():
    global lastQuestions  # Declare that we are using the global variable
    
    questions  = LLMS_Question.getInterviewQuestionsJS()
    
    return render_template('questions.html', questions=questions['questions'])





if __name__ == '__main__':
    app.run(debug=True)
