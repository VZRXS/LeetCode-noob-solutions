#!/usr/bin/env python3


class Solution(object):
    # 5. Longest Palindromic Substring
    def longestPalindrome(self, s: str) -> str:

        output = s[0]
        maxlen = len(output)
        for _ in range(len(s)):
            axis = (len(s) - 1 - _) / 2 + _
            while axis > _:
                if s[_] == s[int(axis * 2 - _)]:
                    if s[_:int(axis) + 1] == s[int(axis * 2 - _):round(axis + 0.1) - 1:-1]:
                        if len(s[_:int(axis * 2 - _) + 1]) > maxlen:
                            output = s[_:int(axis * 2 - _) + 1]
                            maxlen = len(s[_:int(axis * 2 - _) + 1])
                        break
                    axis -= 0.5
                else:
                    axis -= 0.5
            if maxlen >= len(s) - _:
                return output
        return output

    def longestPalindrome_attemp2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # SLOWER THAN THE ABOVE ONE
        output = s[0]
        maxlen = len(output)
        if len(s) == 1:
            return s
        for _ in range(len(s)):
            axis = (len(s) - 1 - _) / 2 + _
            while axis >= _:
                for i in range(_, int(axis + 0.5)):
                    flag = True
                    if s[i] != s[int(axis * 2) - i]:
                        flag = False
                        break
                if flag and len(s[_:int(axis * 2) - _ + 1]) > maxlen:
                    output = s[_:int(axis * 2) - _ + 1]
                    maxlen = len(s[_:int(axis * 2) - _ + 1])
                    break
                else:
                    axis -= 0.5
                if maxlen >= len(s) - _:
                    return output
        return output


if __name__ == '__main__':
    s1 = "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
    s2 = "thelviymgkeddreyviespjsyqwmbmnlwzjhdokfzrczvreiagayofwvhecskjqlqzodtozvzozqyiwfsjyrinrmgfyhplybonzuvmxxyihmggwiuccplqjtgschmieoexvtewbsjqzkzapfxpzhgjtbmlchevohmxnbattphvobptnhmcoihcaimchurqpucxapojgszpopdvsfahwidiyxlpjfhdkcoewzvlmaebudtovnvcuadykhhmwfpilqfdvnseiitokcbuxmhwukrdxwvtgztczrwcsydqwosnktronibiplbljrcpinqorbhxrwjonnqeniebrksjkcmbvjnuwdedoenqmrcxayqbzmlpbubnfnkkqnuljtchaeijcmfpyuxkgfssoqliqmhowtbmcvzkqbanxhowjjejexxlihwwhilxxejejjwohxnabqkzvcmbtwohmqilqossfgkxuypfmcjieahctjlunqkknfnbubplmzbqyaxcrmqneodedwunjvbmckjskrbeineqnnojwrxhbroqnipcrjlblpibinortknsowqdyscwrzctzgtvwxdrkuwhmxubckotiiesnvdfqlipfwmhhkydaucvnvotdubeamlvzweockdhfjplxyidiwhafsvdpopzsgjopaxcupqruhcmiachiocmhntpbovhpttabnxmhovehclmbtjghzpxfpazkzqjsbwetvxeoeimhcsgtjqlpccuiwggmhiyxxmvuznobylphyfgmrniryjsfwiyqzozvzotdozqlqjkscehvwfoyagaiervzcrzfkodhjzwlnmbmwqysjpseivyerddekgmyivleht"
    s3 = "xdxtfdaarvvznrptwicdldmrmwbdrmyppvamdvofujthfcmkcugvodmlvubgvodectwzparprifwgwfvddlrfdnrpspirtyvxqvbqiglugbmzoyzcfkvbjdrdqqxxzutebgoacczuhopvzjfrnfsylgfgkbmbjqqyggtdjcvjbvpspkjcezanajjzabfidndfdpkuamwvxrbpxzoivlnkwdxedtfnmvicmzebwktpktokibeycbpqzejddwnvimmbzupyxwmrgdbmcujadfexcchdkfvkxsdwkuwuxzhpnjgmqbmidcwywjgcsbydixyxcclcbrzjvrmlrzgmbviifllouykovscaufvxovwmmgubshtoizbwtcpqzwchtkmkjfneuybfglywfrorhmfdgvjdsmegtoytsivnuaceszpfsxgddbweckgziahkslykgdkztmpapnoyawqtyrdcuzaxcohohapektyfbfhrsdnjbgjvwvqpcikdnlkdogsinkfpymkkdburnbksnqfjgjlacqpfqlhsjhhoccdkrjipqwzsxmpjughaqchzlrqkogkryqkuuxhzchovebzgeekuflcgvxugnxcvugqlstmnljlvxonkybmzjmnsvvwfztcplgikptnppbzeygbmdsyimsntveojwsejmastiovbctdkdlfvpyzihhxishtveflnmamlnzqroxknrrkkfpveyzvvasdznykygrpbfkbinrrvheekeumlvlgalqelspvpiydqkwduckimyhpzsxlcpkbvgwmwnasdxuupdhcmxjoushcvcnjyrmuemuydyywpvzhkxsqszaqhnbhjwsokkpployomoawtr"
    s4 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # from time import time
    # t=time()
    print(Solution().longestPalindrome(s=s4))
    # print(time()-t)
    # t=time()
    # print(Solution().longestPalindrome_attemp2(s = s4))
    # print(time()-t)
