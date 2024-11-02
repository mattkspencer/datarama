import streamlit as st
from src.ui.app import ValueInvestingApp

def main():
    app = ValueInvestingApp()
    app.run()

if __name__ == "__main__":
    main() 