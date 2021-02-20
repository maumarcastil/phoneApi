import json

data = {
    "name": "360",
    "logo": "https://cdn-files.kimovil.com/brands/0002/11/thumb_110250_brands_small.png",
    "devices": []
}


device = {
    "name": "360 N7 Lite",
    "img": ["https://cdn-files.kimovil.com/default/0002/55/thumb_154387_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154395_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154394_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154393_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154391_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154392_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154390_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154389_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154388_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154396_default_big.jpeg"]
}


class Device(object):
    def __init__(self, name, img):
        self.name = name
        self.img = []


class Brand(object):
    def __init__(self, data):
        self.brands = []
        self.add_brands(data)

    def add_brands(self, data):
        self.brands.append(data)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

data["devices"].append(device)


print(json.dumps(data, sort_keys=True, indent=4))