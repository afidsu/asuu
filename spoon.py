import requests, json, os, sys
import time
from requests.exceptions import Timeout

banner =("""
ㅤㅤㅤㅤㅤㅤ\033[1;31m╔════════•ೋೋ•════════╗
\033[1;33mㅤㅤㅤㅤㅤㅤㅤ╔══╗╔═╗╔══╗╔══╗╔═╦╗
ㅤㅤㅤㅤㅤㅤㅤ║╚═╣║╬║║╔╗║║╔╗║║╱║║
ㅤㅤㅤㅤㅤㅤㅤ╠═╗║║╔╝║╚╝║║╚╝║║║║║
ㅤㅤㅤㅤㅤㅤㅤ╚══╝╚╝┈╚══╝╚══╝╚╩═╝
ㅤㅤㅤㅤㅤㅤㅤ╔══╗╔══╗╔══╗╔╗┈╔══╗
ㅤㅤㅤㅤㅤㅤㅤ╚╗╔╝║╔╗║║╔╗║║║┈║╚═╣
ㅤㅤㅤㅤㅤㅤㅤ┈║║┈║╚╝║║╚╝║║╚╗╠═╗║
ㅤㅤㅤㅤㅤㅤㅤ┈╚╝┈╚══╝╚══╝╚═╝╚══╝
ㅤㅤㅤㅤㅤㅤ\033[1;31m╚════════•ೋೋ•════════╝
ㅤㅤㅤㅤㅤㅤㅤ\033[3;36mᵇʸ: ʀᴋʜᴍᴀᴅ\033[0;37m
""")
os.system('clear')
print(banner)
print("[1] untuk live")
print("[2] untuk user")
print("[3] untuk cast")
modexxx = input("pilih mode: ")
if modexxx in '1':
    print("\033[1;34m[1] convert sharelink room [eg: https://u8kv3.app.goo.gl/CJ2Nh]")
    print("[2] direct link web [eg: 4919698]")
    ask = input("\033[3;34mpilih mode link: ")
    if ask in '1':
        txtid = input('\033[3;35mmasukkan link room: \033[3;34m')
        params = {'username': txtid}
        headers = {'User-Agent':'Mozilla/5.0',  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
        response = requests.get(txtid)
        url = response.url
        slink = url[34:-59]
    if ask in '2':
        slink = input("\033[3;34mmasukkan potongan link: ")
    print("\033[0;37m",slink)
elif modexxx in '2':
    txtid = input('\033[3;35mmasukkan id user: \033[3;34m')
    params = {'username': txtid}
    headers4 = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + txtid + ''), headers=headers4)
    idd = response.json()['results'][0]['id']
    spoonid = idd
    print("\033[0;37muserid target",spoonid)
    slink = str(idd)
