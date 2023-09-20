
########################################################
# Quiz class                                           #
########################################################
class Quiz:
    quiz_name = ""
    max_score = 0
    current_score = 0

    def __init__(self, q_name, q_max, q_score):
        self.quiz_name = q_name
        self.max_score = q_max
        self.current_score = q_score
########################################################
#                                                      #
########################################################


########################################################
# Subject class                                        #
########################################################
class Subject:
    subject_name = ""
    quizzes = []
    exams = {}

    def __init__(self, sub_name):
        self.subject_name = sub_name

    """
    ****************************
    Quizzes manipulation section
    ****************************
    """

    def add_quiz(self, q_name, q_max, q_score):
        temp_quiz = Quiz(q_name, q_max, q_score)
        self.quizzes.append(temp_quiz)

    def initialize_quizzes_list(self):
        quiz_amount = int(input("How many quizzes are you going to record?: "))

        while quiz_amount > 0:
            q_name = input("Enter quiz name: ")
            q_max = int(input("Enter quiz max score: "))
            q_score = int(input("Enter your quiz score: "))
            self.add_quiz(q_name, q_max, q_score)

            quiz_amount -= 1

    def q_max_score_sum(self):
        total_sum = 0
        for i in self.quizzes:
            total_sum += i.max_score

        return total_sum

    def q_weighted_cfrs(self, weight_p):
        return self.q_max_score_sum() * weight_p

    """
    ****************************
    Exams manipulation section
    ****************************
    """

    def


########################################################
#                                                      #
########################################################






# subject_object = Subject("Sex")
# subject_object.initialize_quizzes_list()
# print(subject_object.q_max_score_sum())


















