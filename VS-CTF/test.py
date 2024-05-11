import gmpy2

from Crypto.Util.number import *
n=129699330328568350681562198986490514508637584957167129897472522138320202321246467459276731970410463464391857177528123417751603910462751346700627325019668100946205876629688057506460903842119543114630198205843883677412125928979399310306206497958051030594098963939139480261500434508726394139839879752553022623977
e = 65537
c = 68714465812771918629458927811590174003154180115197184814126210839884489560759278569238529720825987854108702680916795746513252243755426895848025006594322682794808537450690775213231924943855990325311960951679854496020231445474796285969175089003299321197268394938260938798470905069169271992862192897140599755739
n1 = 129699330328568350681562198986490514508637584957167129897472522138320202321246467459276731970410463464391857177528123417751603910462751346700627325019668067056973833292274532016607871906443481233958300928276492550916101187841666991944275728863657788124666879987399045804435273107746626297122522298113586003834
n2 = 129699330328568350681562198986490514508637584957167129897472522138320202321246467459276731970410463464391857177528123417751603910462751346700627325019668066482326285878341068180156082719320570801770055174426452966817548862938770659420487687194933539128855877517847711670959794869291907075654200433400668220458
ppq=(n-n1+n-n2+4)//3 #p+q
'''n-(p-2)*(q-1)=pq-(pq-p-2q+2)=p+2q-2 ①
n-(p-1)*(q-2)=pq-(pq-2p-q+2)=2p+q-2 ②
①+②：n-(p-2)*(q-1)+n-(p-1)*(q-2)=3*(p+q)-4
p+q=(n-(p-2)*(q-1)+n-(p-1)*(q-2)+4)/3'''
phi=n-ppq+1 #phi=(p-1)*(q-1)=pq-(p+q)+1
d=gmpy2.invert(e,phi)
flag=long_to_bytes((pow(c,d,n)))
print(flag)