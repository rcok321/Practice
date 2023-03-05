def uploadChuck(file_length, file_uploaded):
    file_uploaded.sort(key=lambda x:x[0])
    output = 0
    start = 0
    for u,v in file_uploaded:
        uploadfile_count = u-1-start
        # '{0:b}'.format(uploadfile_count) --> 二進制表示 e.g. 10 --> 1010 表示要分兩次上傳
        output += sum([int(e) for e in '{0:b}'.format(uploadfile_count)])
        start = v
    # edge case
    if start != file_length:
        uploadfile_count = file_length-start-1
        print(uploadfile_count)
        output += sum([int(e) for e in '{0:b}'.format(uploadfile_count)])

    return output

if __name__ == "__main__":
    file_length = 25555555
    file_uploaded = [[9,17],[1,2],[20,253]]
    #(3~8     --> 6 ==> 4+2 ==> 2)
    #(18~19   --> 2 ==> 2   ==> 1)
    #(254~25555555 --> 25555301 ('1100001011111000101100101') ==> 13)
    result = uploadChuck(file_length, file_uploaded)
    print(result) # 16
