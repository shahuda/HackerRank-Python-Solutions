if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_sorted = sorted(set(arr))
    print(unique_sorted[-2])
