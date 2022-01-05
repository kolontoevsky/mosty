import folium
import base64
from folium import IFrame
from folium import plugins
from cv2 import cv2
from folium.plugins import MarkerCluster

m = folium.Map(location=[55.7644348, 37.592083], zoom_start=11, tiles = "CartoDB dark_matter")

location = [[55.734134673944716, 37.59868901263204], [55.743623776929255, 37.60841614942666], [55.77633990588869, 37.44312923438722], [55.82862303675761, 37.654981431760426], [55.71384675144925, 37.57757633237106], [55.61649246751481, 37.68075343252131], [55.745894350392284, 37.63051521634395]]
slova = ['Крымский мост', 'Патриарший мост', 'Живописный мост', 'Ростокинский акведук', 'Андреевский железнодорожный мост', 'Фигурный мост', 'Садовнический мост']
phot = ['/Users/eugeneadylin/Desktop/telegramitembot/database/photo/42454dab42342717d6f2873d1268c8e7.jpg', '/Users/eugeneadylin/Desktop/telegramitembot/database/photo/patriarshii-most2.jpg', '/Users/eugeneadylin/Desktop/telegramitembot/database/photo/4.jpg', '/Users/eugeneadylin/Desktop/telegramitembot/database/photo/Akveduk2.jpg', '/Users/eugeneadylin/Desktop/telegramitembot/database/photo/831302_64.jpg', '/Users/eugeneadylin/Desktop/telegramitembot/database/photo/caption.jpg', '/Users/eugeneadylin/Desktop/telegramitembot/database/photo/698c1105f0ab4e88869801178dfe0a15.max-1200x800.jpg']
photo = []
for i in range(0, len(phot)):
    img = cv2.imread(phot[i])
    image = cv2.resize(img, (img.shape[1]//(img.shape[0]//200), 200))
    path = 'image'+str(i)+'.jpg'
    cv2.imwrite(path, image)

    photo.append(path)
print(photo)
for i in range(0, len(slova)):
    html1 = '''<html>
                    <head>
                        <meta charset = "UTF-8">
                        <title>dog</title>
                        <link rel = "stylesheet" href = "https://cdn.jsdelivr.net/npm/boxicons@latest/css/boxicons.min.css">
                        <link rel = "stylesheet" href = "style.css">
                    </head>
                    <body>
                        <table>
                            <tr>
                                <td style="text-align: left" height="10">''' + slova[i] + '''</td>
                            </tr>
                            <tr>  
                                 <td style="text-align: center" colspan="2"><img src="data:''' + photo[i] + ''';base64,{}" alt="HTML5"<br></td>
                            </tr>
                        </table>
    
                    </body>
                 </html>'''
    html2 = html1.format
    # img = cv2.imread(photo)
    # img = cv2.resize(img, (10, 5))

    encoded = base64.b64encode(open(photo[i], 'rb').read())
    iframe = IFrame(html2(encoded.decode('UTF-8')), width=320, height=260)
    popup = folium.Popup(iframe, max_width=2650)
    icon = folium.Icon(color="red", icon="ok")
    marker_cluster = MarkerCluster().add_to(m)
    marker = folium.CircleMarker(radius=9, location=location[i], fill_color='orange', color='black', popup=popup, icon=icon, fill_opacity = 0.9).add_to(marker_cluster)

# # миникарта
minimap = plugins.MiniMap(toggle_display=True)
m.add_child(minimap)
plugins.ScrollZoomToggler().add_to(m)
plugins.Fullscreen(position='topright').add_to(m)
# # миникарта


m.save("mostymsc.html")
