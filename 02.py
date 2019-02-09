# -*- coding: utf-8 -*-
#「「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str1 = u'パトカー'
str2 = u'タクシー'
ans = ''
for i in range(4):
    ans = ans + str1[i] + str2[i]
print(ans)
