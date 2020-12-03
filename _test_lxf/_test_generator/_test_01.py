def image_repository():
    image_id = -1
    while True:
        image_id += 1
        yield get_image_by_id(image_id)


def get_image_by_id(id):
    image_list = [1, 2, 3, 4, 5]
    return image_list[id]

# for image in image_repository():
#     print(image)

print(type(image_repository()))

ir = image_repository()
print(next(ir))
print(next(ir))
print(next(ir))
