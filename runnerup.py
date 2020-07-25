if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = [x for x in list(arr) ]


    arr2.sort()

    last = arr2[len(arr2)-1]

    app = arr2.count(last)
   
 


    print(arr2[len(arr2)-app -1] )
    
  

 
