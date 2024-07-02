API_KEY="OPEN_API_KEY" # Create an API key to access the OpenAI API. https://platform.openai.com/api-keys
# Define the prompt template
GENERAL_EDITORIAL_TEMPLATE = (
    "Please provide approaches and implement the algorithms based on the template below using HTML characters. Ensure that only the correct approaches are selected when answering the question."
    "<h2>Approach : [Name of Approach] </h2>"
    "<p>One common approach to solve problems of this type is to use a brute force method. This involves checking all possible combinations or iterating through all elements to find a solution.</p>"
    "<h3>Algorithm:</h3>"
    "<ol>"
    "<li>Initialize necessary variables.</li>"
    "<li>Iterate through all elements or combinations.</li>"
    "<li>Apply necessary calculations or checks.</li>"
    "<li>Update variables accordingly.</li>"
    "<li>Return the result.</li>"
    "</ol>"
    "<h3>Complexity Analysis:</h3>"
    "<ul>"
    "<li>Time complexity: &Theta;(f(n)) where f(n) describes the time complexity based on the problem constraints.</li>"
    "<li>Space complexity: &Theta;(g(n)) where g(n) describes the space complexity based on the problem constraints.</li>"
    "</ul>"
    "<br>"
     "Please provide a detailed solution for the following problem: "
)



CHAT_RULES = "Just answer true or false if the following question belongs to the field of computer science. The question is: "
#Data Structures and Algorithms

#MCQ_TEMPLATE = "Please provide a set of 10 random multiple-choice questions about Data Structures and Algorithms along with answers in JSON format.Each question should include the question content, a list of four answer options, and the correct answer. "

MCQ_TEMPLATE ="Please provide a set of 10 random, advanced multiple-choice questions about Data Structures and Algorithm along with answers in JSON format. Each question should include the question content, a list of four answer options, and the correct answer."




