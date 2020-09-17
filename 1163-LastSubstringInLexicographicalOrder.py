# 1163. Last Substring in Lexicographical Order

class Solution:
    def lastSubstring(self, s):
        result = ""
        for i in range(len(s)):
            result = max(result, s[i:])
            print(f"i={i}, result={result}, s[i:]={s[i:]}")
        return result

    # https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/Short-python-code-O(n)-time-and-O(1)-space-with-proof-and-visualization
    # i: the starting index of the first substring
    # j: the starting index of the second substring
    # k: if i and j are same, move to compare i+k and j+k
    def lastSubstring2(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            print(f"i={i}, j={j}, k={k}, n={n}, s={s}")
            if s[i + k] == s[j + k]:
                k += 1
                print(f"  s[i+k] {s[i + k]} == s[j+k] {s[j + k]}, k={k} continue")
                # continue
            elif s[i + k] > s[j + k]:
                print(f"  s[i+k] {s[i + k]} > s[j+k] {s[j + k]}")
                j = j + k + 1
                k = 0
                print(f"    , j={j}")
            else:
                # if i + k + 1 > j : print(f"AAAAAAAAAA")   #test printing
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
                print(f"  i={i}, j={j}")

        print(f"s={s}, i={i}")
        return s[i:]

s = "abab"
s = "leetcode"
s = "ababaa"
s = "dafazxd"
s = "xbylisvborylklftl"
s = "addddfgggggxaa"  # test for "i = max(i + k + 1, j)" line
# s="xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji"
# s="pgtrdjdpscrwjifnrcttyruighgygsuvlhxpckkeahrupvnhlnpulyogsbktcuxnmnbmgadksxdjunqvmzyujynwzevtstjvzkddxjjmbgxfueteeuktvcbvypbdnzostbwxmxdwomguuymexfrrwuvuglgwmmwpkrqrpuzvjujksdwopsqlsrfgyzhymfgejuwhyvoqoxluvsdnmkglypoozrcgnzchpurezauixujddjjawqiaasvhrhfbhsqutgskudpcbqkkrcagrtalnsecxmlbiysgabvjbwpfufiwqdsnwbutashtejpmcypfztbgzuxwfcpkwdzhvfxbtvdvdaufjpqgfgxufhsopvwmgekcjejdlgxtdghmyzvopqkdzpuudyunnafvaeyshluuujkqncyigweelxmvgiaegonqmouaxwaqxhnnvaeuppsritdsymdwonbooswiolhbacpnehyvbhekxqxuvpnaxrfgeyixmurlgszqrotqynvtlbpjhhwdkbneiutmwutiyqegkxsrgldqvziysvihgbplhiumonlzlfzbuavbygmltdnfwjbspfpmzkfryjjpswihwixmbeodfpnmytccdvjnctzkxuqrvgjehodfdhpconhfpnatzzxyqkzjttgnwvxcfwyhlajvuhjonbpkvbbahlbybvvnhrwnnpnagtnnqcewzdzsxjgfoqbipohzsgpmyhqgvvnffjumirbhpbfletvcglthgwdvkgczucreovnfpbugyzuugqodpgsylfwyjucfnxjbghurnrkkuwsjfxeoxyzvltwhzyuechbfwstfovqgxngcwsmqsbzasrfrdvjcgedacvviihnzlijbaotpkvzmfejtfsnljthmzfhsrtieqlfhuatdwhcvsoxyphqsoxaqiqjcbuldswtjsukvcoowyfgmixswlyvkllvdtnerfisymrwgtfleupfxxswdlhvioeilstdlqfckoxpohcgnfannhbeeyzthhmszdphsbhjhxbwmjcknyrcsxgxcgnrvqnrlpqqwilhradmbowdvpusmombllpjikbuokakqzovmtmanaavururxjjxvrdnwabfwchkscmmmyixmjtogqgowbqlymnjcalxkmolmhyalvaftbcsidbmyfxshzdbwsfkvlnunvxzadljqngnnhjmlhfpmwnhvvwaokxxyfslhgggpjnhkyzdqgjdsrtaohqaryixzpyrkjumnphvfpsldrcjhxqjisogvybchagdnoezpvehagcqxarruqncmjifvxxvpbsygkzttmnykeptvbxmjsewbppcciomuyuowzbankzklnnxmnxiztfpfcnddaghyuxgaxmgphspocmpcucxkazeakifbsvnatqcvbeywbxsocgyxiawvmljwmokhbpzvijuckbqrjsdtntlriqgyjznvkkeoszsqsonjlsmxhawqqbdwixvnyemiypirwnoyhvfhbbbkcuyuuepobvrspotbbuvtmpykalufsvizvcelblhokldaymsgqasbobwyxnmcqvzqyldgmimsolloudxkjmiyekaiierxwwflmanqkovzxewrrfipzrclqvedftsuswanhfbcmjigxuxaguasfjypjjrgddnwnrfoazbvezxopumretyqfzqyosmvqjpqnuodylrkucrbhtrljryryewvfbnfwjldgjidvucotlvnsvqyjqwfmqhydttjaapqfdmvcytqpcjkqqrhwfiimbvlkvnvtghrggkjppaduhqpdneeejpqrxbnnenvobcgreldbnzpzrwxvkscywgekcnqnkgngokryvfgthpeggwroimsrwwvfmburaaqrzcmtctfxgrlhzbgixfkdjuerowuvtkmawtsrjzucrniwyzeauuizmfdlufwzqotupmykssvwaqljbiegvbonhqaekpeknpvkzgerjljgridlosexgtjkxnnjcqiahuvwvewsjmxbdhsemaoqsfsgxwghtskfxxxtohbqkascghktyxjeznuhguhvkhkhrgxvfjvktljkvmvkrikybfhjrleqxrwvyevynaprnumwpoazwmbevifrcbcckwmhcqrzgyywxlvxjmckmrfitvkelvoubqmflpmuhlwcjtcokvourxueatywmbsgbtcqzmekogznpbqsahgubnsfzfrvlgqvdsqcjptjkztcwbdciaivtwzavpzxgnbtscpzmffbwzezpijzcxnehhecsdyxabdupyqrfxywcikihubgfwrllhdmampqzewshiumisbuabzuthodmfjczwvwwbxbtadhhqqyqdzrfgzlbtlrtayrflxuehrxmggtbglsijmqiozpaydqxcewzizkdauybxbxhekppdxwnrwuchqotbsvatsxallqoatgdlarcoakioexnkugtpdldgzwnjmrdxtaheygwqmesdtinktgfxwsdibsyqyqdypwpzxucwefnzhfwjcnecbhtpuhcmvnyczwlozxlnsiizeteykfiitgyfqjbsoxvtumabgjhaquojutgxzqniiiisqhixjpcnhvopknagkmbuyqbbhlgaqhrnedonfsinfpywjvncbefkdwiidrmjtfunjhbcyvwnbiffildglmcspbmumhyewizqgfwuvbqawruppyjfkmthxpocpbduzqvecdapdjmiuvzduavdasropcdfmrzdfwkisetbznqubivoqkzvxhiuxowfmrsuevnllosjzzeajuxvvayugkzolddxbhyetzqkrxeyomyjidrculppuxxyuswfzkawloetbximriowohrduwpecmczgurxippfecsdrpybwjhbutwgqqrzckigaqevdazolffbffhpmklobchtddrbaqwfddkizyyhpowbgjiswezvhljhcjmetduxyawxjlzthhuplzwidbcbckqxmnitrniupkrqmzxdyctxgaagizoxgpjcedyuewibyalsvlshpngreerfzrqfloevdearlhcdwmxyjoqozxljgbgnccdefycdrqseaqsybwkvzeeccvkpmvpumlhjhsbaenzpbswpcgnxcvkdwllgwubibjaoiadzndfcodoaczxlugycuhdnkcvxjfzptwutlocwctpdfzfkygjrqxavotfrdlmazcfyjsrffzpnzfmuywpjkgywelrhiejhzeuagmlnefnmpscwcpjlcwbkgqwmohylgekxctqmitgtialbugksfirpemtpeixcypilupvlyppqalshwfeeqsqvjorfmpixdzlbiuxmshemapxjrmxhzkrquumpoiqzdgqldzfqohqyfhjeucjsuvjqtlyopxvgauncwthkcuxrtnsobcpkohuygbgltmgogainwmgebuiesejbwgajeaxhbegysmgfhiqdbpgbzsirzjntnfcvjlrqrstbxgznqzzzlxmkwbpvocrzeyquurrjnoblqeohyqfjhmsakicpazwvbvoouiytydwerlxzffwljqtqcwzytmdbpfloyfoixpqivuatqunngyazxvxdnyxhuahilvwnnmhimgxyvtopgsspwzubozebxefsmvsccyiykpoldfmmrnaywhbkcpgjvhuoclwxkxlbszuasmhynflhldmkkecgxjliseppoqrieqwtjkqidksvxctztcpjgedhsgnarqwyliuwbioarpurqdgubcowdepthbqxrtaxzatwzzoxbyuvinokysodoumpztnvcwtsbicuvtvqxszfdpcfdofzkcyqtojcywcsbijvsgitjbdpmqowvvdtllgdbdotqmkgklpizyltljyfdvmluinspznkutjlhwsfudbwiyrmisaqgjlhcneqnoeqrmsztwdkhjqorbfxpkzkihjpgdggwbajszidcvufnjyqxwwxglawjvneegoxztrcyjqlduczzhgdlesnaeyialxfhtcgwkxjcdsllpqwurenryothdqzdbjmppjyvwzxobkvlrxjytmpklararqdqjjnblxaliqhjvtbzysfkbhroccnlwnslpsvkarenxfezocpdocgamvufzcfjkxijwybwgbfmnnwuuunsoupaxbylxggremxxakntirsqjwkyxkldqokrlwevrvoovoekhesvxmbnycclrdhrzzbovalhtnzdhfuyatdgeyazstiovogkiuuvsjvvofvrfwyoxydkgkvhporcxccrlcecgqakknogwyemwcfmokuflsskyevbdkmmumftzcpdonagopprxcmwwuarqxbxglrnprstubwfjmxpwdsribxcglhhzthhajimjawanewsqmwifzndqwojclkdilkisapeegpeixshskpfdnsbmfjiojelllsvuquupkwvnkgfdwreabvhyswnsnsdofccebjqmawlkqbzcrxqcvargeqvruhgypqcfbltnhswzjbjayqglgsyttnvpxrjbbotzcmoscbykzxoqoqkooycfiviewtmpyzzpicglhsydafzdzresxjeqhahsukeprzooumbltzxhmqktoypcjenuqqlkpwtvyscfcxcodnokzxpcjlimqmeltiipawblteiyaftlvefhrglstuwupkfvjzhrlvejljfahcenhnsqmmcfpnbtwrkukzncabvgyvvfqhsairahkulbejckkoapagatvkhceqswlpzijcwddrooijdcircayscwmordpckluyryrguednmhzleeklgggqujqeobgesjdbpuueenraljjecjxssdosskkbhrnykrfvumazfcjalcttxewlxiwtsojrmeakgzkwympgkdrshbiaamlwwwvacewcjgaruzmcpblpgqdyykxjyybhwwgowlcsliiitgffqdfprvrrf"

# "zzwobllyxktqeibfoupcpptncggrdqbkji"

obj = Solution()
print(obj.lastSubstring(s))


# 12. Integer to Roman
# 271. Encode and Decode Strings

'''

    def lastSubstring3(self, s: str) -> str:
        import collections
        count = collections.defaultdict(list)

        for i in range(len(s)):
            count[s[i]].append(i)
            print(f"i={i}, count={count}")
        print(f"count={count}")

        largeC = max(count.keys())
        starts = {}
        print(f"largeC={largeC}, starts={starts}")
        for pos in count[largeC]:
            starts[pos] = pos + 1
            print(f"pos={pos}, starts={starts}")
        # Initialize all candidates and their pointers
        print(f"starts={starts}")

        while len(starts) > 1:
            # Eliminate till we have only one
            toDel = set()
            nextC = collections.defaultdict(list)
            print(f"toDel={toDel}, nextC={nextC}, starts={starts}")
            for start, end in starts.items():
                print(f"start={start}, end={end}")
                if end == len(s):
                    # Remove if reaching the end
                    toDel.add(start)
                    print(f"toDel={toDel}, continue")
                    continue
                nextC[s[end]].append(start)
                print(f"nextC={nextC}")
                # Filter by current letter

                if end in starts:
                    toDel.add(end)
                    print(f"toDel={toDel}. end={end}")
                # "Swallow" the latter candidate

            nextStarts = {}
            largeC = max(nextC.keys())
            print(f"nextStarts={nextStarts}, largeC={largeC}")
            for start in nextC[largeC]:
                print(f"start={start}")
                if start not in toDel:
                    nextStarts[start] = starts[start] + 1
                    print(f"nextStarts={nextStarts}")
                # Select what we keep for the next step
            starts = nextStarts.copy()
            print(f"starts={starts}")
        for start, end in starts.items():
            print(f"start={start}, end={end}, s[start:]={s[start:]}")
            return s[start:]
'''