def read_rows(path):
    image_file = open(path, "rb")
    # Blindly skip the BMP header.
    image_file.seek(54)

    # We need to read pixels in as rows to later swap the order
    # since BMP stores pixels starting at the bottom left.
    rows = []
    row = []
    pixel_index = 0

    while True:
        if pixel_index == 640:
            pixel_index = 0
            rows.insert(0, row)
            if len(row) != 640 * 3:
                raise Exception("Row length is not 640*3 but " + str(len(row)) + " / 3.0 = " + str(len(row) / 3.0))
            row = []
        pixel_index += 1

        r_string = image_file.read(1)
        g_string = image_file.read(1)
        b_string = image_file.read(1)

        if len(r_string) == 0:
            # This is expected to happen when we've read everything.
            if len(rows) != 640:
                print ("Warning!!! Read to the end of the file at the correct sub-pixel (red) but we've not read 1080 rows!")
            break

        if len(g_string) == 0:
            print ("Warning!!! Got 0 length string for green. Breaking.")
            break

        if len(b_string) == 0:
            print ("Warning!!! Got 0 length string for blue. Breaking.")
            break

        r = ord(r_string)
        g = ord(g_string)
        b = ord(b_string)

        row.append(b)
        row.append(g)
        row.append(r)

    image_file.close()

    return rows

def repack_sub_pixels(rows):
    print ("Repacking pixels...")
    sub_pixels = []
    for row in rows:
        for sub_pixel in row:
            sub_pixels.append(sub_pixel)

    diff = len(sub_pixels) - 1920 * 1080 * 3
    print ("Packed", len(sub_pixels), "sub-pixels.")
    if diff != 0:
        print ("Error! Number of sub-pixels packed does not match 1920*1080: (" + str(len(sub_pixels)) + " - 1920 * 1080 * 3 = " + str(diff) +").")

    return sub_pixels

rows = read_rows("image.bmp")

output_file = open("image.csv", "w")
rows.reverse()
for row in rows:
    i = 0
    while i < 640:
        output_file.write(str(row[i * 3]) + "\n")
        output_file.write(str(row[i * 3 + 1]) + "\n")
        output_file.write(str(row[i * 3 + 2]) + "\n")
        '''
        print(row[i])
        print(row[i + 1])
        print(row[i + 2])
        '''
        i += 1       
  

output_file.close()

# This list is raw sub-pixel values. A red image is for example (255, 0, 0, 255, 0, 0, ...).
sub_pixels = repack_sub_pixels(rows)
