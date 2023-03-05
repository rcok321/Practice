def find_between_string(s, keywords):
    for keyword in keywords:
        keyword_l = 0
        keyword_r = len(keyword)-1
        s_l = 0
        s_r = len(s)-1
        start = 0
        end = 0
        while s_l < s_r:
        # for _ in range(4):
            print([s_l,s_r,keyword_l,keyword_r])
            if s[s_l] == keyword[keyword_l]:
                keyword_l += 1
            if s[s_r] == keyword[keyword_r]:
                keyword_r -= 1
            if keyword_l < len(keyword):
                s_l += 1
            if keyword_r >= 0:
                s_r -= 1
            if keyword_l == len(keyword) and keyword_r < 0:
                return s[(s_l):(s_r)]
    return ''

if __name__ == "__main__":
    s = 'axxxxxxxxxxxxxxxxxxxxxxxxxbcdxxacd'
    keywords = ['acd','adc']
    words = find_between_string(s,keywords)
    print(words)
