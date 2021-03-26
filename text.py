# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:22:21 2021

@author: proled
"""

def revword (word):
    num=len(word)-1
    n_word=' '
    i=0
    while(i<=num):
        n_word=n_word+word[num-i]
        i=i+1
    return n_word.lower().lstrip()

def countword():
    xfile= open('text.txt')
    total=xfile.read()
    word=total.split()[0]
    line=total.split('\n')
    count=1
    n_f=word+'\n'
    for sen in line:
        if sen==word:
                continue
        w=sen.split(' ')
        for i in w:
            i=revword (i)
            n_f=n_f+i+' '
            if i==word:
                count=count+1
        n_f=n_f+'\n'
    return count


