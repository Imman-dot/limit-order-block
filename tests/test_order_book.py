from src.order_book import OrderBook, Order

def test_match_simple_trade():
    ob = OrderBook()
    ob.insert_order(Order("B1","buy",10.0,5))
    ob.insert_order(Order("S1","sell",9.5,3))
    trades = ob.match_orders()
    assert trades == [(9.5, 3, "B1", "S1")]
    assert ob.orders["B1"].qty == 2
    assert "S1" not in ob.orders

def test_multiple_fill_and_levels():
    ob = OrderBook()
    ob.insert_order(Order("B1","buy",10,5))
    ob.insert_order(Order("B2","buy",10,2))
    ob.insert_order(Order("S1","sell",9,4))
    trades = ob.match_orders()
    assert trades == [(9, 4, "B1", "S1")]
    assert ob.orders["B1"].qty == 1
    assert "S1" not in ob.orders