elif modexxx in '3':
    print("\033[1;34m[1] convert sharelink cast [eg: https://u8kv3.app.goo.gl/CJ2Nh]")
    print("[2] direct link web [eg: 755536]")
    ask = input("\033[3;34mpilih mode link: ")
    if ask in '1':
        txtid = input('\033[3;35mmasukkan link cast: \033[3;34m')
        params = {'username': txtid}
        headers = {'User-Agent':'Mozilla/5.0',  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
        response = requests.get(txtid)
        url = response.url
        slink = url[34:-58]
    elif ask in '2':
        slink = input("\033[3;34mmasukkan potongan link: ")
    print("\033[0;37m",slink)

token = (
'bdd49d8ca85511dfac337872d6ea8c927d7aaadf',
'fe4219960d2855663601c59b87198cef475d76cb',
'423b92a2c6102ed92acdac2b854dd1f1010d2457',
'7ab19aee7fcea47fea313f27cd9c4c847e39d1cb',
'09fd0fae27160e34eb475cfe97daa82adbf2e73a',
'2d7a424abac44053c48297ec467dfe5d10c76e7c',
'4972f0785012b536fc0ef520e410444af1026fad',
'd4a5e28158e446108ef3e25480ea433bfde1bf66',
'5641780701f17b9d2ac81b1237636373e045e008',
'e3ef6ae25415817065427a42b637d3d79ada8e41',
'29017521e27da9b4bcda91a29528b2c0cbc31dbc',
'57b52fdda2574745c09b84f5ff92f121313bbb7e',
'5de52dba591a18af9e88964a216dc6c4f00f3814',
'e3b27ae637b530126c3da30f59fd4d9c19dabe07',
'ff8727cf1a2be016ee210d55c096246dac52528c',
'124a200f574cc13e80d6125216429ac411a443c8',
'f98b62594842f3f5e87a430ac79887b42646b7e8',
'cdafce1844a8848fb1eda3993b2e254faf747821',
'48d5345c90bc1a546d83e57beb0be1aa02d8a072',
'75721ea472cb941953ff853914c4a0db5a937c2a',
'08efa2ee29a96972627253dc2986ab440745c608',
'12a979c48972415d0f122ec820b8187e67688b99',
'8d42611afae2c86ccb7ed30520320dcb3d8f3c79',
'2587244fa0f2a258a620c32d736f0b9cfa974881',
'f872407eeb6b56b0fab9581e1216521e43e3dabc',
'9f051fbb26cea8c7d7b3b840e58a49aee27a5ab6',
'65dbf70ca6ff66aebe40c11c4ebced4195ba947e',
'0e4a93b0cdc36e894b67735cc45ca88bd1e058f4',
'f7394ec3fbb2af2fdaef3633e7b030cdb47e6ce1',
'cc78631f4ce17f0aa805a01774c9bdbb10f5f373',
'886b5cdc1baea8525598d5032acd6fcb57944025',
'dc4b1a98bff5a2a8cfe22ca8438350a2db6a9abd',
'fb1aca04a26cc3facb0c4d33b9e12b77265d9c3a',
'4b8837570872b6582f0792126cfb11182283ad08',
'81a99e2631b368b75639e7fc8fbe34836affc34a',
'60c705572e104dc9b3043c21a511dc574fef0173',
'bc659f060272f05ff6a1e3580662800f05888e0a',
'8fc4db24ebb3ec940a9062ac1c86bbcfacb9305e',
'de1086cd233da1568eb5c4f4a640a5ece1fe1447',
'951408e6e4dfd7926f0f1972a61b600ed0090795',
'f6baa68dbce42629571d0f6f398f0502657849eb',
'3fde52e0a35193b82c09eea8178b7804a1d664b5',
'89d83c68ba3ae9607c471acb416d43ff24fc49f3',
'c32ff9b0f5123fe5fab2f891a78e59f9ac44c618',
'27e8c2b2c1709f7813e6f1c5784c2b20bd44a9ef',
'fa8f79dda57556ec1a57d71ce64c99684270cbed',
'a8b52a929cdf5a2edc0bf043fb1706df2535890f',
'5a6262049b9b2dd3821ec60fc4a8cbab6a01fa8f',
'ed8e8a0c4d1e1c8acf7a31c808836542e9effbf9',
'0a718d11411a0b8efcc2b27df6632f457cf58ec4',
'0c63c44a13e909912a35c3072881916b3985d595',
'e77724bcd24a3550a77ad9b1abf6e39b7d71818a',
'c5ec4b36f216611f87e404f687a55d22bbc74077',
'755e1d111e147ba62ee174c41209b2ea5e190fa2',
'57acb40639a224595533a96465e710cb72ac5204',
'335cba7b161af69423e809bf1e6ee70ba9c6513a',
'6bd2a9ea129fffac24d87c7b09cd2fd386ef7284',
'719b4f5f23a44c47df58ea85715c2742a30fa79d',
'0daf82c0ee85d4dcede11748e07fb4fe00a5731e',
'0958bdf41c60a8517441a7781dd3683fabd1e569',
'bca6b642b18fc777d450714cdc37c6a8e63e7a5b',
'5dbd83c9730302acd287ad8061635cbff40f7b9e',
'769142c01bdb8e2e21cfa8a837428dcd24eba0e1',
'9ad87b8b98b3cfff0fe6e0ebcb29dc0b6b2f90b7',
'81bf7ffc3a273f0424412971f8b2b0cdec43c6b8',
'f6a52af6f5af3f081aa7ee121eb0db721830a587',
'a59dd850a75bf735adc079d6aeb468cfbd8cc2f1',
'e6104239e8d53d133f9b79b3536234b5d577187b',
'8c65e50923c60c3df05ef048256d27b0d20f3c12',
'7fb03337e72dc351209c69fd88d4eb8b8513c0b1',
'83ec91d286d5a9aa961864905fa04249d13d494b',
'0d0038c514400df8f54222f1b1d237e53301d444',
'75b67e43e118f7c057123c559a1e368bbadb7a8d',
'58f84f929e99588c4f02a9694312dd3583ea3613',
'a94b13c143335570b9e7c2dfa3e5aa8c61d807aa',
'ce7c9a02baaace428dd3dbf37d3c13570b10f636',
'35e803edd263e4aab29b260dba27c0d6c7fbe9ce',
'310d117daf03dfb57fd347d2769db7ed3bcea79f',
'e695f2a1a88a1e415b0a69b209ca4a538cf18df5',
'205aea8a7233425c029276abe6224e4df7170e85',
'01a3da48645562b0a1e2e0d50ac5ad7986f6f804',
'ba6290507f2d01197cd23c9335424159e7caec67',
'7c1f3082db36dda7f1c4194c7b8794006f939cf8',
'c9fb296a62a3dfb00e2d27becebef95a7822ebe4',
'be21b9fa029107d6131296b9198ad7195b33ffc4',
'953539ae7e63f1727092982540902cabb8cedd46',
'4946a492fec793132de02298c5877c4046831c48',
'0985828b3f66ad9d008151699331e7d4b7dec151',
'e64bac7fb45eedd1aa826cc4b0838639107fd56a',
'8a00d32178fd553153f6d7a767a239fbca1886cf',
'9246c55a551d67c2462108141f0e5bac4991a517',
'6fcd13983a0142ae804573e34b00904550f574e3',
'2d34a278494f58a5ebb3e67e5a3e12db43b5034b',
'c0ecb8b04d88d5eb49b2373bc16c923ced29c524',
'0eadf1894c07a97244f7ccf84cec1b132cba976c',
'32a0eed4f28e961715feae1ce208c0d07f46c735',
'0ee869c0712c42ad6c8662c17aaecd19fcdf8dd1',
'b7c77a59171502e39c4bf386246384372d47043c',
'a97b4fedec07580b1b3a9c1f9cc00e2e4b7ce4e8',
'cb92f75c76602dae7478fa7519022512deaae9d4',
'440b33dad96b0e7f1be7054076f2cb5179032686',
'7fdee01317e66764629b44627674074cd578d242',
'69e42c08f4995d9ccb539f8ec4bcbcb0da719e3b',
'6057322086bbcac056b1220abe2cba40c56aa611',
'35e09792313363e7da3e0a0d64c987ab81fc43c5',
'6aad3d237c2bb89d2421945afec76ebd1e45f951',
'fb259d300a1e0b4f414d78d571b3a4dfa8a7f1f5',
'c0e830cd6db1d67f83d62a54a675598af3d45591',
'667ea1931450552c34bcf40f9e5c3085bafab416',
'8921300150827e6b58aebb786e0d0f7fa1225f0e',
'ca353f6ca3b9b4f1a5b12f4e875e61478682fca9',
'44eb50e19d565eff8cc9490a54269bfe2b2e35f5',
'1748ea2ed743bb30dabd3ad781ac43aa675c0070',
'3a23ba9f94eda441a41022923ae758f108b5b0cb',
'bfc497beafb62e5daa6f46e3fbbeec9b9a1932b1',
'23008ab0165eca0e22ac3edf2ef99f6c4c1673fe',
'234ff63cdc5db19a4d8c7ebc4fc1814918c2fe94',
'1a620e8563dc1c7b05d3d92a1b41daefb16a721b',
'0ca359d8f14fcec9a9fc1f6d9e5334706e260438',
'5b1665a5166c3e8151cb359be5b9e5f52d1c33ff',
'd2cad024e4efae0d62d3243c132044bb57efe38f',
'8a10ad00ac70cea5c403725c6376ab61e1c263da',
'4be632cefd894ef37a93605383389d1693648e76',
'ea6fce6d0d9d47573123d44ab2726b2bb661dccc',
'e0a73368d1cfe253f5112c42518a197706d879f2',
'a273d745616c65b33cbd48e2f40fbe9fa51a0193',
'faf5e91f391565d0a96c5f8399ae04a97c7a2d90',
'35504899a6a87d63de8410a416e9d6288c9ead60',
'bfd7e29e08b8ca6628f0db6a90ecef5d8ccf3121',
'339025ba95a7c75cd1a46015a891e4d939be041b',
'1d5e3136981b32ecb2949d84a0f930a92a9f8891',
'dcde4de30c7899321308defda0a70fe7d922921d',
'1868c239787d73e3d2740899a45ce6f5a1450bf9',
'582265366196ef856292ce52caa4403e53f1fa35',
'f1455b00d12b5419a9b580fcfd028cce998056e4',
'a0683f0f3fc91ebacb08c993b440392b2d225689',
'9899ac8c90cf0e5bc9b3bb327160e438a6b6214f',
'ee0db639f8b3e74ddea3e45c1bfa3bf7bfcaed24',
'8898066bd789638d4bdfc5e3cbdb4bbaa0972104',
'68e6f10a7ac0ce82e25007b3118a224ef6e4b4a1',
'7c279d694095c68035f7f365f284d73923bade0e',
'f50009bfc0ad907f6eda4aa52d96f737caf53be5',
'fb9b218b2b72ff05f5bebad334a7f80b5cdfafa4',
'752cba16e82b5a97822b81f72e3fc2b33fd9b99f',
'b674226dfae89b236add16b2c7df259df380ccc7',
'd467cc6b0bff0054b63b165b24f8af3d0af9602f',
'dc9c9d6c9ed226e02b84115618ab99512bdc77ca',
'90c5cc0880c7dd04a20c6a5e2a197f3a01a99d74',
'1099c25fa3b5d607ea1c18165f4b64a72322c440',
'840b720f7c3f3a0e41d04cf2b700bb891805c91d',
'4c31294dc67b5d0669ce1df42fc01362b1b371ab',
'a3297d55064ae46ed06892133c342e91df724cb5',
'ee64427066f50170293ea1102fd37b4d035282fb',
'1845ef553445aafe2fcee7bac5005b84044b9db7',
'56cc8c8f42e17523d1baf6efb400b8e9d5e1a1c4',
'4fe8d359aae539007b08888a47dd22e92aa46780',
'4ce1e3cdcfd21ec5ca57148d1ccb3e90c7d51e54',
'8aba4c81ad709b20944c4ee2363d13a7bd9dcebc',
'7d55a161732b472aeb054807b091783654386009',
'3e6065a767e9e8aa5d0b560fe5d6a4b8f3e3b7bb',
'6d1a8a2fd2d154dc1eb97e61ba356635b8c4aac7',
'3570107f623c545f6053acbc1479538f9518d652',
'cf3231fb3dc2e1bfee17f0a48b333f99889692c6',
'b9bd71ae4b6714cc9cfa2edd1ebf21077a9efc16',
'2632f430e3313782b2174d61aae30c3b01e64d2a',
'8fe2d160c20bc3b782f84952e43ad9cc251dea87',
'f2631bbdd75355ca9872ddad1119a2fc9738050a',
'f96916bcc4d2b5b3d2ddf282f763a4908aa11cac',
'1faf226217de0f5dd95dea38c951f46715167338',
'122d0ea725c3456ac5f85ab6aa1db557402efb9c',
'8177a12cc3e33b11d2d6ef8b1d4ddc01774feadc',
'd3e4ec4b6befc2f02a418d00625823428ab56a7d',
'bf144533c3a8029740fc05925e915c7c17378e2f',
'2e8e6df7fa561e6d980afda686884e8fc131e30e',
'8d2f2ab0dedd3ecf0b3029f3091f44dbf805536b',
'ccad82f64aceb0a9ee3e7c10d4cac91c16d2a783',
'4f1bc5d2d1981ef851d01697e64f10bec856eb78',
'76e6cb6dcb37d353446c7af2c6afeef166955c30',
'b7aa28549b64e4fb7f2ef0a8223aa2d229bcad21',
'b2165143dd64c89447994589e175638566ea13c6',
'517c3670342cf1934f6b9aac3e2be9e03274ad26',
'ee582caf9185dbaa6ff9949cf1623dcaf5747730',
'519cf393e74951f0abff577c4bc46997e22e0379',
'c1783b498c3dedfe5a2a504edd84dc3ba9c76166',
'79d4b1236d38433a8e3fefaf3830eb50a84616de',
'7fe2779a34271366f692d214d312ff6989622eca',
'f86bc2aa3c3a925941b8d5580e477e18e08a91e0',
'888045ddd9f385ce4e97704ac1d54aa4695a6c15',
'39ba6f6957a80495ac80e638d7fb69be246b7afb',
'46b67351e331fe86331ab097d794cb1589a4a830',
'8b346293305e25699daebf95d14543600cfcbe05',
'f6fdf91cff0c63b909c45a0b3519c54f5fe3eb65',
'3b82a11a4f018e885ac3665e335ac920ef3368c4',
'a28494e7770f062d8f641d8e3c13ecd68a43ade1',
'bd8aefe8ac2c917d9a9c8698c866207880d9f43b',
'46ec82c62839dbb6b94f70e6203ded5f1ed0bb98',
'c75241a40740e52ea3553f75a6cc0e011b4abff5',
'062b4c69f75a7f0adcb14b19a19b2a792df8cb50',
'46c3e434d237d951366b2f2c7cf078196e0483e1',
'3e5c9429419fad8ff69b4dd823b808373986482b',
'1e61676955716ed566f83e84e1df137ec93d421a',
'0057504cf1cf33ea19d96e4692088b0c3f08ec4d',
'd6b098a1afa313a33e1fc3c2d592ff1888006971',
'5d7a35ae391caa124085aed670c49b3c3019c680',
'9912decdd8a6b7664f4268b520b21817e137bac2',
'abe5e994658533204ee9150957be2ef2e6fd7b7a',
'ce5c43e71af39a1d73ccdd82b1fa89b6feb65454',
'91470f2058a808208dd6e315d033d342f19ae9b5',
'c8105d614236081acffb42b16d565bde20102443',
'0eaa409eba6759c9303741b32638d509a97311e2',
'de5986cedadfe8729a681dc7100e1a75b58ca01c',
'23a904d9bca954182dcf914f04e46558ad5049b0',
'edfc5caad7c71462b5c1eabf9902d9f0357c215c',
'cfed59b22abe83ba10d48728a6502c4f4351cb1f',
'5059793126c598d4ba03609c9ca6bcbf786c3225',
'2c484d64724606e06ef4c4f6ea25a246cf97181f',
'2e0e3946e18208c314095dbba8ba717eed9dce16',
'6ae5e7e0d6ffa630b85751f1cdf193b562c46201',
'86f36e6f7044c3986e402867b18b15db7ad3302e',
'aa61d1752f6129d277a46290fc72d7bb20a3534f',
'3a29512a5973772647b1f7fcf0e0117b34759d23',
'860bf3846a5fa4dd02b1d604f7c5eeb3b7174b68',
'36368d6eaf8e1cb297ca36b3ef21e6e009081868',
'552e20047a3ca87d1e108576bec074f89d2eebc0',
'7072b9aee82736c0dfa75707407d47d9adb13022',
'5fa1a410f6117132fc8888e03a642b130d7038c6',
'c3bdb465fbce801aa2188bba5ce9a8fff4261d8a',
'd51518ab626ab2e814ff09af56c0b8daffcd3479',
'303f0687304289a22fd0fce7993970fca016dc44',
'a1bac9907dea70f5f265401579f7c72772ecfd5b',
'485c557f304c8b9ea679b69d571471ae556010a5',
'4e9764638981e2c13a15e0350371cc31a5e231c4',
'c65ccfe06f61c4dad6b4bd46affd17cf1efc2306',
'332eb755fb455060abdae8d8624e1ea9063f95f4',
'3a8b083f48a533d653eace1094d01639f25fdafb',
'12e3ec9c0789d41afe6aab59eb166d79bd60371e',
'b37ea4e14e819a699494f28b2a3ca986c6d24a81',
'0bfa137351b28022389c4444f3f708397c296c42',
'4a30ad6f53e001d187f28de2eee759d2178f192a',
'44ed4caa06fd61034d4658ceac42d8912c16025f',
'd949b5edf798555287aa77952552c23a65a5381c',
'fa28ee60cce0a4a40fe3a42aa17c66d739b0707f',
'cc41b640e6ac201372d1e5b194b986a1582152fd',
'56527b9eed03d9258664b29deb71f09dfa01f7bb',
'5fd474f188145e16e4c0341655a4878f269deeb2',
'5e2f08834d8a923f671b8b41bcd6d8b9ac1bdbfa',
'ff30744f050da9ffe8a3c40b73ce3c74787ecbab',
'b7adcb3f09b8ec93b8957a06fa5b69f904eeb175',
'3110227c678df0086b2960f700b08fdc8cdff692',
'b485472cadadf03d8056fc4bfa01cc0096bb5de4',
'79c7dc308859673f44dac33b659856d296135a8f',
'503914e6e45eb83605240f4471097c716ed56ca6',
'cc8b3bd679007497f92de84e6d080c0d4f8078e9',
'bbdf7f974902caaf84b1a17edded76a7d82133f7',
'7caa01454745c8e193cb781b842e9a973fd6ab73',
'60af24a41a99ad61d10401af35ae5bb22b66db59',
'fdc874afc7e8c57f4c327b68976a398c4528bc01',
'6a06647a142430d4bc05f2bd8a6dfbe30bef5528',
'c79600417a1df9d3aeac4a413b5a5404e0d5d792',
'550403063ef01a6073e4ecfdb871feded37410b2',
'740a956fa91f746fa42700237f4ab0c41596e95e',
'cedc00ddba1f5341bcd7c9588b05c536cac41df6',
'01dcb32dd814dcd1c4436728ee9362cdc05bd2bd',
'659f4f3c7a9b7d394c4ce3eba9c3e168388669d2',
'43f28d480668171d0332e87ef803553580340eed',
'043231a0e7ca4efc703a5a34d94c1cd4cd0100c3',
'31605a1856103f4e596123e5be38381d3312ca2b',
'14bd29b9059db2dd1c927cddc63622acfe179cd3',
'9c42fb5481d53fef446cd34db0872d979eb1bc1a',
'4ca1b842253cb36f5c67a9dc4eee70a299136830',
'51f9006f0e4dbe6cf222e93833a6656966eb27a1',
'6689e1a24c72658e54b0f1f3172ae56cd96917ef',
'61d1de185876d20061440ad37a20345d845a92e4',
'4f87157431ca9852603fc9640ea0c0a55150fb60',
'3fae4fff81721c12416742b06612f3b912d36457',
'12e0b5c0dac841b9558aa528c65048db26ec9303',
'd5b85aab3e1a64d73c3f5577dbcbc780510a6074',
'f8bbd14646b718222df603d2d32f44c5b6589463',
'354418d462f341d07b32134a606a797fca0757b6',
'7cc2b93ac89d2cdce747ee07f7ef013c0302ad63',
'b128abfc21b2eff083e4771ae2f668913402eade',
'8de506388d56dda6416e8c006e4aaee5834d483d',
'ed5ce716e61a28b0ba96e0c3c81167da52d948ec',
'3d17e70ee6b3fb42fc7d226d8148227d041c51af',
'ca14c699bfdd6c9074fdfc9a94adc15eeb418f2a',
'd7440459e4807baaaa51751e9603423b390b07d5',
'6a38456d9e730290dddbc5524d0b000336f15b3d',
'a68e7ef373cace8019e6a6184bb29fa4f65289a1',
'aa1615d641242afba1c3742d5bd4d90d0b38eab8',
'f09b596f512fb9b65de4672e41b1ad6328d754db',
'9e41c373e5e8272a22105b8428ad8fc1bb97be2e',
'bd6ddc22358ba3570a4e62f501ee88e656e41be6',
'95f072178c3b75563cf7856f17b3c54c06858580',
'0abc62030250c0ad7007ace9668d19aa8c982a6d',
'27fa303f38b2c912af2afa864892372fd4cd9d12',
'e60b70bbe36258ec70e2ae8c259c1aa0d226d28a',
'8f88d5136bb4ee007384e769d1911cf66f61d94f',
'cc41b640e6ac201372d1e5b194b986a1582152fd',
'0a2c96320271c17ab3c0428b31736031f318293e',
'4315524e4001afbafcb11d4011bf318718abc6dc',
)
mode0 = ('report','masukin','taplove','keluarin','proses','proses','proses','proses')
mode2 = ('.','fan','unfan','report','block','unblock')
mode4 = ('.','play cast','like cast','report cast')
os.system('clear')
print(banner)
if modexxx in '1':
    print('\033[1;31m[1] \033[1;32mjoin')
    print('\033[1;31m[2] \033[1;32mlike')
    print('\033[1;31m[3] \033[1;32mout')
    print('\033[1;31m[4] \033[1;32mjoin+like')
    print('\033[1;31m[5] \033[1;32mlike+out')
    print('\033[1;31m[6] \033[1;32mjoin+out')
    print('\033[1;31m[7] \033[1;32mjoin+like+out')
    mode1 = input("\033[1;35mmasukkan pilihan mode ")
    mode = mode0[int(mode1)]
elif modexxx in '2':
    print('\033[1;31m[1] \033[1;32mfan')
    print('\033[1;31m[2] \033[1;32munfan')
    print('\033[1;31m[3] \033[1;32mreport')
    print('\033[1;31m[4] \033[1;32mblock')
    print('\033[1;31m[4] \033[1;32munblock')
    mode3 = input("\033[1;35masukkan pilihan mode: ")
    mode = mode2[int(mode3)]
elif modexxx in '3':
    print('\033[1;31m[1] \033[1;32mplay cast')
    print('\033[1;31m[2] \033[1;32munlike cast')
    print('\033[1;31m[3] \033[1;32mreport cast')
    mode5 = input("\033[1;35masukkan pilihan mode: ")
    mode = mode4[int(mode5)]
os.system('clear')
print(banner)
bot = token[int(input("\033[1;35mtotal bot 299, masukkan jumlah bot: \033[1;34m"))]
i=0
for tokens in token:
    i+=1
    try:
        headers={'User-Agent':'Mozilla/5.0','Authorization':'Token ' + str(tokens)}
        if modexxx in '1':
            if mode1 in '1':
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/join/',headers=headers)
            elif mode1 in '2':
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/like/',headers=headers)
            elif mode1 in '3':
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/leave/',headers=headers)
            elif mode1 in '4':
                response1 = requests.post('http://id-api.spooncast.net/lives/'+slink+'/join/',headers=headers)
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/like/',headers=headers)
            elif mode1 in '5':
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/like/',headers=headers)
                response1 = requests.post('http://id-api.spooncast.net/lives/'+slink+'/leave/',headers=headers)
            elif mode1 in '6':
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/join/',headers=headers)
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/leave/',headers=headers)
            elif mode1 in '7':
                response1 = requests.post('http://id-api.spooncast.net/lives/'+slink+'/join/',headers=headers)
                response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/like/',headers=headers)
                response2 = requests.post('http://id-api.spooncast.net/lives/'+slink+'/leave/',headers=headers)
        elif modexxx in '2':
            if mode3 in '1':
                response = requests.post('http://id-api.spooncast.net/users/'+slink+'/follow/',headers=headers)
            elif mode3 in '2':
                response = requests.post('http://id-api.spooncast.net/users/'+slink+'/unfollow/',headers=headers)
            elif mode3 in '3':
                response = requests.post('http://id-api.spooncast.net/users/'+slink+'/report/',headers=headers)
            elif mode3 in '4':
                response = requests.post('http://id-api.spooncast.net/users/'+slink+'/block/',headers=headers)
            elif mode3 in '5':
                response = requests.post('http://id-api.spooncast.net/users/'+slink+'/unblock/',headers=headers)
        elif modexxx in '3':
            if mode5 in '1':
                response = requests.post('http://id-api.spooncast.net/casts/'+slink+'/play/',headers=headers)
            elif mode5 in '2':
                response = requests.post('http://id-api.spooncast.net/casts/'+slink+'/like/',headers=headers)
            elif mode5 in '3':
                response = requests.post('http://id-api.spooncast.net/casts/'+slink+'/report/',headers=headers)
    except:
        print("gagal")
    if tokens == bot:
        print("\033[1;33m"+str(i)+" bot,selesai\033[0;37m")
        break
    if response.status_code == 200:
        print("\033[1;32m"+mode+" bot ke "+str(i)+" berhasil")
    elif response.status_code == 403:
        os.system('clear')
        print(banner)
        print("\033[1;33mserver sedang sibuk, tunggu 6 menit\033[0;37m")
        def run_timer(seconds):
            for remaining in range(seconds, 0, -1):
                sys.stdout.write("\r")
                minutes = 0
                seconds = remaining
                if remaining > 60:
                    minutes = int(seconds/60)
                    seconds = int(seconds%60)
                else:
                    seconds = remaining
                sys.stdout.write("\033[1;33mwaktu tunggu: {:2d} menit {:2d} detik lagi.".format(minutes,seconds)) 
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\n\033[1;34m melanjutkan\n") 
        run_timer(360)
    elif response.status_code == 401:
        print("\033[1;31mgagal token", str(tokens))
    else:
        print(response)
        print("\033[1;31m"+mode+" bot ke "+str(i)+" gagal")
