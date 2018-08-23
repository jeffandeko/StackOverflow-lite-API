class Question:
    def __init__(self, api):
        self.api = api
        self.questions = [
            {
                "id": 1,
                "title": "What is Python",
                "description": "give your answer in words",
                "answers": [
                    {
                        "id": 1,
                        "answer": "python is a programming language that uses OOP",
                        "user": "Jeffandeko"
                    }
                ]
            }
        ]

    def get_questions(self, question_id):
        for question in self.questions:
            if question['id'] == question_id:
                return question
        self.api.abort(404, "Question {} doesn't exist".format(question_id))

    def create_questions(self, data):
        question = dict()
        question['title'] = str(data.get('title'))
        question['description'] = str(data.get('description'))
        question['answers'] = []

        """ Ensure table id column value is unique """
        try:
            question['id'] = int(self.questions[-1].get('id')) + 1
        except Exception as e:
            question['id'] = 1

        self.questions.append(question)

        return question

    def update_questions(self, id, data):
        question = self.get_questions(id)
        question.update(data)
        return question

    def delete_questions(self, id):
        question = self.get_questions(id)
        self.questions.remove(question)

    def get_stack_answers(self, id):
        question = self.get_stack_answers(id)
        return question['answers']

    def create_stack_answer(self, id, data):
        question = self.get_stack_answers(id)
        question['answers'].append(data)
        return data

    def delete_stack_answer(self, question_id, answer_id):
        question = self.get_stack_answers(question_id)
        answer = list(filter(lambda d: d['id'] in [int(answer_id)], question['answers']))
        """ return a list and get the first element matching query """
        question['answers'].remove(answer[0])

    def get_answers(self, id):
        pass

    def create_answer(self, id, payload):
        pass
