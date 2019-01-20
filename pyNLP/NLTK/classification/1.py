from nltk.corpus import names
import random


class One:
    def __init__(self):
        pass

    def main(self):
        labeled_names = self.getLabeledNames()
        pass

    def getLabeledNames(self):
        labeled_names = []
        for name in names.words('male.txt'):
            labeled_names.append((name, 'male'))
        for name in names.words('female.txt'):
            labeled_names.append((name, 'female'))
        return random.shuffle(labeled_names)
        pass


if __name__ == "__main__":
    one = One()
    one.main()
