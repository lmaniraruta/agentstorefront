"""Seller registration."""
import sqlite3
from fastapi import APIRouter, HTTPException
from models import SellerCreate, Seller
from db import cursor

router = APIRouter(prefix="/sellers", tags=["sellers"])


@router.post("", response_model=Seller, status_code=201)
def create_seller(body: SellerCreate):
    with cursor() as c:
        try:
            c.execute("INSERT INTO sellers (email) VALUES (?)", (body.email,))
            sid = c.lastrowid
        except sqlite3.IntegrityError:
            raise HTTPException(409, "Seller email already registered")
        except sqlite3.OperationalError as e:
            raise HTTPException(500, f"DB error: {e}")
        c.execute("SELECT * FROM sellers WHERE id = ?", (sid,))
        row = dict(c.fetchone())
    return Seller(**row)
