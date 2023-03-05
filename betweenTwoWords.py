def find_between_string(s, keywords):
    for keyword in keywords:
        keyword_l = 0
        keyword_r = len(keyword)-1
        s_l = 0
        s_r = len(s)-1
        while s_l < s_r:
            print([s_l,s_r,keyword_l,keyword_r])
            if s[s_l] == keyword[keyword_l]: # 左邊比較 keyword 字串
                keyword_l += 1
            if s[s_r] == keyword[keyword_r]: # 右邊比較 keyword 字串
                keyword_r -= 1
            if keyword_l < len(keyword):
                s_l += 1
            if keyword_r >= 0:
                s_r -= 1
            if keyword_l == len(keyword) and keyword_r < 0: # 如果字串比完了就回傳
                return s[(s_l):(s_r)]
    return '-1'

if __name__ == "__main__":
    s = 'axxxxxxxxxxxxxxxxxxxxxxxxxbcdxxacd'
    keywords = ['acd','adc']
    words = find_between_string(s,keywords)
    print(words)
