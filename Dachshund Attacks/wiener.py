import owiener

e = 80879202244646020072460903311471663567017331730768624331442206670944598953045814205147283319931301186403639641631375753807896605323887320455024819581152635006478804128653845875734759259066049732160406030763698696957240871301336400377201122119345547627567853636531068394832612379289560351381716939408892883047

n = 103793860742805942679250081387943173952720682080587275718172960340821643825394868637933473077865333565986083596732549763954102984726139583045200792888072947036763986421794818221143430771596726034515782709367880779391292957988994012573333830283032317301149719459173969514909080634367016240545103469059124110691

d = 21322045494154294428775871059654090667971578031638874806796736618147543232087

c = 77534131540902263432606799696039557244838636027649921385374505825318043629986101536070579409955812648799802765913422280370655039451455782673779740046222173451961203737836386987255494249184484077292879027784385080707023445666055141030999561940490277674075108098029628256775466637925941121319585612803686694381

#Untuk mendapatkan teks hex (ketika nilai d sudah diketahui)
#print(hex(pow(c,d,n)))

#Untuk mendapatkan nilai d
#d = owiener.attack(e, n)

#if d is None:
#   print("Failed")
#else:
#   print("Hacked d={}".format(d))
    