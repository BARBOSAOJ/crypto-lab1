# Lab 1C - many time pad
import string

CIPHERTEXTS = [
    (  # Message 1
        "0f381a39fe6f41bd57c44646eacc3ecb2b695ae729ee174ac650ab0c92547a73b19ca7a24d40162b"
        "ea9c0d1c2c1395678f6dec2ae8b4eaa449b1511507c3e06dd6c9c02c69c5eca4241d3f3585f44440"
        "ad011078381bacc075e4c3"
    ),
    (  # Message 2
        "0f351c71d96e59b742c34053a6853d9930664da237f24456874ae61198546b7ea6c8f7a34b581823"
        "ead8490c29568e618b68a929f3e6e6ea0ca35f1944c2ec70d686df3028c4f9a42a0720748cbb4e41"
        "a74c07773213bad56eefde922d44cdbcbf3e008be80870a5eb7c55ab907f18fcf347dd433bcf8343"
        "2d0849e80c22b0"
    ),
    (  # Message 3
        "127d183cb07342a042d40553e9cc3dd83d2e5cea3be91756cf46f904d74f6c3fbcd3b8f04f431c27"
        "af8842003147c27a9425b82fe2e6f8ed5fb2540e05c9ee23d681cc3d28c7f6e227522466c2fe555a"
        "a34f116d7b1fb58168f4d8d72c0dd3b3bb701197fe087baefe784eac9c3002b4f9488f0029c08606"
        "341d49ef113ff7cdd8c60abe6f5cefbff792e9317e4f9d36b948dfddf409e264580f65"
    ),
    (  # Message 4
        "0f351c71e76f5fbe548d4c54a69a2bcb3d2e4ceb3cfb5250c24dff419949683f8ed3a5f04f57116f"
        "e797410d2c138b60db6da534a7abe0f658b65b5c0ccbeb67d1c9d9216d8befeb35173f3596f40d4f"
        "a84e1e702818fbc06bec90d4315fceacfa7112c3e55d74aaf3394bb08f7504a8e5019c4e3e838e0f"
        "364946f31721a49ad2d24ff6775efcb4f79fe4217a01b43cb5068bf3b52ca76543187274"
    ),
    (  # Message 5
        "1a311571ff660da658c80545e98325ca646746a22ef55202d04cf90d93067c70a6c8b6b94c161120"
        "af95421b3a138b609d6abe2ae6b2e6eb42f7431405c4a56ad1c9cf3b67cafbe72301393583e80d58"
        "a34517767b19b58166a0c3db304acfbafa721591ea4d398af07c49b69a7118fcff4889597aca8143"
        "3b4953f50b2bbbdf9dcd0aff7013d3b5a3d3ec2b73019c3aa91b8bddf411a72b480c636cc6597494"
        "151386"
    ),
    (  # Message 6
        "1835183ce0614abc558d4c41a69521cc646f5ae77aee5247cc4ae506d752777ae8c8a5a5565e5f26"
        "fcd84f0c2b47877cdb71a426e9e6eea440be525c00cff166c19dc23b28e2eba4271c2e7a97e94c49"
        "af5252787b1dbacf27f4df923c4883baa26e158dfe416faebd7c4dba973004b9ff4a914529d0cf14"
        "32004cf94520bedf9dd00aea6750e9b5a580ad266d44de3cb304d295f447a1634c117a68c41e67d5"
        "0d09c35928a62e6d6648371b40ac83b274cecb04d6c41b6fba"
    ),
    (  # Message 7
        "1928103df46943b510d94044ee8227da256208f123ee4347ca50ab0899507073bed9a4f043161320"
        "fbd8420f7f5b837c9f25bb28f5adafe542b3170f14cfe66ac385c4336dcfbfef2c1d3a7987ff4a4b"
        "ea4d13773c05bac662f390d3304983afa871008cee4775b8bd7a54bb907e11fcfd4f99003ec68d16"
        "3d0e49f2026ca3dfcec006f06513fcb4b3d3ff2279409d27b21ac2dbf2"
    ),
    (  # Message 8
        "12290a71f96d5dbd43de4c45ea896ecd2b2e45ed2cf81756c803e70881433f6ba79cb8a047441e3b"
        "ead84c1d7f528c77db69a931e2aaaff345a35f1311dea56fc788db2066ccbff030132e7091bb4f47"
        "be52526a3e15b6c869e7dccb7e40c6beb4771a84e14d6ab8bd7f49be9e7d13b2e852dd4f3c839f06"
        "281a4ff20420f7d3d3d200ec6f52e9b3b89d"
    ),
    (  # Message 9
        "14331c71fd614eba59c34007e58d2099206108f632f81755c851e04198403f79a1daa3a902590d2b"
        "e6964c1b26138f6b95258228a7abeee744be591944c9e46d828dc2697cc3faa4351d3f7ec2f44b0e"
        "a54f17393e08afd366efc2d63743c2ada33e1982e3"
    ),
    (  # Message 10
        "127d0c22f5640da65f8d514fef822599306649f67afe4e40c251f81196457a3fbfdda4f0445f193b"
        "f6d8540c3e41912e9a72ad3ea791e7e558f77e5c10c2ea76c581d9697fcaeca4241b2b619bbb544b"
        "ab5301393a07bad827f7d1c17e42cdb3a33e0086e30860aefc6b48ff986717a5bc6093447ad48702"
        "2e4969bc1124b8cfdadc1bbe7552eefaa396e36766449f21ae48cac2f41ee262595d616cd9596399"
        "0b03824934ea2a287844722140b583a2638bcf16c3df0323a212740f3d5b517fbd10e4e253512e"
    ),
    (  # Message 11
        "0c385930e2650da658c80544ee8522dd366b46a235fb17438757ee029f487073a7dbbeb3435a5f2e"
        "e89d0d3e3a138a6f8d60ec21e8b3e1e00ca4430e01cbe86fcb87c82d28dcfefd31522273c2ff4247"
        "a44652742e13b38168e690dd2b5f83adb56b008ae34d39bcf26b50ffa9621fb2e84893477aca9c43"
        "340600f00a22b0dfcf941bf66713f2b4bb8aad307e58de3cbb48d9d0e515ad6f581e7f63cd59609a"
        "160d900d1faf2329634f354814b793bc37c3d700d5c71271e30d740e7815516dbd1af8a344533fcb"
    ),
    (  # Message 12
        "0829003df52058a155c90553e9cc2cdc646f46a233f34347d542e8159e49713faad9a3a74753116f"
        "fb90484937468f6f9525bf28f2aaafe542b317080bc5e970829dc5287c8be8e130176d798bf6445a"
        "a34f1539121efbd56fe590d6374acaabbb725486ff4939a2e9394cb6957c56b4fd5798002ecccf00"
        "350445bc033eb8d79dc007fb2240f2afbbd3ec2b704f9b"
    ),
    (  # Message 13
        "0f351c71c7654ff251de056ea68920cf2d7d49e53ff9174bd303fc04d74e7e69ad9cb9bf56160c2a"
        "ea960d002b139b6b8f25982fe2e6e9f158a2451944c3f623d19dc425648beceb621f38768abb4f47"
        "ad46176b7b04b3c069a0c4da3b0dd3bea96a54b7e4453989f86b55ba8b635b90f944"
    ),
]
cts = [bytes.fromhex(c) for c in CIPHERTEXTS]
length = max(len(c) for c in cts)
letters = set(string.ascii_letters.encode())

# step 1: guess the key using spaces
# space XOR letter = letter, so if one message has a space here
# it gives letters with most of the others
key = [None] * length
for pos in range(length):
    column = [c[pos] for c in cts if len(c) > pos]
    best = 0
    for a in column:
        count = 0
        for b in column:
            if (a ^ b) in letters or a == b:
                count += 1
        if count > best:
            best = count
            key[pos] = a ^ 0x20


def decrypt(c):
    out = ""
    for i in range(len(c)):
        ch = c[i] ^ key[i]
        if 32 <= ch < 127:
            out += chr(ch)
        else:
            out += "_"
    return out


print("After step 1:")
for n in range(len(cts)):
    print(n + 1, decrypt(cts[n]))

# step 2: message 11 is a known quote, so I use it to get the full key
guess = ("We are the children of a technological age We have found streamlined ways "
         "of doing much of our routine work Printing is no longer the only way of "
         "reproducing books Reading them however has not changed")
for i in range(len(guess)):
    key[i] = cts[10][i] ^ ord(guess[i])

print()
print("After step 2:")
for n in range(len(cts)):
    print(n + 1, decrypt(cts[n]))

print()
print("Message 13:", decrypt(cts[12]))
