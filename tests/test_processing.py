# Tests for processing

# Uses a snippet of data for testing to see if processing.py works
import pytest

from src.data.processing import process_zip
from src.data.processing import process_mbta
from src.data.processing import process_weather
from src.data.processing import combine_data



# use a dummy input or a snippet of data?

def test_process_zip(mbta_data_zip):
  pass
def test_process_mbta(mbta_data):
  pass
def test_process_weather(weather_data):
  pass
def test_combine_data(celaned_mbta, cleaned_weather):
  pass