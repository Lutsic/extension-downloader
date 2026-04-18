import json
import requests
import xml.etree.ElementTree as ET
import time
import os
import pyperclip
from urllib.parse import urlparse, parse_qs

extensions = {"1":["boxel_rebound", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Diginnfkhmmfhlkagcmpgofnjhanpmklb%26installsource%3Dondemand%26uc"], "2":["vpn_turbo", "https://clients2.go ogle.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dbnlofglpdlboacepdieejiecfbfpmhlb%26installsource%3Dondemand%26uc"], "3":["ublock_origin_lite", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dddkjiahejlhfcafbddmgiahcphecmpfh%26installsource%3Dondemand%26uc"], "4":["boxel_rebound", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Diginnfkhmmfhlkagcmpgofnjhanpmklb%26installsource%3Dondemand%26uc"], "5":["boxel_3d", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dmjjgmlmpeaikcaajghilhnioimmaibon%26installsource%3Dondemand%26uc"], "6":["boxel_golf", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dmmgjkfjlmdkmoipndaeombfnomjfgeff%26installsource%3Dondemand%26uc"], "7":["helix_jump_fruit", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Djhegmncopobmnnmcdaobcepcamekoomb%26installsource%3Dondemand%26uc"], "8":["level_maze", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Djbnboceikbdhfinjlebidbhhlplagahc%26installsource%3Dondemand%26uc"], "9":["stacker", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dbnchicpgbdgahiecgofdabidjihblaff%26installsource%3Dondemand%26uc"], "10":["trixel", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dkfemlcmefehdnnnfjplhckdndgaglnhc%26installsource%3Dondemand%26uc"], "11":["table_tennis", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Diibmocmonpccjkjpdgngimgdgpaeheje%26installsource%3Dondemand%26uc"], "12":["table_tennis_workout", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dgkahkdehbcjlbdnbjcgndhakhdaogjoa%26installsource%3Dondemand%26uc"], "13":["tiny_tycoon", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dbamdkjfjhhnjcgcjmmjdnncpglihepoi%26installsource%3Dondemand%26uc"], "14":["arcade_classics", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dgokcmhknbfbkchaljcbjloaebnoblcnd%26installsource%3Dondemand%26uc"], "15":["watermelon_game", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Djoginlggdlgfofmhnfbebafafbmddbpe%26installsource%3Dondemand%26uc"], "16":["ultimate_car_driving", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Daomkpefnllinimbhddlfhelelngakbbn%26installsource%3Dondemand%26uc"], "17":["toy_car_driving", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dlkkhkpnodkflpecmnbkaceebgejjfhhl%26installsource%3Dondemand%26uc"], "18":["game_2048", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dijkmjnaahlnmdjjlbhbjbhlnmadmmlgg%26installsource%3Dondemand%26uc"], "19":["vpn_turbo", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dbnlofglpdlboacepdieejiecfbfpmhlb%26installsource%3Dondemand%26uc"], "20":["vpn_veepn", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dmajdfhpaihoncoakbjgbdhglocklcgno%26installsource%3Dondemand%26uc"], "21":["vpn_browsec", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Domghfjlpggmjjaagoclmmobgdodcjboh%26installsource%3Dondemand%26uc"], "22":["vpn_proton", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Djplgfhpmjnbigmhklmmbgecoobifkmpa%26installsource%3Dondemand%26uc"], "23":["ublock_origin_lite", "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3Dddkjiahejlhfcafbddmgiahcphecmpfh%26installsource%3Dondemand%26uc"]}


while True:
    print("\nVersion: 1.4.0", "\nYou can enter q anytime to return to main menu. \nChoose mode: \n", "1 - Download from featured extensions (21 extensions) \n", "2 - Download by webstore link\n", "3 - Extension parsing (txt output) \n", "4 - Create a data.js file from txt\n")
    mode = 0
    while mode == 0:
        try: 
            mode = int(input())
        except ValueError:
            print("Invalid mode selection! Try again.\n")

    if mode == 1:
        print("\n", " ◈Recommended◈ \n", "1 - Boxel Rebound \n", "2 - TurboVPN \n", "3 - UBlockOrigin Lite \n", " ◈Games◈ \n", "4 - Boxel Rebound \n", "5 - Boxel 3D \n", "6 - Boxel Golf \n", "7 - Helix Fruit Jump \n", "8 - Maze \n", "9 - Stacker (Tetris-like) \n", "10 - Trixel (Tetris-like) \n", "11 - Table Tennis (Ping-pong) \n", "12 - Table Tennis Workout (Solo ping-pong) \n", "13 - Tiny Tycoon \n", "14 - Arcade Classics \n", "15 - Watermelon Game \n", "16 - Ultimate Car Driving Game \n", "17 - Toy Car Driving Game \n", "18 - 2048 \n", " ◈VPNs◈ \n", "19 - TurboVPN \n", "20 - VeePN \n", "21 - BrowsecVPN \n", "22 - ProtonVPN \n", " ◈Utilities◈ \n", "23 - UBlockOrigin Lite \n",)
        while True:
            ext_sel = -1
            while ext_sel == -1:
                try:
                    ext_sel = str(input())
                    if ext_sel == "q":
                        break
                    else:
                        print("\n", extensions[ext_sel][1])
                        pyperclip.copy(extensions[ext_sel][1])
                        print("\nLink succesfully copied to clipboard!\n")
                except KeyError:
                    print("Invalid selection! Try again.\n")
            if ext_sel == "q":
                break

    if mode == 2:
        while True:
            ext_link = input("\nExtension link: ")
            if ext_link == "q":
                break
            ext_sep1 = ext_link.split("/")
            ext_sep2 = ext_sep1[-1]
            ext_sep3 = ext_sep2.split("?")
            ext_id = ext_sep3[0]
            print("\nhttps://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3D", ext_id, "%26installsource%3Dondemand%26uc", sep="")
            pyperclip.copy(f"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3D{ext_id}%26installsource%3Dondemand%26uc")
            print("\nLink succesfully copied to clipboard!")


    if mode == 3:
        def generate_crx_url(extension_id):
            base_url = "https://clients2.google.com/service/update2/crx"
            params = {
                "response": "redirect",
                "prodversion": "122.0",
                "acceptformat": "crx2,crx3",
                "x": f"id%3D{extension_id}%26installsource%3Dondemand%26uc"
            }
            query_string = "&".join([f"{k}={v}" for k, v in params.items()])
            return f"{base_url}?{query_string}"

        output_file = "extensions.txt"
        extensions = set()

        for shard in range(28):
            sitemap_url = f"https://chromewebstore.google.com/sitemap?shard={shard}"
            try:
                response = requests.get(sitemap_url)
                if response.status_code != 200:
                    raise Exception(f"HTTP error {response.status_code}")
                xml_content = response.content

                root = ET.fromstring(xml_content)
                namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

                for url in root.findall('ns:url', namespace):
                    loc = url.find('ns:loc', namespace)
                    if loc is not None and '/detail/' in loc.text:
                        path_parts = loc.text.split('/detail/')
                        if len(path_parts) == 2:
                            detail_part = path_parts[1]
                            slug_id = detail_part.split('/')
                            if len(slug_id) == 2:
                                slug, ext_id = slug_id
                                name = slug.replace('-', '_')
                                crx_url = generate_crx_url(ext_id)
                                extensions.add(f'{name} = "{crx_url}"')

                print(f"Processed shard {shard} successfully. Current extensions count: {len(extensions)}")
                time.sleep(0.5)

            except Exception as e:
                print(f"Error processing shard {shard}: {str(e)}")

        full_path = output_file
        print(f"Total extensions found: {len(extensions)}")
        print(f"Writing to file: {full_path}")
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in sorted(extensions):
                f.write(line + '\n')

        print(f"Extensions written to {output_file}.")

    if mode == 4:
        inp = "extensions.txt"
        out = "data.js"
        data = {}
        with open(inp, "r", encoding="utf-8") as f:
            for line in f:
                i = line.find("=")
                if i == -1:
                    continue
                name = line[:i].strip()
                url = line[i+1:].strip().strip('"')
                data[name] = url
        with open(out, "w", encoding="utf-8") as f:
            f.write("const DATA = ")
            json.dump(data, f, separators=(",",":"))
            f.write(";")
        print("done:", len(data))
