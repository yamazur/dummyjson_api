from pydantic import BaseModel

class CartProductPositions(BaseModel):
    id: int
    quantity: int

class CartProductDetails(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    total: float
    discountPercentage: float
    thumbnail: str

class Cart(BaseModel):
    id: int
    products: list[CartProductDetails]
    total: float
    discountedTotal: float
    userId: int
    totalProducts: int
    totalQuantity: int
    isDeleted: bool = False

class CartListResponse(BaseModel):
    carts: list[Cart]
    total: int
    skip: int
    limit: int
