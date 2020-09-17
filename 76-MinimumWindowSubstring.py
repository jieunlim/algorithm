# 76 Minimum Window Substring
import collections
class Solution(object):
    def minWindow(self, s, t):

        if not t or not s:
            return ""

        tCnt = collections.Counter(t)
        need = len(tCnt)
        start, found = 0, 0
        winCnt = collections.defaultdict(int)
        res = float('inf'), None, None

        for end in range(len(s)):

            endChar = s[end]
            winCnt[endChar] += 1
            if tCnt[endChar] == winCnt[endChar]:
                found += 1

            while start <= end and found == need:
                if res[0] > end-start+1:
                    res = (end - start + 1, start, end)

                stChar = s[start]
                winCnt[stChar] -= 1
                if tCnt[stChar] > winCnt[stChar]:
                    found -= 1
                start += 1

        print(f"start={start}, end={end}, res={res}, res[1]={res[1]}, {res[2]}")
        return "" if res[0] == float('inf') else s[res[1]:res[2]+1]

obj = Solution()
s='ABC'
t='AB'
# s = "ADOBECODEBANC"
# t = "ABC"
print(obj.minWindow(s, t))





# cnt = collections.Counter()
# # A Counter is a dict subclass for counting hashable objects
# for w in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[w] += 1
# print(cnt)
#
# print("==========")

def minWindow11(s, t):
    m = len(s)
    n = len(t)
    if m < n:
        return ''

    lt = {}
    for i in t:
        if i not in lt:
            lt[i] = 1
        else:
            lt[i] += 1
    missing = n
    i = I = J = 0
    print(f"s={s}, t={t}, lt={lt}, missing={missing}")

    for j, c in enumerate(s, 1):
        print(f"j={j}, c={c}")
        if c in lt and lt[c] > 0:
            missing -= 1
        if c in lt:
            lt[c] -= 1
        print(f"missing={missing}, lt={lt}")
        while i < j and not missing:
            print(f"  i={i}, j={j}, I={I}, J={J}")
            if not J or j - i < J - I:
                I, J = i, j
                print(f"    I={I}, J={J}")

            if s[i] not in lt:
                i += 1
                print(f"    i={i}")
                continue
            else:
                lt[s[i]] += 1
                if lt[s[i]] > 0:
                    missing += 1
                i += 1
                print(f"    i={i}, lt={lt}, missing={missing}")
    return s[I:J]

def minWindow(s, t):
    need = collections.Counter(t)            #hash table to store char frequency
    missing = len(t)                         #total number of chars we care
    start, end = 0, 0
    i = 0
    print(f"s={s}, t={t}, need={need}, missing={missing}")
    for j, char in enumerate(s, 1):          #index j from 1
        print(f"j={j}, char={char}")
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        print(f"  missing={missing}, {need}")
        if missing == 0:                     #match all chars
            while i < j and need[s[i]] < 0:  #remove chars to find the real start
                need[s[i]] += 1
                i += 1
                print(f"   i={i}, j={j}, need={need}")

            need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
            missing += 1                     #we missed this first char, so add missing by 1
            print(f"    need={need}, missing={missing}")
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                           #update i to start+1 for next window
            print(f"  i={i}, missing={missing}, need={need}, start={start}, end={end}")
    print(f"start={start}, end={end}")
    return s[start:end]

