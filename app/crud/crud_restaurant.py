from app.crud.base import CRUDBase

from app.schema.restaurant import Restaurants, RestaurantsCreate, RestaurantsUpdate


class CRUDRestaurant(CRUDBase[Restaurants, RestaurantsCreate, RestaurantsUpdate]):
    pass

restaurant = CRUDRestaurant(Restaurants)
