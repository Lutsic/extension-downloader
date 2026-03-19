#https://chromewebstore.google.com/detail/boxel-rebound/iginnfkhmmfhlkagcmpgofnjhanpmklb?hl=ru&utm_source=ext_sidebar
while True:
   ext_link = input("Extension link: ")
   print(ext_link.split("/"))
   ext_sep1 = ext_link.split("/")
   ext_sep2 = ext_sep1[-1]
   ext_sep3 = ext_sep2.split("?")
   ext_id = ext_sep3[0]
   print("https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3D", ext_id, "%26installsource%3Dondemand%26uc", sep="")