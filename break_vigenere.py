import numpy as np
import matplotlib.pyplot as plt
import numpy as np
def shift_str(str):
    str = ' ' + str[:len(str)-1]
    return str


def clean_str(str):
    str = str.lower()
    str = str.replace(' ', '').replace('\n', '').replace('.', '').replace(';', '').replace(':', '').replace('\'', '').replace(',', '').replace('!', '')

    return str


string = '''kojhmq ir myx iptgovog zazoqh bb bdskn buie.. voum vs ym eqyhazhsiqnbxs zuivsq cp gmsemh prz log:
myx pnvq akqitep hy hfpeqr wb mkpqqddbvoz oxg yhioyvb jrcmao dv rxbsbw qa bdsknqag owzkmes, xcdv ws xe cx wpnt abo owy.
tdivb, i ormwxewk or hrla zasbswcqe fc rddr fuueumq ogh dkig mk yob qf yaib zqse ycugqaa.
zcg ln log'jo hfpahodhl vt aid zqghaid pm gexzsqo log vyz unnk qrdzncfsbv iee ub dkm xek.. hrhv log obh i suoysqo yessxg, iysa ryq'b jafqr afk bqqkxar xjl sv pnrma kql v jggd zianm ich i yof cp a'a vn ooch gbu ggo vbntugdlknl mbkogfie.
ryq'b tef ao zzbns, myx'zr sfwvo iosazewmyy sfodb sod pbhixizu dkm pibvou miez kswp ghq vsqb!
ghq tkfb ghmh irc'ee dskgqag fvsv auoig irce rqgsoqrnos kql gaxsxw.
q gaws wb pnt atp ww logf clz!

aofs: lb bue atp fpnnos dkig yai prcad fvsv jl lgqu rz uahs txag apaswbrd psphig... ttsx... wpnt'e byw bue kojhmq i wbyz, jht u'a cxzr yai nlla't nsmdcfe kce uwpk!'''

string = clean_str(string)

shifted_strs = [string]
coincidences = []

for i in range(1, len(string) - 1):
    shifted_strs.append(shift_str(shifted_strs[i-1]))

for i in range(1, len(shifted_strs)):
    count = 0
    for j in range(len(string)):
        if string[j] == shifted_strs[i][j]:
            count += 1
    coincidences.append(count)
    if len(coincidences) == int(len(string) / 2):
        break
print(coincidences)

x = np.arange(0, len(coincidences))
y = np.array(coincidences)

plt.hist(y, bins=len(y))
plt.xticks(np.arange(0, max(coincidences)))
plt.show()


