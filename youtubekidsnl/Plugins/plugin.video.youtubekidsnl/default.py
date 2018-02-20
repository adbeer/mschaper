# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Kids NL
# (c) 2017 - MSCHAPER
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.youtubekidsnl'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addonID + '/resources/art/'))



channellist=[
    ("[COLOR blue]Kinderfilmpjes NL >>[/COLOR]", "Kinderfilmpjes NL", ART+'filmpjes.jpg'),
    ("[COLOR magenta]Kinderliedjes NL >>[/COLOR]", "Kinderliedjes NL", ART+'liedjes.jpg'),    
	("[COLOR green]Kinder Karaoke kanalen >>[/COLOR] ", "Kinder Karaoke kanalen", ART+'karaoke.jpg'),
    ("[COLOR orange]Youtube NL Kanalen >>[/COLOR]", "Youtube NL Kanalen", ART+'YouTube-kanaal.png'),
    ]

	
	
sublists = {
'Kinderfilmpjes NL':[
     ("Bob de Bouwer", "playlist/PLIDgZMnHTt1qhPTD7LOhf2PiUgFF5q4ZZ", "https://yt3.ggpht.com/-4vozPo5t5K0/AAAAAAAAAAI/AAAAAAAAAAA/Ju1Q-mDIAhA/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"),
     ("Bibi de Bij", "playlist/PLup781SSffsxe5r5fP9JSdc5fOSMePWLb", "https://yt3.ggpht.com/-gLXdZB97TBA/AAAAAAAAAAI/AAAAAAAAAAA/YVo9Ihq3_QU/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"),	 
     ("Brandweerman Sam", "playlist/PLS3AaYzBaR2eAlWqVqBD8DPqHR-snWQSf", "https://i.ytimg.com/vi/AjvHzNcw-q0/maxresdefault.jpg"),
	 ("Bibaboerderij", "playlist/PL_ns56fUdWZKZvA7mRusSQ49zqgDJk9Eg", "https://yt3.ggpht.com/-ZAHtA-HErRo/AAAAAAAAAAI/AAAAAAAAAAA/hjU0RK2FSRo/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"),
	 ("Bobo", "channel/UCQ3GBHmhmKwmcjjC62BjM4Q/playlists", "https://yt3.ggpht.com/-x2Fl2iqcWGs/AAAAAAAAAAI/AAAAAAAAAAA/tN9GEK38BR4/s288-c-k-no-mo-rj-c0xffffff/photo.jpg"),
	 ("Bol & Smik", "playlist/PLTVteViFsSU9BMHzwWXj16UHrWcDCYdc9", "https://yt3.ggpht.com/-wf91Mku5FfE/AAAAAAAAAAI/AAAAAAAAAAA/J3aaUlqQL1k/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"),
	 ("Bumba", "playlist/PL9S3PRwyiLReg4c8bmHPqc6IhgkrFmeh9", "https://yt3.ggpht.com/-m3GkQATOCWE/AAAAAAAAAAI/AAAAAAAAAAA/ZLxbNBoBGZ0/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"),
     ("Buurman en Buurman", "playlist/PLDd-9uTzQrpTyLy0jXAWKkNn_TajN61en", "https://i.ytimg.com/vi/JyUSVuvM7qE/hqdefault.jpg"),
	 ("De Tofu's", "playlist/PLDyfEDDq7obVDwqQTJlwpNefhfb54eajN", "http://www.mediasmarties.nl/media/uploads/producties/d/de-/De%20Tofu's.jpg"),
     ("De wereld van K3", "playlist/PLw_5zTBMF4hy3DgTeSMdUMuEUuTJg7LKS", "https://i.ytimg.com/vi/m0gbMyzckrk/maxresdefault.jpg"),
	 ("De Wielen van de Bus", "channel/UC9REV5dflUeJsC3ij87zSbQ/playlists", "https://yt3.ggpht.com/-Zee55tOc0l4/AAAAAAAAAAI/AAAAAAAAAAA/ZBxw1bSi12Q/s288-c-k-no-mo-rj-c0xffffff/photo.jpg"),
	 ("Efteling Sprookjesboom Sprookjes", "playlist/PLGJ8-PwGgVmQ0qbQI2rNenX2fa5dBTuF4", "http://i.imgur.com/JVMcRTa.jpg"),
	 ("Hallo K3", "playlist/PLw_5zTBMF4hxMfBGi5PF-RIT5KA7cmZd7", "https://i.ytimg.com/vi/U8pIGftHjgk/maxresdefault.jpg"),
	 ("Heidi", "playlist/PLGIlSVz-FsQy2UGrwFna7FpE_Fg5cJ7dZ", "https://yt3.ggpht.com/-tAIg25UbuE4/AAAAAAAAAAI/AAAAAAAAAAA/N5H_rzQ7BHM/s88-c-k-no-mo-rj-c0xffffff/photo.jpg"),
	 ("Juf Roos Afleveringen", "playlist/PLpb0mdVsIliOgxUhbxvwEEr8M1hPNCBzo", "https://i.ytimg.com/vi/coWKC95ZqNk/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBpXRw-FJlBJtglGX6qCf4tA91SQQ",),
	 ("Juf Roos Lesjes", "playlist/PLpb0mdVsIliPg0mVpbhtkhMIeABKzChAo", "https://i.ytimg.com/vi/AIMAbIZA2p8/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBqSDBUNAI2L0NrQYcWcVG6y3YBvQ",),
	 ("Jokie", "playlist/PLxGx3wMkEOuc8Ek01S9Sb9QrzHUkQzsuK", "https://yt3.ggpht.com/-er-K_KRiCRM/AAAAAAAAAAI/AAAAAAAAAAA/eIFhX8rrQ2Y/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("K3 Shows", "playlist/PLv5LxtNCw0zNPgQawDA6hskOAoS1cTxLQ", "https://i.ytimg.com/vi/DkGhMsR2An4/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDCUgupHmKXPPoP5CJ3iH4MZQTniQ",),
	 ("Kabouter Plop", "playlist/PLIWmBtraYPbf8nww-V2aGB7Sw0O0bREcG", "https://yt3.ggpht.com/--OyPBdXiuh0/AAAAAAAAAAI/AAAAAAAAAAA/AXu-gIzqZ4I/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Kikker & Vriendjes", "playlist/PLIeebRAwsaww6Jr3OuW_dmItw5VU6zIKq", "https://i.ytimg.com/vi/5tjtWFjIJqg/maxresdefault.jpg",),
	 ("Leer Tellen in het Engels met Kapitein Pudding", "playlist/PLxBVrUZUpjI2s8cLUf6ODFeAoFSADWde3", "https://i.ytimg.com/vi/24uhLX7BKws/maxresdefault.jpg",),
	 ("Ludovic", "playlist/PLoEixDOfA3k_gw6ZEmGv6tw4WLd3oBhFf", "https://i.ytimg.com/vi/4F4Ar7dA6UY/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCzdcruBGV5m5mpWuzX3xlNKM0DsQ",),
	 ("Lolly Lolbroek", "playlist/PLpQsZn5iPhzAMCWqJ0qK911sQRuuFSJYt", "https://yt3.ggpht.com/-eOaDq57wYLI/AAAAAAAAAAI/AAAAAAAAAAA/NI2bH9MahI4/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Nienke van Zappelin leest voor", "playlist/PLXf7Id-BrOwxNnfb3xGkMTGzPUiyunHYr", "https://yt3.ggpht.com/-CJTA4AUfspM/AAAAAAAAAAI/AAAAAAAAAAA/2ONhgB-umU8/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Nijntje", "playlist/PL7W9JqbVCN0Fgz1omLnuZKzX6NmaeaAFJ", "https://yt3.ggpht.com/-tGFH5niOEi8/AAAAAAAAAAI/AAAAAAAAAAA/mad1KLhKKzU/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Peppa Big Seizoen 1", "playlist/PLIeebRAwsawwuPckJLuOa7KXQ2CA5rJFJ", "https://i.ytimg.com/vi/UgA0wI1hjOk/maxresdefault.jpg",),
	 ("Peppa Big Seizoen 2", "playlist/PLIeebRAwsawzb64urCMWRZ4W7zuiz_sBI", "https://i.ytimg.com/vi/UgA0wI1hjOk/maxresdefault.jpg",),
	 ("Pororo", "playlist/PLS9i-wdw8ZyPGzE90PF0xkleWAzRQnhHg", "https://yt3.ggpht.com/-2-9l1GC2A5E/AAAAAAAAAAI/AAAAAAAAAAA/KlPw3N7acEU/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Storyzoo", "playlist/PLEOBE7_v7dNlR8CMaGGTIuXHWB25zcKta", "https://yt3.ggpht.com/-9mbXCmWGNHA/AAAAAAAAAAI/AAAAAAAAAAA/KAT61NPK6kE/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Smurfen", "playlist/PLvSQ6HKv2WcJW-y7DMCkfN1AFXFa7OKSb", "https://yt3.ggpht.com/--i8vUQ3KRSc/AAAAAAAAAAI/AAAAAAAAAAA/lljCwDfNQoM/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Teletubbies", "playlist/PLIeebRAwsawyw4GHDzErS-9sdD_vnECT_", "https://i.ytimg.com/vi/baIhR1CdLHg/maxresdefault.jpg",),
	 ("Thomas de Stoomlocomotief", "playlist/PLOaH4rwCwbRm-hkfsbZCcIOns14kiDWAP", "https://i.ytimg.com/vi/2OAlpStqmNc/maxresdefault.jpg",),
	 ("Tractor Tom", "playlist/PLdAOY_vKneiCGlfDZfPUQrRMLb4VRoZ3c", "https://yt3.ggpht.com/-TN1ih4Az918/AAAAAAAAAAI/AAAAAAAAAAA/wV9Lj-WPewg/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("TwiniPop", "playlist/PLPL7CkhLx1AuWAOCaQ06rjFCUQ6a4kwMS", "https://yt3.ggpht.com/-z8vwsuHexhc/AAAAAAAAAAI/AAAAAAAAAAA/2OxNo8dgf64/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Uki", "playlist/PL8cP9XOFMdlj4ZHL7HKUcmmv2OKPzxHLh", "https://yt3.ggpht.com/-wF_Yz1KSc7w/AAAAAAAAAAI/AAAAAAAAAAA/HGz2Xuebet4/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("WILDBRAIN NEDERLANDS PLAYLIST | CARTOONS", "playlist/PLIpTQUiq8YvrehBUAsr5-Ou-GchPpXw3j", "https://i.ytimg.com/vi/oML9C2TrKs4/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBjaHMHrZrBvoz_Wb4vwoTCS7c6rw",),
     ],
 
'Kinderliedjes NL':[
     ("Bibaboerderij Liedjes", "playlist/PL_ns56fUdWZK4KRDVn_QsdTfq23xx3Iyl", "https://yt3.ggpht.com/-ZAHtA-HErRo/AAAAAAAAAAI/AAAAAAAAAAA/hjU0RK2FSRo/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
     ("De leukste liedjes van K3", "playlist/PLw_5zTBMF4hw8fCCDmzyfMVcKaFh9IN8F", "https://www.muzieklijstjes.com/wp-content/uploads/2015/11/k3.jpg",),
     ("Efteling Jokie & Jet", "playlist/GZnaLllN_Us&list=PLxGx3wMkEOueEcIsbBf5pHmqHr8beTi73", "http://i.imgur.com/SGVsy1l.jpg"),
	 ("Efteling Sprookjesboom", "playlist/JmNmakIcOTk&list=PLGJ8-PwGgVmQv9oEhNoM2M-_Kj6HfmM7M", "http://i.imgur.com/JVMcRTa.jpg"),
	 ("Juf Roos", "playlist/PLpb0mdVsIliP-fllkQW6j3RIv8C8xWKrn", "http://i.imgur.com/fCyPI09.jpg"),
	 ("Kabouter Plop", "playlist/PLe6pJa9t9PIEi7o0uf7cUhVNY9MK2nrNi", "http://i.imgur.com/bTO5mR4.jpg"),
	 ("Kerstliedjes", "playlist/PL0Ce81PoTVxht9UA1VGOhvF4V38niMFjv", "https://i.ytimg.com/vi/GXAgl-GCoO4/maxresdefault.jpg",),
	 ("Kinderen voor Kinderen", "playlist/PLkPzEInYF3eWnpCd1XT6R_L2be_NiR0dv", "https://yt3.ggpht.com/-hLqayoCdq1g/AAAAAAAAAAI/AAAAAAAAAAA/98sw47L2_6E/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Liedjes voor peuters en kleuters", "playlist/PL0Ce81PoTVxi6nHf5IXkgchUHt-cLE4v0", "https://i.ytimg.com/vi/Dp0BfJonw5o/maxresdefault.jpg",),
	 ("Minidisco NL", "playlist/PLzDZvvekbRQ3_YbrXSbpFC5_5e1qaItyb", "https://i.ytimg.com/vi/O5B0QdCXS9w/maxresdefault.jpg",),
	 ("Nijntje Liedjes", "playlist/PL7W9JqbVCN0GTBj9_pNm9X4oLge8q5GYd", "http://i.imgur.com/f31Qinn.jpg"),
	 ("Op het kinderdagverblijf", "playlist/PL0Ce81PoTVxiSVPjLVTBZHIZpVu-slSps", "https://i.ytimg.com/vi/CoQ3XO_mfNs/maxresdefault.jpg",),
     ("Samson & Gert", "playlist/JSDJHWYtA38&list=PL3igZ4Js4cXUDZ7pDszWlvsVUSWuTCaBX", "http://i.imgur.com/JJeh9a5.jpg"),
	 ("Sinterklaasliedjes", "playlist/PLwbalUCRCXCXu0kYLfKkLumqT_Bv6vike", "https://i.ytimg.com/vi/KHGDSEoy7SU/maxresdefault.jpg",),
	 ("The voice kids", "user/thevoicekids", "https://yt3.ggpht.com/-x2qHvjgplTo/AAAAAAAAAAI/AAAAAAAAAAA/NoaU7YmDw40/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Zing en dans mee met Juf Nouk!", "playlist/PLnzjOY6ern_wAtuAahLB_E-bxt_6ojFVZ", "https://yt3.ggpht.com/-GcqNuTrNuwY/AAAAAAAAAAI/AAAAAAAAAAA/Y00DvJFunfk/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
	 ("Zingen en dansen met Nienke van Zappelin", "playlist/PLXf7Id-BrOwwDBw79sS3mG4iVoiBSSmw6", "https://yt3.ggpht.com/-CJTA4AUfspM/AAAAAAAAAAI/AAAAAAAAAAA/2ONhgB-umU8/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",),
     ],

'Youtube NL Kanalen':[
     ("Amika", "user/AmikaKanaal", "http://i.imgur.com/XRNctz8.jpg"),
	 ("Bassie en Adriaan", "user/bassieadriaanchannel", "http://i.imgur.com/REyFIga.jpg"),
	 ("De Smurfen", "channel/UCeR6gZ7LpF-DB-d0clvwY4w", "http://i.imgur.com/wHGEfVH.jpg"),
	 ("Disney XD", "channel/UCh8JtgfHLUhW08yyQOD493A", "http://i.imgur.com/zS1K0pE.jpg"),
	 ("Efteling Raveleijn", "user/Raveleijn", "http://i.imgur.com/2kuMsEf.jpg"),
     ("Galaxy Park", "user/GalaxyParkKanaal", "http://i.imgur.com/Fzh5SOj.jpg"),
	 ("Heidi", "user/HeidiKanaal", "http://i.imgur.com/wX7N9kJ.jpg"),
     ("Mega Mindy", "user/MegaMindyKanaal", "http://i.imgur.com/dQ8EQn2.jpg"),
	 ("National Geographic Junior", "playlist/PL16F97188D646E450", "http://i.imgur.com/KebLOpC.jpg"),
	 ("Nickelodeon", "channel/UCTfMaiRjr3goFg_Iqie2I8g", "http://i.imgur.com/jyKAVp7.jpg"),
	 ("Oggy", "channel/UCNEKMkg_DG8eAyR1BNWsSvw", "http://i.imgur.com/fBLojgW.jpg"),
	 ("Prinsessia", "user/prinsessiatv", "http://i.imgur.com/Ou2MNZo.jpg"),
	 ("Rox", "user/RoxKanaal", "http://i.imgur.com/ftquvWd.jpg"),
	 ("Super Sportlets", "playlist/PLYAskUYrLf4Xapuncsobk11V1T8KylIVM", "http://i.imgur.com/nqz6d9m.jpg"),
     ("Tita Tovernaar", "user/Titatovenaar", "http://i.imgur.com/nQSmo7I.jpg"),
	 ("Walt Disney Studios Nederland", "user/WaltDisneyStudiosNL", "http://i.imgur.com/Ui0lVz5.jpg"),
	 ("Wickie de Viking", "user/WickieKanaal", "http://i.imgur.com/keHTmKj.jpg"),
	 ("Winx Club", "user/WinxClubNL1", "http://i.imgur.com/IHnpuWU.jpg"),
     ],

'Kinder Karaoke kanalen':[
     ("Kinderliedjes Nederlands", "playlist/PLCm89dwWipl32ORkcPIuznNWarBJEnLxF", "http://www.finesound.nl/verkoop/images/Web_kinder_karaoke_dvd_shop_winkel_Fine_sound.jpg",),
     ("Liedjes Nederlands 1", "playlist/PLxbCc28H2cRqF0hTHK73r60kTNvgED4Tq", "http://www.finesound.nl/verkoop/images/Web_kinder_karaoke_dvd_shop_winkel_Fine_sound.jpg",),
	 ("Liedjes Nederlands 2", "playlist/PL6E37C4391BBB924B", "http://www.finesound.nl/verkoop/images/Web_kinder_karaoke_dvd_shop_winkel_Fine_sound.jpg",),
	 ],
	 
    }



# Entry point
def run():
    plugintools.log("kidstime.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        sub_list(action)
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("kidstime.main_list "+repr(params))

    for name, id, icon in channellist:
        url = sys.argv[0] + "?action=" + id
        plugintools.add_item(title=name,url=url,thumbnail=icon,folder=True )

def sub_list(action):
    plugintools.log("kidstime.sub_list "+repr(action))
    for List in sublists[str(action)]:
        name = List[0]
        id = List[1]
        icon = List[2]
        plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )        

run()