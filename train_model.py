def main():
    api_key = 'YOUR_API_KEY'  # Replace with your API key
    stations = [ ... ]  # List of metro stations

    output = []
    csv_file_path = "directions.csv"

    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['question', 'answer']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(stations)):
            for j in range(i+1, len(stations)):
                origin = stations[i] + " "
                destination = stations[j] + " "

                direction_info = get_directions(api_key, origin, destination)
                if direction_info:
                    output.append(direction_info)
                    writer.writerow(direction_info)

                reverse_direction_info = get_directions(api_key, destination, origin)
                if reverse_direction_info:
                    output.append(reverse_direction_info)
                    writer.writerow(reverse_direction_info)

    print("Data exported to", csv_file_path)

main()
