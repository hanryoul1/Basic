# 신조어 퀴즈 클래스

class Word():
    def __init__(self, new_word, ex1, ex2, answer):
        self.new_word = new_word
        self.a1 = ex1
        self.a2 = ex2
        self.answer = answer
    
    def show_question(self):
        print(f"\"{self.new_word}\"의 뜻은?")
        print(f"{self.a1}")
        print(f"{self.a2}")
    
    def check_answer(self, user_input):
        if user_input == self.answer:
            print("정답입니다.\n")
        else:
            print("틀렸습니다.\n")

word1 = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word1.show_question()
word1.check_answer(int(input("=> ")))

word2 = Word("애빼시", "애교 빼면 시체", "애들은 빼빼로 시시해", 1)
word2.show_question()
word2.check_answer(int(input("=> ")))

word3 = Word("혼코노", "혼자서는 코딩 노노", "혼자 코인 노래방", 2)
word3.show_question()
word3.check_answer(int(input("=> ")))