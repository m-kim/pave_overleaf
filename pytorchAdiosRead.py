import adios2
def read_adios_bp(filename,
                  conditional,
                  sample_count=1080,
                  width, height):
    shape = (width,height)
    start = [0]
    count = [width*height*4]
    image_names = []
    name_to_image = {}
    with adios2.open(filename, "r") as bundle:
        for images in bundle:
            imgs = images.available_variables()
            for name, attributes in imgs.items():
                image_names.append(name)
                IMAGE = imgs.read(name, start, count)
                sample = translate(IMAGE,
                                samplecount=sample_count,
                                buffer_type=conditional,
                                shape=shape
                name_to_image[name] = sample
    return (image_names, name_to_image)
