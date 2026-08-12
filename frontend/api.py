import requests
import streamlit as st

from config import API_URL


# --------------------------------------------------
# Backend Health Check
# --------------------------------------------------

def check_backend():
    try:
        response = requests.get(
            f"{API_URL}/health",
            timeout=5
        )

        return response.status_code == 200

    except requests.RequestException:
        return False


# --------------------------------------------------
# News Analysis
# --------------------------------------------------

def analyze_news(symbol):
    try:
        response = requests.post(
            f"{API_URL}/news/",
            json={
                "symbol": symbol
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Financial Analysis
# --------------------------------------------------

def analyze_financial(company, pdf_file):
    try:

        files = {
            "file": (
                pdf_file.name,
                pdf_file.getvalue(),
                "application/pdf"
            )
        }

        data = {
            "company": company
        }

        response = requests.post(
            f"{API_URL}/financial/",
            data=data,
            files=files,
            timeout=180
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Technical Analysis
# --------------------------------------------------

def analyze_technical(symbol):
    try:

        response = requests.post(
            f"{API_URL}/technical/",
            json={
                "symbol": symbol
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Risk Analysis
# --------------------------------------------------

def analyze_risk(symbol):
    try:

        response = requests.post(
            f"{API_URL}/risk/",
            json={
                "symbol": symbol
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Portfolio Analysis
# --------------------------------------------------

def analyze_portfolio(symbols):
    try:

        response = requests.post(
            f"{API_URL}/portfolio/",
            json={
                "symbols": symbols
            },
            timeout=300
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Investment Advisor
# --------------------------------------------------

def analyze_advisor(symbol, pdf_file):
    try:

        files = {
            "file": (
                pdf_file.name,
                pdf_file.getvalue(),
                "application/pdf"
            )
        }

        data = {
            "symbol": symbol
        }

        response = requests.post(
            f"{API_URL}/advisor/",
            data=data,
            files=files,
            timeout=300
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Daily Report
# --------------------------------------------------

def generate_report(symbol, pdf_file):
    try:

        files = {
            "file": (
                pdf_file.name,
                pdf_file.getvalue(),
                "application/pdf"
            )
        }

        data = {
            "symbol": symbol
        }

        response = requests.post(
            f"{API_URL}/report/",
            data=data,
            files=files,
            timeout=600
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except requests.RequestException as e:
        return {
            "error": str(e)
        }