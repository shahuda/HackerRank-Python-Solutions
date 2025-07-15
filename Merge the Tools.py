def merge_the_tools(s, k):
    
    for i in range(0, len(s), k):
        chunk = s[i:i+k]
        seen = ''
        
        
        for c in chunk:
            if c not in seen:
                seen += c
                
       
        print(seen)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)