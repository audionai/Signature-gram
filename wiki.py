import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    t = {"name": ["Elon Musk",
                  "Bill Gates",
                  "Mark Zuckerburg",
                  "Rihanna",
                  "Shakira",
                  "Jennifer Lopez",
                  "Ariana Grande",
                  "Drake",
                  "The Weeknd",
                  "Nicki Minaj",
                  "Cardi B",
                  "Taylor Swift",
                  "Dwayne Johnson",
                  ""
                  ],
          "url": ["//upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Elon_Musk_Royal_Society_crop.jpg/220px-Elon_Musk_Royal_Society_crop.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Bill_Gates%2C_September_2024.jpg/220px-Bill_Gates%2C_September_2024.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/1/18/Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg/220px-Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/d/de/Rihanna_Fenty_2024_02.jpg/220px-Rihanna_Fenty_2024_02.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2023-11-16_Gala_de_los_Latin_Grammy%2C_03_%28cropped%2902.jpg/220px-2023-11-16_Gala_de_los_Latin_Grammy%2C_03_%28cropped%2902.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/6/68/Jennifer_Lopez_Interview_2019_%28cropped%29.jpg/220px-Jennifer_Lopez_Interview_2019_%28cropped%29.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/6/69/Ariana_Grande_at_the_Met_Gala_2024_%281%29.jpg/220px-Ariana_Grande_at_the_Met_Gala_2024_%281%29.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/2/28/Drake_July_2016.jpg/220px-Drake_July_2016.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/9/95/The_Weeknd_Cannes_2023.png/220px-The_Weeknd_Cannes_2023.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Nicki_Minaj_Barbie_Premiere_2023_%28cropped%29.png/220px-Nicki_Minaj_Barbie_Premiere_2023_%28cropped%29.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Cardi_B_2021_02.jpg/220px-Cardi_B_2021_02.jpg",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Taylor_Swift_at_the_2023_MTV_Video_Music_Awards_%283%29.png/220px-Taylor_Swift_at_the_2023_MTV_Video_Music_Awards_%283%29.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Dwayne_%22The_Rock%22_Johnson_Visits_the_Pentagon_%2841%29_%28cropped%29.jpg/220px-Dwayne_%22The_Rock%22_Johnson_Visits_the_Pentagon_%2841%29_%28cropped%29.jpg",
                  ""],
           "si": ["//upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Elon_Musk_Signature.svg/150px-Elon_Musk_Signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/3/34/Bill_Gates_signature.svg/150px-Bill_Gates_signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mark_Zuckerberg_Signature.svg/150px-Mark_Zuckerberg_Signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Rihanna-signature.svg/150px-Rihanna-signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Shakira_signature%2C_Billboard_Open_Letter_2016.png/150px-Shakira_signature%2C_Billboard_Open_Letter_2016.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/7/75/Jennifer_Lopez_Signature.svg/150px-Jennifer_Lopez_Signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Ariana_Grande_autograph.svg/150px-Ariana_Grande_autograph.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Drake_sig.png/150px-Drake_sig.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/d/d0/The_Weeknd_signature.svg/40px-The_Weeknd_signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Nicki_Minaj_sig.png/150px-Nicki_Minaj_sig.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Cardi_B_sig.png/150px-Cardi_B_sig.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Taylor_Swift_signature.svg/150px-Taylor_Swift_signature.svg.png",
                  "//upload.wikimedia.org/wikipedia/commons/thumb/1/1e/DwayneTheRockJohnson2.svg/150px-DwayneTheRockJohnson2.svg.png",
                  ""],
            }
    nanv = t["name"]
    url = t["url"]
    si = t["si"]
    na = len(nanv)
    username = ""
    user_p =      ""
    user=         ""
    usersi = ""
    # for m in t:
    #     re = requests.get(f"https://en.wikipedia.org/wiki/{m}")
    #     resp = re.text
    #     tx = BeautifulSoup(resp, "html.parser")
    #     username = tx.find(name="span",class_="mw-pag-title-main")
    #     user_ = tx.find(name="span", class_="infobox-signature skin-invert")
    #     user = user_.find(name="img",class_="ml-file-element")
    #     user_p = tx.find(name="span", class_="mw-default-size")
    #     user_p = user_p.find(name="img", class_="mw-file-element")
    #     username = username.text
    #     user_p = user_p.get("src")
    #     user = user.get("src")
    #     return user, user_p, username
    name = ""
    abo = ""
    img_ = None
    if request.method == "POST":
        api = request.form.get("name")
        api = api.strip()
        api = api.capitalize()
        try:
            api = api.split()
            api = api[0] + '_' + api[1]
        except IndexError:
            # api = api.split()
            try:
                api = api[0]
            except IndexError:
                api = "Not found"
        # else :
        #     api = api
        response  =requests.get(f"https://en.wikipedia.org/wiki/{api}")
        res = response.text
        txt = BeautifulSoup(res, "html.parser")
        name = txt.find(name="span", class_="mw-page-title-main")
        try:
            nam = txt.find_all(name="span", class_="skin-invert")
        except:
            nam = txt.find_all(name="span", class_="skin-invert")
        # try:
        abo = nam[1].find(name="img", class_="mw-file-element").get("src") if nam else None
        # except:
            # abo = nam[].find(name="img", class_="mw-file-element").get("src") if nam else None
        img = txt.find(name="span", class_="mw-default-size")
        iml = img.find(name="img", class_="mw-file-element").get("src") if img else None
        name = name.text  if name else None
        iml = img.find(name="img", class_="mw-file-element") if img else None
        img_ = iml["src"] if iml and hasattr(iml, "attrs") and "src" in iml.attrs else None

    # print(name.text)
    
    return render_template("index.html", namem=name, ab=abo, image=img_, nam=nanv, url=url, sip=si, na=na)

if __name__ == '__main__':
    app.run(debug=True)