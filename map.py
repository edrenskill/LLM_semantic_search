import googlemaps
from datetime import datetime
from googlemaps.exceptions import ApiError

def get_directions(api_key, origin, destination):
    gmaps = googlemaps.Client(key=api_key)
    try:
        directions = gmaps.directions(origin, destination, mode="transit", departure_time=datetime.now())
    except ApiError as e:
        return None

    if not directions:
        return None

    direction_sentence = "To get from {} to {}, ".format(directions[0]['legs'][0]['start_address'], directions[0]['legs'][0]['end_address'])

    for i, leg in enumerate(directions[0]['legs']):
        for j, step in enumerate(leg['steps']):
            instruction = step['html_instructions']
            duration = step['duration']['text']
            distance = step['distance']['text']
            direction_sentence += instruction.replace("<b>", "").replace("</b>", "") + f" for {duration} covering {distance}. "

    return {"question": f"Directions from {origin} to {destination}", "answer": direction_sentence}