S = "ADOBECODEBANC"
# S="ABCDOODEBANC"
S = "ABAACBAB"
# S="obzcopzocynyrsgsarijyxnkpnukkrvzuwdjldxndmnvevpgmxrmvfwkutwekrffnloyqnntbdohyfqndhzyoykiripdzwiojyoznbtogjyfpouuxvumtewmmnqnkadvzrvouqfbbdiqremqzgevkbhyoznacqwbhtrcjwfkzpdstpjswnpiqxjhywjanhdwavajrhwtwzlrqwmombxcaijzevbtcfsdcuovckoalcseaesmhrrizcjgxkbartdtotpsefsrjmvksqyahpijsrppdqpvmuocofuunonybjivbjviyftsyiicbzxnwnrmvlgkzticetyfcvqcbjvbufdxgcmesdqnowzpshuwcseenwjqhgsdlxatamysrohfnixfprdsljyyfhrnnjsagtuihuczilgvtfcjwgdhpbixlzmakebszxbhrdibpoxiwztshwczamwnninzmqrmpsviydkptjzpktksrortapgpxwojofxeasoyvyprjoguhqobehugwdvtzlenrcttuitsiijswpogicjolfxhiscjggzzissfcnxnvgftxvbfzkukqrtalvktdjsodmtgzqtuyaqvvrbuexgwqzwduixzrpnvegddyyywaquxjxrnuzlmyipuqotkghfkpknqinoidifnfyczzonxydtqroazxhjnrxfbmtlqcsfhshjrxwqvblovaouxwempdrrplefnxmwrwfjtebrfnfanvvmtbzjesctdgbsfnpxlwihalyiafincfcwgdfkvhebphtxukwgjgplrntsuchyjjuqozakiglangxkttsczhnswjksnuqwflmumpexxrznzwxurrysaokwxxqkrggytvsgkyfjrewrcvntomnoazmzycjrjrqemimyhriyxgrzcfuqtjhvjtuhwfzhwpljzajitrhryaqchnuawbxhxrpvyqcvhpggrpplhychyulijhkglinibedauhvdydkqszdbzfkzbvhldstocgydnbfjkcnkfxcyyfbzmmyojgzmasccaahpdnzproaxnexnkamwmkmwslksfpwirexxtymkmojztgmfhydvlqtddewjvsrmyqjrpycbmndhupmdqqabiuelacuvxnhxgtpvrtwfgzpcrbhhtikbcqpctlxszgpfbgcsbaaiapmtsucocmpecgixshrrnhyrpalralbccnxvjzjllarqhznzghswqsnfuyywmzbopyjyauknxddgdthlabjqtwxpxwljvoxkpjjpfvccyikbbrpdsyvlxscuoofkecwtnfkvcnzbxkeabtdusyhrqklhaqreupakxkfzxgawqfwsaboszvlshwzhosojjotgyagygguzntrouhiweuomqptfjjqsxlbylhwtpssdlltgubczxslqjgxuqnmpynnlwjgmebrpokxjnbiltvbebyytnnjlcwyzignmhedwqbfdepqakrelrdfesqrumptwwgifmmbepiktxavhuavlfaqxqhreznbvvlakzeoomykkzftthoemqwliednfsqcnbexbimrvkdhllcesrlhhjsspvfupxwdybablotibypmjutclgjurbmhztboqatrdwsomnxnmocvixxvfiqwmednahdqhxjkvcyhpxxdmzzuyyqdjibvmfkmonfxmohhshpkhmntnoplphqyprveyfsmsxjfosmicdsjrieeytpnbhlsziwxnpmgoxneqbnufhfwrjbqcsdfarybzwaplmxckkgclvwqdbpumsmqkswmjwnkuqbicykoisqwoootrdpdvcuiuswfqmrkctsgrevcxnyncmivsxbpbxzxpwchiwtkroqisnmrbmefbmatmdknaklpgpyqlsccgunaibsloyqpnsibwuowebomrmcegejozypjzjunjmeygozcjqbnrpakdermjcckartbcppmbtkhkmmtcngteigjnxxyzaibtdcwutkvpwezisskfaeljmxyjwykwglqlnofhycwuivdbnpintuyhtyqpwaoelgpbuwiuyeqhbvkqlsfgmeoheexbhnhutxvnvfjwlzfmvpcghiowocdsjcvqrdmkcizxnivbianfpsnzabxqecinhgfyjrjlbikrrgsbgfgyxtzzwwpayapfgueroncpxogouyrdgzdfucfrywtywjeefkvtzxlwmrniselyeodysirqflpduvibfdvedgcrzpzrunpadvawfsmmddqzaaahfxlifobffbyzqqbtlcpquedzjvykvarayfldvmkapjcfzfbmhscdwhciecsbdledspgpdtsteuafzbrjuvmsfrajtulwirzagiqjdiehefmfifocadxfuxrpsemavncdxuoaetjkavqicgndjkkfhbvbhjdcygfwcwyhpirrfjziqonbyxhibelinpllxsjzoiifscwzlyjdmwhnuovvugfhvquuleuzmehggdfubpzolgbhwyeqekzccuypaspozwuhbzbdqdtejuniuuyagackubauvriwneeqfhtwkocuipcelcfrcjcymcuktegiikyosumeioatfcxrheklookaqekljtvtdwhxsteajevpjviqzudnjnqbucnfvkybggaybebljwcstmktgnipdyrxbgewqczzkaxmeazpzbjsntltjwlmuclxirwytvxgvxscztryubtjweehapvxrguzzsatozzjytnamfyiitreyxmanhzeqwgpoikcjlokebksgkaqetverjegqgkicsyqcktmwjwakivtsxjwrgakphqincqrxqhzbcnxljzwturmsaklhnvyungjrxaonjqomdnxpnvihmwzphkyuhwqwdboabepmwgyatyrgtboiypxfavbjtrgwswyvcqhzwibpisydtmltbkydhznbsvxktyfxopwkxzbftzknnwipghuoijrbgqnzovxckvojvsqqraffwowfvqvfcmiicwitrhxdeombgesxexedlakitfovtydxunqnwqqdeeekiwjnwoshqcsljiicgobbbuqakjdonjawgjlezdnqhfdqnmsuavxdpnfzwipmspiabveaarshzwxmirgkmfncvtdrdvfxkpxlkdokxgtwcskmjryyymcthfnkasinihaunohkxaibtsqelockaefjmsuolebtnepauwmrxutspjwaxbmahsjtkfkxlnszribmeofbkyvbjscjtqjakuwvcgunvnonvqbbggfshauqsyznokqbhowjusypfnecffenojfvlblgzntqzlrgzprvhqnpfrrkzxznieiuivajivzijsqijigtatifmbplzqahuidegfoobpymkputzamzvweiyvvzlwihgmmmrcburbgbsdxrfjsbiylitghgcpqjbevvgypxcybubyoijijrhuzcdijfybqbfowlookqmlnplbxvjjosfqviygqyhgamuwzjklbyzopkrnhbywtfoqomweldmlrhjqswctubiknzzvcztyehouvnyiqnvkufaobehxhrjvtisxjlxoumipzjarwvbsaegdkpbsjmpevjbewzuqnfhoohhmdjgfpmjzdmtmykqvtucptwfidpwtwffzolffzqfdearclkyeecuzabjeqhxpmfodsvisnpxrqowdawheydfyhoexvcmihdlzavtqlshdhdgjzpozvvackebhgqppvcrvymljfvooauxcjnbejdivikcoaugxwzsulgfqdtefpehbrlhaoqxwcancuvbqutnfbuygoemditeagmcveatgaikwflozgdhkyfqmjcruyyuemwbqwxyyfiwnvlmbovlmccaoguieu"

T = "ABC"

# print(minWindow(S,T))
