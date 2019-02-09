# -*- coding: utf-8 -*-
#「「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

STR1 = u'パトカー'
STR2 = u'タクシー'

ans = ''
for i in range(4):
    ans = ans + STR1[i] + STR2[i]
print(ans)
