from Classes.Solution import Solution


class Question:
    def __init__(self, code_q=None, subject=None, sub_subject=None, level=None, type_test=None, year=None, semester=None,
                 term_test=None, format_q=None, is_solution=False, format_s=None, type_s=None):
        """
        init question
        param sub: the subject of the question
        param sub_theme: the sub_theme of the question
        param level: the level of the question
        param type_test: the type of the test that the question was taken from
        param year: the year of the test that the question was taken from
        param semester: the semester of the test that the question was taken from
        param term_test: the term of the test that the question was taken from
        param formatQ: the format of the question file
        param type_s: full solution or part solution
        param formatS: the format of the solution file
        param codeQ: the code of the question
        """
        self.is_solution = False
        self.solution = None
        if is_solution:
            self.is_solution = True
            self.solution = Solution(code_q, format_s, type_s)
        self.subject = subject
        self.sub_subject = sub_subject
        self.level = level
        self.type_test = type_test
        self.year = year
        self.semester = semester
        self.term_test = term_test
        self.format_q = format_q
        self.code_q = code_q
