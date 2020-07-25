if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    all_val = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    #print (sum(all_val[6]))
    correct = [i for i in  all_val  if  (sum (i) != n) ]
    
    print(correct)
    

   
