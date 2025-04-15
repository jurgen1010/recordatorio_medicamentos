class MedicamentoFarmacia:
    def __init__(self, id: int, farmacia_id: int, medicamento_id: int, precio: float, stock: int = 0):
        self.id = id
        self.farmacia_id = farmacia_id
        self.medicamento_id = medicamento_id
        self.precio = precio
        self.stock = stock

    def set_id(self, id: int): self.id = id
    def get_id(self) -> int: return self.id

    def set_farmacia_id(self, farmacia_id: int): self.farmacia_id = farmacia_id
    def get_farmacia_id(self) -> int: return self.farmacia_id

    def set_medicamento_id(self, medicamento_id: int): self.medicamento_id = medicamento_id
    def get_medicamento_id(self) -> int: return self.medicamento_id

    def set_precio(self, precio: float): self.precio = precio
    def get_precio(self) -> float: return self.precio

    def set_stock(self, stock: int): self.stock = stock
    def get_stock(self) -> int: return self.stock

    def __str__(self) -> str:
        return f"ID: {self.id}, FarmaciaID: {self.farmacia_id}, MedicamentoID: {self.medicamento_id}, Precio: {self.precio}, Stock: {self.stock}"
