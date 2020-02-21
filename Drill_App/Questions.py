class Questions:
    def __init__(self):
        self.questions = []
        self.a_answers = []
        self.b_answers = []
        self.c_answers = []
        self.d_answers = []
        self.correct_answers = []
        self.path = None

    def open_file_questions(self, path):
        f = open(path)
        txt_file = []

        self.questions.clear()
        self.a_answers.clear()
        self.b_answers.clear()
        self.c_answers.clear()
        self.d_answers.clear()
        self.c_answers.clear()

        for i in f:
            txt_file.append(i)

        for i in range(0, len(txt_file)):
            if txt_file[i].startswith(">>>"):
                self.correct_answers.append(txt_file[i][3:4])
        #  questions list, self.questions = []
        for i in range(0, len(txt_file), 6):
            self.questions.append(txt_file[i])
        #  a_answers list, self.a_answers = []
        for i in range(1, len(txt_file), 6):
            self.a_answers.append(txt_file[i])
        #  b_answers list, self.b_answers = []
        for i in range(2, len(txt_file), 6):
            self.b_answers.append(txt_file[i])
        #  c_answers list, self.c_answers = []
        for i in range(3, len(txt_file), 6):
            self.c_answers.append(txt_file[i])
        #  d_answers list, self.d_answers = []
        for i in range(4, len(txt_file), 6):
            self.d_answers.append(txt_file[i])


