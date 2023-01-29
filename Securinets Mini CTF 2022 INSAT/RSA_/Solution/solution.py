from Crypto.Util.number import *

N=161045428586645637683450674429135634581430303516004618849687159354116469395458984953479060311843223287811426501369034042231592747925519789946665078087389745539677527760685120877832142090742006252398002546098691598757470869551662844404847753838966143841012167327024740382773439818680823627246838703971062727819
hint=91844762128166135406581908639773167956928165907030894379830797238119495659794223136909466210714872212362723075625183357915188377756452205882575184405757670332894795185885774205919876724467471896459840559277528661861522258154580322787573539827024865359619144177327987072257075412881730691006615890555271878511
c=52051776800583514059370043120878133315037799922805506892695435950334363051051930662210582806782648478915979298955650172355199056632533514445825907662806065800315933703846173303223521788548745519218735965327291361820339660651595274377069061332604094247105193992593124657308222337864744408749139957598758490788
e = 65537

p = GCD((hint+1),N)
q = N//p
phi = (p - 1)*(q - 1)
d = inverse(e, phi)
m = pow(c, d, N)
print (long_to_bytes(m).decode())

#Securinets{wils0n'S_7HeOr3M_S4v3_you_7hs_tiMe}