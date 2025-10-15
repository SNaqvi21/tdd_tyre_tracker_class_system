import pytest
from datetime import datetime
from lib.tyre_tracker import TyreTracker

"""
Given I add one tyre with position
add_tyre() returns tyres list
"""
def test_tyre_tracker_class_by_add_tyre_method_with_one_tyre():
    tt = TyreTracker()
    tt.add_tyre("offside front right")
    result = tt.list_tyres() 
    assert result == ["offside front right"]


"""
Given I add mutliple tyres with positions
add_tyre() returns latest tyre list
"""
def test_tyre_tracker_class_by_add_tyre_method_with_multiple_tyres():
    tt = TyreTracker()
    tt.add_tyre("offside front right")
    tt.add_tyre("offside rear right")
    tt.add_tyre("nearside front left")
    tt.add_tyre("nearside rear left")
    tt.add_tyre("spare")
    result = tt.list_tyres()
    assert result == ["offside front right", "offside rear right", 
                    "nearside front left", "nearside rear left", "spare"]
    

"""
Given a tyre position,
when I record a reading (pressure or tread_depth),
get_latest_reading() returns self.tryes list correctly
"""
def test_tyre_tracker_class_by_record_reading_method_with_one_tyre_pressure_and_tread_depth():
    tt = TyreTracker()
    tt.add_tyre("nearside front left")
    tt.record_reading("nearside front left", 39, 6)
    latest = tt.get_latest_reading("nearside front left") 
    assert latest["pressure"] == 39
    assert latest["tread_depth"] == 6
    assert "timestamp" in latest
    

"""
Given multiple tyre readings of a tyre,
it returns the last/latest_reading in the list
"""
def test_tyre_tracker_class_by_record_reading_method_with_muliple_readings_to_return_latest_reading():
    tt = TyreTracker()
    tt.add_tyre("nearside front left")
    tt.record_reading("nearside front left", 39, 6)
    tt.record_reading("nearside front left", 33, 6.5)
    tt.record_reading("nearside front left", 36, 6.2)
    tt.record_reading("nearside front left", 35, 6.6)
    latest = tt.get_latest_reading("nearside front left")
    assert latest["pressure"] == 35
    assert latest["tread_depth"] == 6.6
    assert "timestamp" in latest


"""
Given an entry,
it returns the timestamp alongside everything else
"""
def test_tyre_tracker_class_for_tyre_timestamp():
    tt = TyreTracker()
    tt.add_tyre("nearside front left")
    tt.record_reading("nearside front left", 39, 6)
    latest = tt.get_latest_reading("nearside front left")
    assert latest["pressure"] == 39 
    assert latest["tread_depth"] == 6
    assert "timestamp" in latest

