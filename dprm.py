import pandas as pd
import folium

data = pd.read_json('deprem_bilgileri (2).json')

map = folium.Map(location=[data['Enlem'].mean(), data['Boylam'].mean()], zoom_start=5)


for index, row in data.iterrows():
    popup_content = f"""
    Tarih: {row['Olus Tarihi']} <br>
    Saat: {row['Olus Zamani']} <br>
    Enlem: {row['Enlem']} <br>
    Boylam: {row['Boylam']} <br>
    Derinlik: {row['Der(km)']} km <br>
    xM: {row['xM']} <br>
    ML: {row['ML']} <br>
    Mw: {row['Mw']} <br>
    Tip: {row['Tip']} <br>
    Yer: {row['Yer']}
    """
    print(popup_content)

    folium.Marker(
        location=[row['Enlem'], row['Boylam']],
        popup=folium.Popup(popup_content, max_width=300),
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map)


map.save('deprem_haritasi.html')


