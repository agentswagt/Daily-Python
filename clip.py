import requests




print("[1] Submit")
print("[2] Read")

option = input("[!] Please Select A option: ")
if option == "1":
    text = input("Clip: ")
    text = text.replace("\n", "<br>")
    with open("clipboard.html", "w") as fp:
        fp.write(text)
        fp.close
    import os
    os.system("sh submit.sh")
elif option == "2":
    x = "https://scblog.netlify.app/clipboard.html"

    clip_b = requests.get(x)

    print(clip_b.text)
