import pytube




video_list = []


print("""




_____.___.              __       ___.           
\__  |   | ____  __ ___/  |_ __ _\_ |__   ____  
 /   |   |/  _ \|  |  \   __\  |  \ __ \_/ __ \ 
 \____   (  <_> )  |  /|  | |  |  / \_\ \  ___/ 
 / ______|\____/|____/ |__| |____/|___  /\___  >
 \/                                   \/     \/ 


________                            .__                       .___                
\______ \    ____  __  _  __  ____  |  |    ____  _____     __| _/  ____  _______ 
 |    |  \  /  _ \ \ \/ \/ / /    \ |  |   /  _ \ \__  \   / __ | _/ __ \ \_  __ \
 |    `   \(  <_> ) \     / |   |  \|  |__(  <_> ) / __ \_/ /_/ | \  ___/  |  | \/
/_______  / \____/   \/\_/  |___|  /|____/ \____/ (____  /\____ |  \___  > |__|   
        \/                       \/                    \/      \/      \/         







	""")

print("______")
print("|infos|___________________________________________________________")
print("|                                                                |")
print("| Passer à la ligne après chaque URLs                            |")
print("|----------------------------------------------------------------|")
print("| Pour valider l'ensemble de vos ajouts terminer par 'start'     |")
print("|________________________________________________________________|\n\n")

print("#######################################\n")
print("Entrer les URLs de vidéo Youtube\n")
print("#######################################\n")

while True:
	url = input("")
	if url == 'start':
		break
	video_list.append(url)



for x, video in enumerate(video_list):

	v = pytube.YouTube(video)

	stream = v.streams.get_by_itag(22)
	print("################################\n")
	print(f"Téléchargement en cours vidéo {x}...")
	print("\n################################")
	stream.download()
	print("##################################")
	print("Terminé")
	print("################################\n")
	
	













