def search(keyword, dataframe, topn=1000):
    all_string = ""
    
    for row in dataframe['content'][:topn]:
        all_string += str(row)
    
    return sub_pat(keyword, all_string)
