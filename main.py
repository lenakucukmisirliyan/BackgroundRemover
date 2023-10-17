from rembg import remove

input_path = "Roni.jpg"
output_path = "output.png"          # .png arkaplansızları destekler .jpg vs desteklemez

with open(input_path, 'rb') as i:               # rb = read binary
    with open(output_path, 'wb') as o:          # wb = write binary
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)