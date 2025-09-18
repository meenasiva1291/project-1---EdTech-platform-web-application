**Project Name**: Automation Test Suite with Pytest and Selenium

**Overview**
This project contains automated test cases using Pytest and Selenium WebDriver following the Page Object Model (POM) design pattern.
It is configured to support cross-browser tests, read configurations from files, and generate HTML test reports.

**Project Structure**
project1_guviautomation/ - Page classes and locators

tests/ - Test cases using pytest

conftest.py - Pytest fixtures for driver setup

config.ini - Test configuration data

read_data.py - Data reading utilities

requirements.txt - Python dependencies list

**How to Extend**
Add new page objects under pages/

Add test data in Excel file used by read_data.py

Add new tests in tests/ folder

Customize pytest options and fixtures in conftest.py

**Features**
Cross-browser testing with Chrome, Firefox, and Edge.

Data-driven tests using external Excel inputs.

HTML reports generation with pytest-html.

Screenshots automatically captured for all test cases

Page Object Model to organize UI locators and actions.

**Requirements**
Python 3.8+

Selenium

pytest

pytest-html

webdriver-manager

Excel file reader (like openpyxl if used)



**Author**
 Meenakshi Sivasankaran

