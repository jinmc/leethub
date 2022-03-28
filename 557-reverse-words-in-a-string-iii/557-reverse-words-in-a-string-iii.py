class Solution:
    def reverseWords(self, s: str) -> str:
        wordlist = s.split()
        # print(wordlist)
        new_word_list = []
        for word in wordlist:
            slist = list(word)
            # print(slist)
            start, end = 0, len(slist) - 1
            while start < end:
                temp = slist[start]
                slist[start] = slist[end]
                slist[end] = temp
                start += 1
                end -= 1
            # print(slist)
            new_word = "".join(slist)
            # print(new_word)
            new_word_list.append(new_word)
        return " ".join(new_word_list)
        