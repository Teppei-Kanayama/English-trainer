import numpy as np
import math

class Questioner():

    def __init__(self, source_file):
        self.sample_sentence = "I'd like to go to America."

    def print_question(self, drop_rate=0.7):
        self.question = "I'd like to go to America."
        question_splited = self.question.split(" ")
        question_len = len(question_splited)
        drop_num = int(question_len * drop_rate)

        flags = np.concatenate((np.zeros(drop_num, dtype=np.uint8), np.ones(question_len - drop_num, np.uint8)))
        np.random.shuffle(flags)

        for flag, word_pos in zip(flags, range(question_len)):
            if flag == 0:
                question_splited[word_pos] = "_"

        print(" ".join(question_splited))

    def check_answer(self, your_answer: str):
        if your_answer == self.question:
            print("collect")
        else:
            print("incollect")

def main():
    questioner = Questioner("hoge")

    while True:
        questioner.print_question()
        text = input("Your Answer > ")
        questioner.check_answer(text)
        break

if __name__ == "__main__":
    main()