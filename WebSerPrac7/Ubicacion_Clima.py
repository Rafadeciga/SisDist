import requests

def obtener_datos_meteorologicos(api_key, ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es"

    try:
        response = requests.get(url)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            return temperatura, condiciones_climaticas
        else:
            return None, None
    except Exception as e:
        print(f"Error al obtener datos meteorológicos: {str(e)}")
        return None, None

def obtener_informacion_ubicacion(geonames_username, lugar):
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"

    try:
        response = requests.get(url)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            nombre = ubicacion['name']
            pais = ubicacion['countryName']
            return nombre, pais
        else:
            return None, None
    except Exception as e:
        print(f"Error al obtener información de ubicación: {str(e)}")
        return None, None

if __name__ == "__main__":
    api_key = "bc6d4fd282e882eddc745d9efd6c10bd"  # tu api key de OpenWeatherMap
    geonames_username = "rafadeciga"  # tu usuario de GeoNames
    ciudad = "Santiago"  # Cambia esto a la ciudad que desees consultar

    nombre_ubicacion, pais_ubicacion = obtener_informacion_ubicacion(geonames_username, ciudad)
    if nombre_ubicacion and pais_ubicacion:
        temperatura, condiciones_climaticas = obtener_datos_meteorologicos(api_key, ciudad)
        if temperatura is not None and condiciones_climaticas is not None:
            print(f"Temperatura en {nombre_ubicacion}, {pais_ubicacion}: {temperatura:.2f}°C")
            print(f"Condiciones Climáticas en {nombre_ubicacion}, {pais_ubicacion}: {condiciones_climaticas}")
        else:
            print("No se pudieron obtener los datos meteorológicos.")
    else:
        print("No se pudo obtener la información de la ubicación.")
