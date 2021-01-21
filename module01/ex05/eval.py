class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return -1
        return sum([coeff * len(word) for (coeff, word)
                    in list(zip(coefs, words))])

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return -1


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))

words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))
