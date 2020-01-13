if __name__ == "__main__":
    fd = open('dragon', 'r')
    a = fd.read()
    print(a)
    # print('[[\n')
    # for x in a:
    #     if x == "\n":
    #         print('],'+x+'[')
    #     else:
    #         if x == '\'' or x == '\"' or x == '\\':
    #             print('[\''+'\\'+x+'\'],', end='')
    #         else:
    #             print('[\''+x+'\'],', end='')

    # print(']]')
