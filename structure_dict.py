bd = {
    "artistes": [
        {
            "Nom": "Michael Jackson",
            "Albums": [
                {"Nom": "Bad", "Titres": [{"Nom": "Bad"}, {"Nom": "Smooth Criminal"}]}
            ],
        }
    ]
}

bd["artistes"].append({
            "Nom": "AC/DC",
            "Albums": [
                {"Nom": "Thunderstruck", "Titres": [{"Nom": "Thunderstruck"}, {"Nom": "Hell's Bells"}]}
            ],
        })

for artist in bd["artistes"]:
    for album in artist["Albums"]:
        print(album["Nom"])
        for titre in album["Titres"]:
            print("     - " + titre["Nom"])