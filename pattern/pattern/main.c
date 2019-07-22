//
//  main.c
//  pattern
//
//  Created by Mir Hamed Ali on 15/02/19.
//  Copyright © 2019 Mir Hamed Ali. All rights reserved.
//
/*
 def printer():
 global c, n, x
 
 print(n, end=" ")
 if c > 0 and n == x:
 print(n)
 return 1
 elif n > 0:
 n = n-5
 return printer()
 else:
 n = n+5
 return printer()
 */

#include <stdio.h>
int x;
int printer(int n,int c){
    printf("%d",n);
    if (c>0 && x==n){
        return 1;
    }
    c=c+1;
    if (n<=0){
        return printer(n+5, c);
    }
    else if(n>0){
    return printer(n-5,c);
    }
    return 1;
}
int main(int argc, const char * argv[]) {
    // insert code here...
    int n=10,v,c=0;
    x=n;
    v=printer(n,c);
    
}
