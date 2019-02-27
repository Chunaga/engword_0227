import re
import random


source = 'english_word_01.txt'
n_tests = 50
n_questions = 50

def create_words_dict(source):
    with open(source) as f:
        data = f.read()

    english_word = re.findall('^[a-z]', data)
    ja = re.findall('\s.*\t', data)

    meanings = []
    for word in ja:
        m = re.sub('\t|\n','', data)
        meanings = m.append(i)

    words_dict = dict(zip(english_words, meanings))

    return english_words, meanings, word_dict


    english_words, meanings, words_dict = create_words_dict(source)

    for test_num in range(n_test):
        with open('第{02d:}回 英単語テスト.txt'.format(test_num + 1, 'w')) as f:
            f.write('出席番号: \n'
                    '名前: \n'
                    '第{}回英単語テスト'.format(test_num + 1))

            question_word = random.sample(english_words, n_questions)

            for question_num in range(n_questions):
                question_word = question_words[question_num]
                correct_answer =words_dict[question_word]

                meanings_copy = meanings.copy()
                meanings_copy.remove(correct_answer)
                wrong_answers = random.sample(meanings_copy, 3)
                answer_options = [correct_answer] + wrong_answers
                random.shuffle(answer_options)

                f.write('問{}.{}\n\n'.format(question_num + 1 ,question_word))
                        
                for i in range(4):
                        f.write('{}.{}\n'.format(i +1, answer_options[i]))
                f.write('\n\n')


            
                

        
