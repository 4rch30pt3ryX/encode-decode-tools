#!usr/bin/env python

import os
from colorama import init, Fore, Back, Style
from termcolor import colored

os.system('mode con: cols=100 lines=50')

signage = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:@@@@@@@,@:**,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@,@,S++.,..*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@*+.,:S,.:..,.S%%.?%.%.SSS+:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.S:.%S%?.??.%+.%%?%?#.SS.+.+:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:S+%S%%?%.?#%%.+??%.S.?#??.S.*@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.**+%%%%?.S??%%S??%S+??%%.S.S..%S,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*+S%..?%%.##%.#?%?%%??%.%%.%?%?%?%.S.@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*+%%%?#%?%%S?%%??.S..%%%%%%%.?%%+..+S.+S,@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+S?.?????#?%%..%+.+.::..%##?%%?.%%...S*@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,::%#%%??%%%.+S,,.::::*,,,,+?....%????%%.S*@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,S%.S.%??...::,@,:,,:,,,,,*,:%###?%%??.:%:..,@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*..++SS%...,*@,,@,@@,,,,.%%.*S.?????????%.S.:,@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@:*,**.+.+%.+*,:,,,::,::,:,,@@@,@S?..??....??%.S+..:@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::::::*.S%?.+,,,.,*:***,@::,@,@@@@,S.%%.%%.%S....%.::,@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,::::::,,,:*.S..%::,:*S.*,,*:*,:,,,@@,,*:S**+%.%%????.:,@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@,*:****:::,::*.+SSS..*@:S..:*..%*.*:*.*:,@@,,,,::,:.%%?##??%+:,@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@,*......*...*:,::***.+++++..+,+*:#?S%?.S+.,**:.::,@@@,:::S.%+?#?????%%%.:@@@@@@@@@@@@@@@@
@@@@@@@*::***....*..****:..+..++++S.S.S.+.?.S..%?%%+.:*:,@@***:*.+%.%???????????%.SS@@@@@@@@@@@@@@@
@@@@@*.**.+...++...***..........+S..%.:*+.%..#%.%?.S*:*::,:**:*::,,*....####?.S:,:,@@@@@@@@@@@@@@@@
@@@@:*+S%??*.+.*.....*..*.....*.+SS...:@.%%####S%?%.*..+.****,,,,::::*+.????##?##??S@@@@@@@@@@@@@@@
@@@::*...+++++.+.+..**...***::*..+S.?..*.:??##%S.?%.**:,,,,**:,:..*.++SS??.#?%??????%+*,@@@@@@@@@@@
@@@*.+S++++..++*..:*************.+S%%S.++SS%%%%.%++.+*:*...*::*:,,@@@,,@,,,+%#???????%S.@@@@@@@@@@@
@@:+++.+++...**.....********.*.*.+S.%%?.*...%%%%..%S.**..++::,,,,:::,,::..%######???%???%.:@@@@@@@@
@@.SSS++........+*.******..*...*.+S.%%%.*+S?.+S%+%...***:::*%S+S:::,::::,.%%%%%?%???#?%%SS,*@@@@@@@
@@+%...S+++++++.+:**.***....+.*.++S.%??%**+.S..%.%+**+...*.*+.#?..*..**:.+.S?#######???%**@@@@@@@@@
@@@.?%%..SS+++S.+....***.....**.++S...?%.:.+S%.+....*...+.+%.??##..+..::*:*S?###?######???%+::@@@@@
@@@S@.@S%....%SSS.+...**.*.*::...+++SS?%?S:*..+*..*.++*..*++???####?.*.::.*:*..S?????#####????+:,,@
@@@@@+@*+,*.:%%.SSS+.+...*.**..**...*.+???....+.+.*S.***.**..**S%#????.+:,,,*:.%?###??????#??%..:,@
@@@@@@@@@@@%@@.@%%SS+++.....**..**...+..??##?%..???#???%?.%%++S+S.,.S?##%**++.**%?#########???%.+::
@@@@@@@@@@@@@@.@S@,*.%.S+*++.......*.++..%.?#??#########?####%.SS++S.SS?#%+S..***..S.??##???????%%S
@@@@@@@@@@@@@@@@@@,@++,S?SSS++.......++SS.%%#####%#%?##??#####%%S.+....*+S.#%%.**..?######?#???#?.*
@@@@@@@@@@@@@@@@@@@@@S:@@*S##%.S+..+...+S..%.%?#??.%%..?%?%.####.%.+*.****:?###?+.+*+?##????%?#####
@@@@@@@@@@@@@@@@@@@@@@@@@.@@@@@@@@...+.++.S..%S?.#?S**S.++...?#??S?S+.*::...*.%?#SSSS+???%?#?######
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.SS+.+..SS+S%?%*++..**::*S?##.#.S+*....*...?##?....#########??
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%?%+SSSSS???S#%%%S.**:*+%#??#S#%*S**..*.+?###.S%??#########
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,S%?..S...S.%%??????.**+S.S.?##%.S..***++SS%####?.%###????
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.?.?...??######?#?:%?+.+++S%#+#?.S**++.S...##.%????????
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+S%S:%%.?+.%%?????%%###SS+.S.#?###%...S.%.S???####?????#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:SS.+%%%.%?????%?###?###S..S...####?##+.....%.?#########
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+S*.+%.%?#?######??#?#####????.?#######?S#.%+++.%?###???
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*S...+.%????#?#??%?#%.%.%??#??###?###?########?++SSS%??#?#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+%?++.+S.%%..%?####%++???+..%.##########??#####??#??%%????%?
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..*.+++++..S%+.%??###?#?%???S+%%%?##########?##??#########????
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*S...+....S.S%SS.%??#?#####%?##?*.%?%?#########%??#??####????###
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++S:++:**.SSSSSS+.?%??###########.%#%?#%?#########.?########??###
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:*.++..S*:**.++S..S..%%%??################?##?########?%%#####?###?##
@@@@@@@@@@@@@@@@@@@@@@@@@@,:.++SS%%*+:***++SS...%%%?%??#############################?...?####?#####
@@@@@@@@@@@@@@@@@@@@@@@@,.+S.%%%%%.+.:*++++S.S%%?????????%##########################%?SS.?#########
@@@@@@@@@@@@@@@@@@@@@@@++++.+...S.****+S+++S..%????##?????###########################..SSS%?#######
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,+S**...++++SS.%%????%.S..????###########################.%.+++#####?#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:**.**++S++SS.%??%%%+SSS.S%%%#?###########################%.%++S%??###
@@@@@@@@@@@@@@@@@@@@@@@@@@:@@*....+S+++S.%??%%S@@@@@@@@,+S:S..%??%#%S..??%##############?%S++SS%?##
@@@@@@@@@@@@@@@@@@@@@@@@@@@.....++SSSS.%%??..@@@@@@@@@@@@,.@,:@@S.**.:*,,.%?.??####?#######%S.SSS.?
@@@@@@@@@@@@@@@@@@@@@@@@@@@S...++SS...%%%%.@@@@@@@@@@@@@@@@@@@,@@@*,@@,@@@,S.%??############++....S
@@@@@@@@@@@@@@@@@@@@@@@@.++.+.+SS..%%%%%%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+####?########%?#?%?
@@@@@@@@@@@@@@@@@@@@@@*:++++++SS..%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.:%##??########??#??
@@@@@@@@@@@@@@@@@@@@@S+S+.S+SSS.%??%.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:,.????##?#########
@@@@@@@@@@@@@@@@@@@@.*SSSSSSS.%%??.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@,.,.?????#######
@@@@@@@@@@@@@@@@@@@+....SSS+.%??.:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@*@*.%.########
@@@@@@@@@@@@@@@@@,@%?%.SSSS%??%*@@@@@@@@@@@:.                           .;@@@@@@@@@@@,@,@*,S?######
@@@@@@@@@@@@@@@,@.%%%%SSS%%?%.@@@@@@@@@@@@@:.   Conversion Repository   .:@@@@@@@@@,@@@@@@,@,.?#?##
@@@@@@@@@@@@@@@.S%%%.S..??%+@@@@@@@@@@@@@@@:.                           .:@@@@@@@@@@@@@@@@@@@@..+%?
@@@@@@@@@@@@@S@???%..%%?#.@@@@@@@@@@@@@@@@@:.                           .;@@@@@@@@@@@@@@@@@@@@@@.S.
@@@@@@@@@@@@@?.?#???%?#%,@@@@@@@@@@@@@@@@@@:.           By:             .:@@@@@@@@@@@@@@@@@@@@@@@@*
@@@@@@@@@@@@@.????%???*@@@@@@@@@@@@@@@@@@@@:..                         ..:@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%..%?%@@@@@@@@@@@@@@@@@@@@@@:.............................;@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@ @@@@@@@@@@@@@@*  @@@@@@@@ @@@@@@@**@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@+    @@     ,@@@@
@@@@@@@@@  @@@@@@@@@@@@@@   @@@@@@     @@@* .  @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@. @@@@+ @@@@@@@
@@@@@@@@*  @@@@@@@@@@@@@@@ @@@@@@@ @@  @@@ ,@@  @@@@@@@@@@@@@@@@@@@ *@@@@@@@@@@@@@@@@. @@@ @@@@@@@@
@@@@@@@@   @@@@@@@@@@@@@@@ @@@@@@@@@@  @@+ @@@: *@@@@@@@@@@*@@@@@@@ ,@@@@@@@@@@@@@@@@@. @ ,@@@@@@@@
@@@@@@@ .  @@@  @@@@@@@@@@ @@@@@@@@@@ @@@  @@@@  @@+@@@@@@  @@@@@@: @@@@:@@@@@@@@@@@@@+ : @@@@@@@@@
@@@@@@  @  @@     @@    @@     @@@@@  :@@  @@@@  S      @     @@@:  @@.     @+  @:  @@@   @@@@@@@@@
@@@@@  @@  @@@  @ @  @@ @@ @@@ @@@@@@   @  @@@@  @  @@  @@  @@@@@@,  @@, ,@ @@: @* @@@@ : @@@@@@@@@
@@@@@       @@  @@@ @@@@@@ @@@ @@@@@@@  @  @@@@ .@  @@@  @  @@@@@@@, @@, @@@@@$ @ @@@@ ,@  @@@@@@@@
@@@@@@@@@  @@@  @@@ @@@@@@ @@@ @@  @@@  @  @@@@ ,@  @@@ ,@  @@@ @@@@ @@, @@@@@@ * @@@ .@@, ,@@@@@@@
@@@@@@@@@  @@@  @@@  @@@@@ @@@ @@ +@@@ ,@@  @@  @@  @@@ @@  @@@ @@@  @@, @@@@@@  ,@@ .@@@@  @@@@@@@
@@@@@@@*    @    *@@    @  *@  *@*     @@@,    @@@     @@@    @     @@@   *@@@@  @@.  @@@@.   $@@@@
@@@@@@@@@@@,@@@@@@@@@@,@@@@@@@@@@@@,@@@@@@@@@@@@@@  @@@@@@@,@@@@@,@@@@@@@@@@@@@ @@@@@@@@@@@@@,@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@
@@@@@$..                                     ..$@@  @@$..                ..$@@+ @@$..        ..$@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@

"""
print colored(signage, 'magenta')