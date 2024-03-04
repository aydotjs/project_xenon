Translation_Dic = {
    "please": "abeg", "know": "sabi",
    "hastiness": "gragra", "charm": "juju", "mother": "mama",
    "child": "pikin", "you": "una", "walk": "waka",
    "rubish": "yamayama", "our": "awa", "people": "pipul",
    "come": "kom", "said": "tok", "that": "wey", "what": "wetin",
    "old": "old", "man": "man", "is": "de", "see": "si", "for": "fo",
    "where": "wie", "he": "im", "sit": "sidon", "small": "smol",
    "child": "pikin", "cannot": "no-fit", "it": "am", "even": "ivun"
    , "when": "wen", "he": "im", "climb": "klaimb", "tree": "tri",
    "the": "Di", "three": "tiri", "elder": "sinio", "child": "pikin",
    "magician": "majishan", "and": "an", "they": "dem", "their": "dia",
    "small": "smol", "brother": "broda", "not": "neva", "mature": "big",
    "enough": "rich", "to": "to", "learn": "len", "any": "eni", "work": "wok",
    "one": "Wan", "day": "dé", "the": "di", "hunter": "honta", "entered": "enta",
    "bush": "bush", "go": "go", "hunt": "hont", "animal": "anima"}


def English_Pidgin_Dic(English_Sentence):
    words = English_Sentence.lower().split()


    """
    pidgin_sentence = []   

    for word in words:
        if word in Translation_Dic:
            pidgin_word = Translation_Dic[word]
        else:
            pidgin_word = word  
        pidgin_sentence.append(pidgin_word)

    pidgin_sentence = " ".join(pidgin_sentence)
    return pidgin_sentence
    """
    #[Translation_Dic.get(word, word) for word in words]
    #"""
    pidgin_sentence = list(map(lambda word: Translation_Dic.get(word, word), words))
    pidgin_sentence = " ".join(pidgin_sentence)
    #movements_in_dollars = [50, 60, 70]
    #movements_in_naira = [item*1600 for item in movements_in_dollars]
    #print(movements_in_naira)
    movements_in_dollars = [50, 60, 70]
    #squared_list = list(map(lambda x: x**2, original_list))
    movement_in_naira = list(map(lambda movement: movement * 1600, movements_in_dollars))
    print(movement_in_naira)
    return pidgin_sentence
    #"""

English_Sentence = ("Your brother cannot climb the tree that you climbed")
print(English_Pidgin_Dic(English_Sentence))