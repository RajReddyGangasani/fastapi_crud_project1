from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib

from database import Base, get_db, engine
from schemas import ProductCreate, ProductResponse, ProductUpdate, UserCreate, UserResponse, UserUpdate
from models import Product as ProductModel, User as UserModel


#create all tables in database
Base.metadata.create_all(bind= engine)

app = FastAPI()


# ==================== PRODUCT ENDPOINTS ====================

#product CREATE ENDPOINT
@app.post("/products/", response_model= ProductResponse)
def create_product(product: ProductCreate, db:Session = Depends(get_db)):
    db_product = ProductModel(
        name = product.name,
        price = product.price,
        stock = product.stock

    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



# GET - Retrieve all products
@app.get("/products", response_model= list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products


# GET - Retrieve a product by ID
@app.get("/products/{product_id}", response_model= ProductResponse, )
def get_product(product_id: int, db: Session = Depends (get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# UPDATE - Modify an existing product
@app.patch("/products/{product_id}",  response_model= ProductResponse)
def update_product(product_id: int, Product = ProductUpdate,  db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        raise HTTPException(status_code= 404, details = "product not found")
    
    if Product.name is not None:
        db_product.name = Product.name
    if Product.price is not None:
        db_product.price = Product.price
    if Product.stock is not None:
        db_product.stock = Product.stock

    db.commit()
    db.refresh(db_product)
    return db_product
 
# DELETE - Remove a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    
    return {"message": "Product deleted successfully", "product_id": product_id}
 

# ==================== USER ENDPOINTS ====================
 
# CREATE - Add a new user

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = UserModel(
        username=user.username,
        email=user.email,
        password_hash=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
 
# READ ALL - Get all users
@app.get("/users", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users
 
# READ ONE - Get a specific user
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
 
# DELETE - Remove a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    
    return {"message": "User deleted successfully", "user_id": user_id}
 
# ==================== HEALTH CHECK ====================
 
@app.get("/health")
def health_check():
    return {"status": "ok"}


