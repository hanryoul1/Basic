def cutline(lst, k):
    return sorted(lst, reverse = True)[k-1]

if __name__ == "__main__":
    N, k = map(int, input().split()) # 5 2
    score_list = list(map(int, input().split())) # 100 76 85 93 98
    
    print(cutline(lst = score_list, k = k))