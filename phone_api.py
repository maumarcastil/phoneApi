import json


class Dispositivo(object):
    def __init__(self, name, img):
        self.name = name
        self.img = img


class Marca(object):
    def __init__(self, name, logo):
        self.brand = name
        self.logo = logo
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)


class Marcas(object):
    def __init__(self):
        self.brands = []

    def add_brand(self, brand):
        self.brands.append(brand)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



data_marca = Marca(
    "360", "https://cdn-files.kimovil.com/brands/0002/11/thumb_110250_brands_small.png")


nombre_dispositivo1 = "cell 1"
fotos_dispositivo1 = ["https://cdn-files.kimovil.com/default/0002/55/thumb_154387_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154395_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154394_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154393_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154391_default_big.jpeg",
                      "https://cdn-files.kimovil.com/default/0002/55/thumb_154392_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154390_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154389_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154388_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154396_default_big.jpeg"]

nombre_dispositivo2 = "cell 2"
fotos_dispositivo2 = ["https://cdn-files.kimovil.com/default/0002/55/thumb_154387_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154395_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154394_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154393_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154391_default_big.jpeg",
                      "https://cdn-files.kimovil.com/default/0002/55/thumb_154392_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154390_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154389_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154388_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154396_default_big.jpeg"]

nombre_dispositivo3 = "cell 3"
fotos_dispositivo3 = ["https://cdn-files.kimovil.com/default/0002/55/thumb_154387_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154395_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154394_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154393_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154391_default_big.jpeg",
                      "https://cdn-files.kimovil.com/default/0002/55/thumb_154392_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154390_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154389_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154388_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154396_default_big.jpeg"]

nombre_dispositivo4 = "cell 4"
fotos_dispositivo4 = ["https://cdn-files.kimovil.com/default/0002/55/thumb_154387_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154395_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154394_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154393_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154391_default_big.jpeg",
                      "https://cdn-files.kimovil.com/default/0002/55/thumb_154392_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154390_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154389_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154388_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154396_default_big.jpeg"]

nombre_dispositivo5 = "cell 5"
fotos_dispositivo5 = ["https://cdn-files.kimovil.com/default/0002/55/thumb_154387_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154395_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154394_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154393_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154391_default_big.jpeg",
                      "https://cdn-files.kimovil.com/default/0002/55/thumb_154392_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154390_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154389_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154388_default_big.jpeg", "https://cdn-files.kimovil.com/default/0002/55/thumb_154396_default_big.jpeg"]


data_dispositivo1 = Dispositivo(nombre_dispositivo1, fotos_dispositivo1)
data_dispositivo2 = Dispositivo(nombre_dispositivo2, fotos_dispositivo2)
data_dispositivo3 = Dispositivo(nombre_dispositivo3, fotos_dispositivo3)
data_dispositivo4 = Dispositivo(nombre_dispositivo4, fotos_dispositivo4)
data_dispositivo5 = Dispositivo(nombre_dispositivo5, fotos_dispositivo5)


data_marca.add_device(data_dispositivo1)
data_marca.add_device(data_dispositivo1)
data_marca.add_device(data_dispositivo3)
data_marca.add_device(data_dispositivo4)
data_marca.add_device(data_dispositivo5)


marcas = Marcas()
marcas.add_brand(data_marca)

print(marcas.to_JSON())
