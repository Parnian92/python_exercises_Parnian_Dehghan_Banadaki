#session_07
#1) Text Analysis
def analyze_text(text):
    words=text.split()
    letters=0
    digits=0
    uppercase=0
    lowercase=0
    letter_list=[]
    word_list=[]
    for char in text:
        if char.isalpha():
            letters +=1
            letter_list.append(char.lower())
            if char.isupper():
                uppercase+=1
            if char.islower():
                lowercase+=1

        elif char.isdigit():
            digits+=1
    for word in words:
        word=word.strip('.,!?;:')
        word_list.append(word.lower())
    most_common_letter=''
    max_count=0
    for letter in letter_list:
        count=letter_list.count(letter)
        if count>max_count:
            max_count=count
            most_common_letter=letter
    most_common_word=''
    max_count=0
    for word in word_list:
        count=word_list.count(word)
        if count>max_count:
            max_count=count
            most_common_word=word
    longest_word=word_list[0]
    shortest_word=word_list[0]
    palindrome_words=0
    for word in word_list:
        if len(word)>len(longest_word):
            longest_word=word
        if len(word)<len(shortest_word):
            shortest_word=word
    for word in word_list:
        if len(word)>1 and word==word[::-1]:
            palindrome_words+=1
    result={'words':len(words),'letters':letters,'digits':digits,'most_common_letter':\
            most_common_letter,'most_common_word':most_common_word,'longest_word':\
            longest_word,'shortest_word':shortest_word,'palindrome_words':palindrome_words,\
            'uppercase':uppercase,'lowercase':lowercase}
    return result
text='Hello world python 123 level madam'
print(analyze_text(text))                